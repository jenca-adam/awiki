import click
import functools
from .err import AwikiError
from .server import run_app
from .config import AwikiConfig
from .data import find_awiki_data_dir
from .awiki import awiki_init, awiki_reload_data, awiki_fix_notmyown, awiki_fix_myown, awiki_view

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
@click.option("-p", "--port", help="Port to run Flask on (defaults to config)", type=int)
@wrap_error
def run(port):
    conf = AwikiConfig()
    run_app(conf, debug=True, port=port or conf.port)


@main.command()
@click.option(
    "-p", "--pages_dir", prompt="Directory to store pages in", default="pages"
)
@click.option(
    "-s", "--static_dir", prompt="Directory to store static files in", default="static"
)
@click.option(
    "-a", "--awiki_dir", prompt="Directory to store internal data in", default=".awiki"
)
@click.option("-n", "name", prompt="Your SURNAME (for page sorting)", required=True)
@wrap_error
def init(pages_dir, static_dir, awiki_dir, name):
    awiki_init(pages_dir, static_dir, awiki_dir, name)

@main.command()
@click.argument("page", type=str)
@click.option(
    "-b", "--bib", help="view bib instead of markdown", is_flag=True)
@wrap_error
def view(page,bib):
    cnf = AwikiConfig()
    awiki_view(page, bib, cnf)
@main.command()
@wrap_error
def fix_notmyown():
    awiki_fix_notmyown()
@main.command()
@wrap_error
def fix_myown():
    awiki_fix_myown()



@main.command()
@wrap_error
def reload_data():
    awiki_reload_data()


if __name__ == "__main__":
    main()
