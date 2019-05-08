import os
import pytest
from advisor import to_usd

def test_to_usd():
    assert to_usd(5) == "$5.00"