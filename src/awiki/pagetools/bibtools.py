import enum
import io
import re


class BibParseError(ValueError):
    pass


def smart_quote(value):
    return '"{}"'.format(value.replace('"', '\\"'))


def smart_brace(value):
    return "{{{}}}".format(value.replace("{", "\\{").replace("}", "\\}"))


def smart_escape(value, style):
    if style == "quote":
        return smart_quote(value)
    elif style == "brace":
        return smart_brace(value)
    elif style == "best":
        if value.isnumeric():  # use id fields for numeric values
            return value
        elif "{" in value:
            return smart_quote(value)
        else:
            return smart_brace(value)


class BibParserState(enum.Enum):
    IDLE = 0
    READING_TYPE = 1
    READING_CITEKEY = 2
    READING_FIELD_KEY = 3
    READING_FIELD_VALUE = 4
    READING_FIELD_VALUE_BRACED = 5
    READING_FIELD_VALUE_QUOTED = 6
    READING_FIELD_VALUE_ID = 8


class BibParserCharTypes:
    ASCII = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'\"()*+,-./:;<=>?@[\\]^_`{|}~"
    CTKEY = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_:/."
    BTYPE = "abcdefghijklmnopqrstuvwxyz"
    FDKEY = "abcdefghijklmnopqrstuvwxyz"
    IDVAL = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-"
    LBRAC = "{"
    RBRAC = "}"
    QUOTE = '"'
    ATSGN = "@"
    BCKSL = "\\"
    WSPCE = " \t\n\r"
    COMMA = ","
    EQUAL = "="


class BibParser:
    def __init__(self):
        self.bib_type = None
        self.citekey = None
        self.fields = []
        self.state = BibParserState.IDLE
        self.accum = []
        self.done = False

    def feed(self, char):

        if not char:
            raise BibParseError("unexpected end of input")
        if self.state == BibParserState.IDLE:
            if char in BibParserCharTypes.ATSGN:
                self.accum = []
                self.state = BibParserState.READING_TYPE

            elif char in BibParserCharTypes.RBRAC:
                if self.bib_type is None:
                    raise BibParseError("disallowed char } before entry type")
                if self.citekey is None:
                    self.citekey = "".join(self.accum)  # assume empty
                self.done = True
            elif char in BibParserCharTypes.COMMA:
                if self.bib_type is None:
                    raise BibParseError("disallowed char , before entry type")
                if self.citekey is None:
                    self.citekey = "".join(self.accum)
                self.state = BibParserState.READING_FIELD_KEY
            elif char in BibParserCharTypes.EQUAL:
                if self.bib_type is None:
                    raise BibParseError("disallowed char = before entry type")
                if self.citekey is None:
                    raise BibParseError("disallowed char = before self.citekey")
                if not self.fields or self.fields[-1][1] is not None:
                    raise BibParseError("disallowed char = before the field key")
                self.state = BibParserState.READING_VALUE
            elif char not in BibParserCharTypes.WSPCE:
                raise BibParseError(
                    f"disallowed char {char} outside a field, the self.citekey, or the type"
                )

        elif self.state == BibParserState.READING_TYPE:
            char = char.lower()
            if char in BibParserCharTypes.BTYPE:
                self.accum.append(char)
            elif char in BibParserCharTypes.LBRAC:
                self.bib_type = "".join(self.accum)
                self.accum = []
                self.state = BibParserState.READING_CITEKEY
            elif char not in BibParserCharTypes.WSPCE:
                raise BibParseError(f"disallowed char {char} in the type")
        elif self.state == BibParserState.READING_CITEKEY:
            if char in BibParserCharTypes.CTKEY:
                self.accum.append(char)
            elif char in BibParserCharTypes.RBRAC:
                self.citekey = "".join(self.accum)
                self.done = True
            elif char in BibParserCharTypes.COMMA:
                self.citekey = "".join(self.accum)
                self.accum = []
                self.state = BibParserState.READING_FIELD_KEY
            elif char not in BibParserCharTypes.WSPCE:
                #raise BibParseError(f"disallowed char {char} in the citekey")
                self.accum.append(char)#this is fine?
        elif self.state == BibParserState.READING_FIELD_KEY:
            char = char.lower()
            if char in BibParserCharTypes.FDKEY:
                self.accum.append(char)
            elif char in BibParserCharTypes.EQUAL:
                self.fields.append(["".join(self.accum), None])
                self.accum = []  # reset for value reading
                self.state = BibParserState.READING_FIELD_VALUE
            elif (
                char in BibParserCharTypes.RBRAC and not self.accum
            ):  # not sure if this is allowed but we want to be as permissive as possible
                self.done = True
            elif char not in BibParserCharTypes.WSPCE:
                raise BibParseError(f"disallowed char {char} in the field key")
        elif self.state == BibParserState.READING_FIELD_VALUE:
            if char in BibParserCharTypes.LBRAC:
                self.state = BibParserState.READING_FIELD_VALUE_BRACED
            elif char in BibParserCharTypes.QUOTE:
                self.state = BibParserState.READING_FIELD_VALUE_QUOTED
            elif char in BibParserCharTypes.IDVAL:
                self.state = BibParserState.READING_FIELD_VALUE_ID
                self.feed(char)  # refeed to add to self.accum
            elif char not in BibParserCharTypes.WSPCE:
                raise BibParseError(
                    f"disallowed char {char} while determining the field value style"
                )
        elif self.state == BibParserState.READING_FIELD_VALUE_BRACED:
            if char in BibParserCharTypes.RBRAC:
                if self.accum and self.accum[-1] == "\\":
                    self.accum.append(char)
                else:
                    self.fields[-1][1] = "".join(self.accum)
                    self.accum = []
                    self.state = BibParserState.IDLE
            else:
                self.accum.append(char)

        elif self.state == BibParserState.READING_FIELD_VALUE_QUOTED:
            if char in BibParserCharTypes.QUOTE:
                if self.accum and self.accum[-1] == "\\":
                    self.accum.append(char)
                else:
                    self.fields[-1][1] = "".join(self.accum)
                    self.accum = []
                    self.state = BibParserState.IDLE
            else:
                self.accum.append(char)
        elif self.state == BibParserState.READING_FIELD_VALUE_ID:
            if (
                char in BibParserCharTypes.IDVAL or char in BibParserCharTypes.WSPCE
            ):  # allow spaces in id keys even though it's probably a bad idea
                self.accum.append(char)
            elif char in BibParserCharTypes.COMMA or char in BibParserCharTypes.RBRAC:
                self.fields[-1][1] = "".join(self.accum).strip()
                self.accum = []
                if char in BibParserCharTypes.COMMA:
                    self.state = BibParserState.READING_FIELD_KEY
                elif char in BibParserCharTypes.RBRAC:
                    self.done = True
            else:
                raise BibParseError(
                    f"disallowed char {char} while reading an unquoted, unbraced field value"
                )
        else:
            raise NotImplementedError(f"unimplemented self.state:{self.state}")


class Bib:
    def __init__(self, bib_type, citekey, fields):
        self.type = bib_type
        self.citekey = citekey
        self.fields = dict(fields)

    @classmethod
    def parse(cls, stream):
        parser = BibParser()
        while not parser.done:
            parser.feed(stream.read(1))
        return cls(parser.bib_type, parser.citekey, parser.fields)

    def __repr__(self):
        return self.serialise()

    @classmethod
    def parse_string(cls, string):
        stream = io.StringIO(string)
        return cls.parse(stream)

    @classmethod
    def plain(cls, citekey, type="article"):
        return cls(type, citekey, [])

    def serialise(self, style="best", spaces=None, sep="\n"):
        assert (
            sep.isspace()
        ), "separator must be white-space to avoid producing invalid files"
        if spaces is None:  # align
            spaces = len(self.type) + 2  # @+{+type
        lines = ["@%s{%s," % (self.type, self.citekey)]  # f-string ugky
        for field, val in self.fields.items():
            lines.append(" " * spaces + "%s=%s," % (field, smart_escape(val, style)))
        lines.append("}")
        return sep.join(lines)
