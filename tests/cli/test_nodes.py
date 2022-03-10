import json
import pytest
import subprocess

from pbsreport.cli import cli


@pytest.fixture(scope="class")
def nodes_data():
    return {
        "timestamp": 1606173513,
        "pbs_version": "19.2.6.20200311140837",
        "pbs_server": "pbsserver",
        "nodes": {
            "hpcnode03": {
                "Mom": "hpcnode03",
                "ntype": "PBS",
                "state": "free",
                "pcpus": 56,
                "jobs": ["110298.hpcnode0", "110609.hpcnode0"],
                "resources_available": {
                    "arch": "linux",
                    "centos6_node": "no",
                    "host": "hpcnode03",
                    "intel_node": "yes",
                    "mem": "384000000kb",
                    "ncpus": 56,
                    "Qlist": "normal",
                    "vnode": "hpcnode03",
                },
                "resources_assigned": {"mem": "278921216kb", "ncpus": 32},
                "resv_enable": "True",
                "sharing": "default_shared",
                "last_state_change_time": 1606093393,
                "last_used_time": 1606111932,
            }
        },
    }


class TestCliNodes:
    def test_valid_nodes_no_args(self, cli_runner, nodes_data, mocker):
        mock = mocker.patch.object(subprocess, "Popen").return_value
        mocker.patch.object(
            mock, "communicate", return_value=(json.dumps(nodes_data), "")
        )
        mocker.patch.object(mock, "returncode", new=0)
        result = cli_runner.invoke(cli, ["nodes"])

        assert result.exit_code == 0
        assert len(result.stdout.splitlines()) == 3

    def test_existing_node_lookup(self, cli_runner, nodes_data, mocker):
        mock = mocker.patch.object(subprocess, "Popen").return_value
        mocker.patch.object(
            mock, "communicate", return_value=(json.dumps(nodes_data), "")
        )
        mocker.patch.object(mock, "returncode", new=0)
        result = cli_runner.invoke(cli, ["nodes", "hpcnode03"])

        assert result.exit_code == 0
        assert len(result.stdout.splitlines()) == 3

    def test_partial_node_lookup(self, cli_runner, nodes_data, mocker):
        mock = mocker.patch.object(subprocess, "Popen").return_value
        mocker.patch.object(
            mock, "communicate", return_value=(json.dumps(nodes_data), "")
        )
        mocker.patch.object(mock, "returncode", new=0)
        result = cli_runner.invoke(cli, ["nodes", "hpc"])

        assert result.exit_code == 0
        assert len(result.stdout.splitlines()) == 3

    def test_missing_node_lookup(self, cli_runner, nodes_data, mocker):
        mock = mocker.patch.object(subprocess, "Popen").return_value
        mocker.patch.object(
            mock, "communicate", return_value=(json.dumps(nodes_data), "")
        )
        mocker.patch.object(mock, "returncode", new=0)
        result = cli_runner.invoke(cli, ["nodes", "hpcnode99"])

        assert result.exit_code == 0
        assert len(result.stdout.splitlines()) == 2

