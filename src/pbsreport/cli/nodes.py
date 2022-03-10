import click

from pbsreport.api.pbs import PBSFormatter


@click.command()
@click.option(
    "--sort",
    "sort",
    help="column to sort by",
    type=click.Choice(
        ["name", "queue", "state", "cpus", "gpus", "mem", "cpu_type", "comment"]
    ),
    default="name",
    show_default=True,
)
@click.pass_obj
def nodes(pbs, sort):
    """Provide metrics from cluster nodes."""
    stdout = PBSFormatter.nodes(data=pbs.nodes(sort=sort))
    print(stdout)
