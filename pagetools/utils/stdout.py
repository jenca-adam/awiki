import sys
import contextlib
import io

@contextlib.contextmanager
def capture_stdout():
    stio=io.StringIO()
    old=sys.stdout
    sys.stdout=stio
    yield stio
    sys.stdout=old
