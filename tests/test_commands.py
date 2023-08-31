"""
Unit Tests for `commands.py`
"""

import pytest
import typer

from pdoctest import commands


def test_what_am_i() -> None:
    """Test: Say hello to NAME"""
    assert commands.numeric_intake(2, 1) == 3
    assert commands.numeric_intake(2, 0) == 2
    assert commands.numeric_intake(1, 1) == 2


def test_version_callback():
    """
    Test error and non-error exit
    """
    assert commands.version_callback(False) is None
    with pytest.raises(typer.Exit):
        commands.version_callback(True)


def test_pword() -> None:
    """doesn't really test pword"""

    assert commands.pword("bob") is None


def test_numeric_intake():
    """tests numeric_intake"""
    assert commands.numeric_intake(2, 3) == 5
