import json
import typing
from collections import defaultdict

import shell
import tabulate

import pbsreport.utils as utils
from pbsreport.schemas.pbs import NodesSchema

__all__ = ("PBS", "PBSFormatter")


class PBS:
    def __init__(self, exec, server=None):
        self._exec = exec
        self.server = server

    def nodes(self, regex=None, vnodes=False, server=None, flags=''):
        flags = f" -s {server or self.server}"
        flags = f"{flags} -a{' -v' if vnodes else ''}"
        flags = f"{flags} -F json"
        cmd = f"{self._exec}/bin/pbsnodes{flags}"

        response = shell.Shell().run(cmd)
        if response.code != 0:
            raise shell.CommandError(response.errors(raw=True))
        data = json.loads(response.output(raw=True))
        return NodesSchema().load(data)


class PBSFormatter:

    @staticmethod
    def nodes(data: typing.List[dict], format="simple"):
        headers = ["name", "queue", "state", "cpus (t/f)",
                  "gpus (t/f)", "mem (t/f)",
                  "cpu type", "network", "comment"]
        table = [[
            d["name"], d["queue"],
            f"{utils.colored_state(d['state'])}",
            f"{d['resources_available']['cpus']} / {d['resources_assigned']['cpus']}",
            f"{d['resources_available']['gpus']} / {d['resources_assigned']['gpus']}",
            f"{d['resources_available']['mem']} / {d['resources_assigned']['mem']}",
            d["cpu_type"], d["network"], d["comment"]
        ] for d in data]

        return tabulate.tabulate(table, headers=headers, tablefmt=format)
