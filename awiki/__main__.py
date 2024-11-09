import click
import functools
from .err import AwikiError
from .server import run_app
from .config import AwikiConfig
from .data import find_awiki_data_dir
from .awiki import awiki_init
import sys


def wrap_error(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AwikiError as e:
            click.secho(f"{func.__name__}: {e}", err=True, fg="red")
            sys.exit(1)

    return wrapped


@click.group()
@wrap_error
def main():
    find_awiki_data_dir()


@main.command()
@wrap_error
def run():
    conf = AwikiConfig()
    run_app(conf, debug=True, port=conf.port)


@main.command()
@click.argument("pages_dir")
@click.argument("static_dir")
def init(pages_dir, static_dir):
    awiki_init(pages_dir, static_dir)


if __name__ == "__main__":
    main()
