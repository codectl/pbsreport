import click

from pbsreport.api.pbs import PBSFormatter


@click.command()
@click.pass_obj
def nodes(pbs):
    """Provide metrics from cluster nodes."""
    PBSFormatter.nodes(data=pbs.nodes())
