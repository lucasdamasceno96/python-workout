# test_main.py
import pytest
from main import convert_seconds_to_hms

@pytest.mark.asyncio
@pytest.mark.parametrize("input_seconds, expected", [
    (0, "00:00:00"),
    (59, "00:00:59"),
    (60, "00:01:00"),
    (3600, "01:00:00"),
    (3661, "01:01:01"),
    (86400, "24:00:00"),
])
async def test_convert_seconds_to_hms(input_seconds, expected):
    assert await convert_seconds_to_hms(input_seconds) == expected