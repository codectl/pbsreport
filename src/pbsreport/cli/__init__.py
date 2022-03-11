import click
import dotenv

from pbsreport.api.pbs import PBS
from pbsreport.cli.nodes import nodes, vnodes
from pbsreport.cli.queues import queues
from pbsreport.cli.fairshare import fairshare

# load environment if exists
dotenv.load_dotenv(".env")

defaults = {
    "PBS_HOME": "/usr/spool/PBS",
    "PBS_EXEC": "/opt/pbs",
    "PBS_SERVER": "pbs",
}


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "--home",
    "pbs_home",
    envvar="PBS_HOME",
    help="location of PBS working directories",
    type=click.Path(),
    default=defaults["PBS_HOME"],
    show_default=True,
)
@click.option(
    "--exec",
    "pbs_exec",
    envvar="PBS_EXEC",
    help="location of PBS bin and sbin directories",
    type=click.Path(),
    default=defaults["PBS_EXEC"],
    show_default=True,
)
@click.option(
    "--server",
    "pbs_server",
    envvar="PBS_SERVER",
    help="hostname of host running the server",
    default=defaults["PBS_SERVER"],
    show_default=True,
)
@click.pass_context
def cli(ctx, pbs_server, pbs_home, pbs_exec):
    """Provide metrics from a PBS server."""
    ctx.obj = PBS(server=pbs_server, exec=pbs_exec)


cli.add_command(nodes)
cli.add_command(vnodes)
cli.add_command(queues)
cli.add_command(fairshare)
