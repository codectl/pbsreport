import click

from pbsreport.api.pbs import PBSFormatter


@click.command()
@click.pass_obj
def nodes(pbs):
    """Provide metrics from cluster nodes."""
    stdout = PBSFormatter.nodes(data=pbs.nodes())
    print(stdout)
