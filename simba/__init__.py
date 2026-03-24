"""
Sea Ice Mass Budget Analysis (SIMBA) Python package.

Command line tool for perfoming sea ice mass budget analyses
using sea-ice Earth System Model (ESM) outputs.
"""
__author__ = "Ollie Tooth (oliver.tooth@noc.ac.uk)"
__credits__ = "National Oceanography Centre (NOC), Southampton, UK"

from importlib.metadata import version as _version

from simba import cli

try:
    __version__ = _version("simba")
except Exception:
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "9999.0.0"

__all__ = ("cli",)