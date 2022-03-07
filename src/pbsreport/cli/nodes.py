import click


@click.command()
def nodes():
    """Provide metrics from cluster nodes."""
    print("Ran nodes")
