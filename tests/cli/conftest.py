import pytest
import click.testing


@pytest.fixture(scope="class")
def cli_runner():
    return click.testing.CliRunner()
