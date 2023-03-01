from zoneinfo import ZoneInfo
from zoneinfo import ZoneInfoNotFoundError

import pytest


CONTROL_CHARS = [chr(n) for n in range(32)]


@pytest.mark.parametrize(
    "key",
    ["*", "<", ">", ":", '"', "a/b", "a\\b" "|", "?"] + CONTROL_CHARS
)
def test_weird_key(key):
    with pytest.raises((ValueError, ZoneInfoNotFoundError)):
        ZoneInfo(key)
