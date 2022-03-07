import click


@click.command()
@click.pass_obj
def nodes(pbs):
    """Provide metrics from cluster nodes."""
    pbs.nodes()
