from zoneinfo import ZoneInfo
from zoneinfo import ZoneInfoNotFoundError

import pytest


def test_weird_key():
    with pytest.raises((ValueError, ZoneInfoNotFoundError)):
        ZoneInfo("*0800")
