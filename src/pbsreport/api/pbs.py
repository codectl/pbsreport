import json
import operator
import typing

import shell
import tabulate

from pbsreport import utils
from pbsreport.schemas.pbs import NodesSchema

__all__ = ("PBS", "PBSFormatter")


class PBS:
    def __init__(self, exec, server=None):
        self._exec = exec
        self.server = server

    def nodes(self, name="", vnodes=False, server=None, sort="name", flags=""):
        flags = f" -s {server or self.server}"
        flags = f"{flags} -a{' -v' if vnodes else ''}"
        flags = f"{flags} -F json"
        cmd = f"{self._exec}/bin/pbsnodes{flags}"

        response = shell.Shell().run(cmd)
        if response.code != 0:
            raise shell.CommandError(response.errors(raw=True))
        data = json.loads(response.output(raw=True))
        parsed_data = NodesSchema().load(data)
        sorted_data = sorted(parsed_data, key=operator.itemgetter("name"))
        return [d for d in sorted_data if name in d["name"]]


class PBSFormatter:
    @classmethod
    def nodes(cls, data: typing.List[dict], format="simple"):
        def resource(node_data, resource_type):
            available = node_data["resources_available"][resource_type]
            assigned = node_data["resources_assigned"][resource_type]
            free = available - assigned
            line = f"{free}/{available}"
            if resource_type == "mem":
                line = f"{utils.human_size(free)}/{utils.human_size(available)}"
            color = utils.color_resource(available=available, free=free)
            return utils.colored_line(line=line, color=color)

        headers = [
            "name",
            "queue",
            "state",
            "cpus (f/t)",
            "gpus (f/t)",
            "mem (f/t)",
            "cpu type",
            "network",
            "comment",
        ]
        table = map(
            cls._truncate_row,
            [
                [
                    d["name"],
                    d["queue"],
                    utils.colored_line(
                        line=d["state"], color=utils.color_state(d["state"])
                    ),
                    resource(node_data=d, resource_type="cpus"),
                    resource(node_data=d, resource_type="gpus"),
                    resource(node_data=d, resource_type="mem"),
                    d["cpu_type"],
                    d["network"],
                    d["comment"],
                ]
                for d in data
            ],
        )

        return tabulate.tabulate(table, headers=headers, tablefmt=format)

    @classmethod
    def _truncate_row(cls, row):
        return map(cls._truncate_column, row)

    @staticmethod
    def _truncate_column(column):
        column = str(column)
        return (column[:30] + "...") if len(column) > 30 else column
