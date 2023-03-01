from zoneinfo import ZoneInfo
from zoneinfo import ZoneInfoNotFoundError

import pytest


@pytest.mark.parametrize("key", ["*0800", "*", "0800*", "&0800"])
def test_weird_key(key):
    with pytest.raises((ValueError, ZoneInfoNotFoundError)):
        ZoneInfo(key)
