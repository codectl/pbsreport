import json

from shell import Shell

from pbsreport.schemas.pbs import NodeSchema


__all__ = ('PBS',)


class PBS:
    def __init__(self, exec, server=None):
        self._exec = exec
        self.server = server

    def nodes(self, regex=None, vnodes=False, server=None, flags=''):
        flags = f" -s {server or self.server}"
        flags = f"{flags}{' -v' if vnodes else ''}"
        cmd = f"{self._exec}/bin/pbsnodes{flags}"

        data = Shell().run(cmd).output()
        nodes = NodeSchema().load(data)
        print(nodes)