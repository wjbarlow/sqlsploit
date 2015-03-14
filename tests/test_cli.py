import pytest
from click.testing import CliRunner
from sqlsploit import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'SQLSploit'


def test_cli_with_option(runner):
    result = runner.invoke(cli.main, ['-U Test'])
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.strip() == 'Username: Test'


def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ['-P Password'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Password: Password'
