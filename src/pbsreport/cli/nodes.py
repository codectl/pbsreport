import click

from pbsreport.api.pbs import PBSFormatter


@click.command()
@click.option(
    "--sort",
    "sort",
    help="column to sort by",
    type=click.Choice(["name", "queue", "state", "cpu_type", "comment"]),
    default="name",
    show_default=True,
)
@click.argument(
    'name', nargs=1,
    help="full or partial node name to search by",
    type=str,
    default=""
)
@click.pass_obj
def nodes(pbs, sort, name):
    """Provide metrics from cluster nodes."""
    stdout = PBSFormatter.nodes(data=pbs.nodes(name=name, sort=sort))
    print(stdout)
