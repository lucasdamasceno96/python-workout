import pytest
from pydantic import ValidationError
from main import calculate_circle_area

@pytest.mark.asyncio
async def test_calculate_circle_area_success():
    # Test with radius 3: pi * 9 = 28.2743...
    result = await calculate_circle_area(3.0)
    assert result == 28.27

@pytest.mark.asyncio
async def test_calculate_circle_area_unit_radius():
    # Test with radius 1: pi * 1^2 = 3.14
    result = await calculate_circle_area(1.0)
    assert result == 3.14

@pytest.mark.asyncio
async def test_calculate_circle_area_invalid_input_negative():
    with pytest.raises(ValidationError):
        await calculate_circle_area(-5.0)

@pytest.mark.asyncio
async def test_calculate_circle_area_invalid_input_type():
    with pytest.raises(ValidationError):
        await calculate_circle_area("invalid") # type: ignore