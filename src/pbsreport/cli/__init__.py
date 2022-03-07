import click

from .nodes import nodes


@click.group()
def cli():
    """Provide metrics from a PBS server."""
    pass


cli.add_command(nodes)
