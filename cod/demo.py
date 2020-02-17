import click
from .cod import main, echo

@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.command()
def hello(name):
    echo(name)

main()
