#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `admindojo` package."""

import pytest

from click.testing import CliRunner

from admindojo import admindojo
from admindojo import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.cli, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

    update_result = runner.invoke(cli.cli, ['update'])
    assert update_result.exit_code == 0
    assert 'To update please....' in update_result.output
