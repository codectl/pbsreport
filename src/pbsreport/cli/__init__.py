from dataclasses import dataclass

import click
import dotenv

from .nodes import nodes

# load environment if exists
dotenv.load_dotenv(".env")

defaults = {
    "PBS_HOME": "/usr/spool/PBS",
    "PBS_EXEC": "/opt/pbs",
    "PBS_SERVER": "pbs",
}

@dataclass
class Ctx:
    server: str
    home: str
    exec: str


@click.group()
@click.option(
    "--home", "pbs_home", envvar="PBS_HOME",
    help="location of PBS working directories",
    default=defaults["PBS_HOME"],
    show_default=True
)
@click.option(
    "--exec", "pbs_exec", envvar="PBS_EXEC",
    help="location of PBS bin and sbin directories",
    default=defaults["PBS_EXEC"],
    show_default=True
)
@click.option(
    "--server", "pbs_server", envvar="PBS_SERVER",
    help="hostname of host running the server",
    default=defaults["PBS_SERVER"],
    show_default=True
)
@click.pass_context
def cli(ctx, pbs_server, pbs_home, pbs_exec):
    """Provide metrics from a PBS server."""
    ctx.obj = Ctx(
        server=pbs_server,
        home=pbs_home,
        exec=pbs_exec
    )


cli.add_command(nodes)
