import json

import shell

from pbsreport.schemas.pbs import NodeSchema


__all__ = ('PBS',)


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
        data = response.output()
        nodes = NodeSchema().load(data, many=True)
        print(nodes)
