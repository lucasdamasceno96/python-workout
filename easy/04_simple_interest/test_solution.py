import pytest
from pydantic import ValidationError
# Supondo que seu arquivo se chame main.py
from main import calculate_simple_interest

@pytest.mark.asyncio
async def test_calculation_logic():
    # R$ 1.000,00 a 10% (0.10) por 3 anos: 1000 * (1 + 0.3) = 1300
    result = await calculate_simple_interest(1000.0, 0.10, 3)
    assert result == 1300.0

@pytest.mark.asyncio
async def test_invalid_rate_fails():
    # Taxa de 1.5 (150%) é bloqueada pelo nosso 'lt=1' no Pydantic
    with pytest.raises(ValidationError):
        await calculate_simple_interest(1000.0, 1.5, 2)