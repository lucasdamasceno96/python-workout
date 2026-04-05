import pytest
from main import GradeReport, get_student_average

@pytest.mark.asyncio
async def test_calculate_average_success():
    report = GradeReport(grades=[10.0, 8.0, 6.0])
    result = await get_student_average(report)
    assert result == 8.0

@pytest.mark.asyncio
async def test_calculate_average_empty_list():
    with pytest.raises(ValueError): # Ou ValidationError do Pydantic
        GradeReport(grades=[])