#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `neural_summarization` package."""

import pytest

from click.testing import CliRunner

from neural_summarization import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'neural_summarization.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
