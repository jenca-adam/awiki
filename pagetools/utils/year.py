from ..common.exceptions import YearException
import pprint
def year(ystr):
    x=ystr.split(',')
    for a in x:
        pprint.pprint(a)
        try:
            return int(a)
        except:
            pass
    raise YearException(f"Could not parse year string {ystr!r}") 
