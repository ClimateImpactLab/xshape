#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `xshape` package."""

import pytest
from click.testing import CliRunner

from xshape import xshape
from xshape import cli

import xarray as xr
import pandas as pd


@pytest.fixture
def california_pop_by_county():
    df = pd.read_csv('tests/data/datasets/co-est2016.csv', encoding='latin1')
    ca = df[(df['STATE'] == 6) & (df['COUNTY'] > 0)].copy()
    ca['fips'] = df['STATE'] * 1000 + df['COUNTY']
    da = ca.set_index(['fips'])['POPESTIMATE2016'].to_xarray()
    da.coords['GEOID'] = ('fips', ), list(map('{:05}'.format, da.fips.values))
    return da


def test_plot(california_pop_by_county):
    ax = california_pop_by_county.swap_dims({'fips': 'GEOID'}).xshape.plot(
        'tests/data/shapefiles/CA_counties/CA_counties', encoding='latin1')


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'xshape.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
