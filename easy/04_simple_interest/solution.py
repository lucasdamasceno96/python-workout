from pydantic import BaseModel, Field, PositiveFloat, ValidationError
from typing import Final

# Constante global para arredondamento financeiro
CURRENCY_PRECISION: Final[int] = 2

class InterestRequest(BaseModel):
    """Esquema para validação de entrada de dados de juros."""
    principal: PositiveFloat = Field(..., description="Valor inicial investido")
    annual_rate: float = Field(..., gt=0, lt=1, description="Taxa anual em decimal (ex: 0.05 para 5%)")
    years: int = Field(..., gt=0, description="Período em anos")

async def calculate_simple_interest(principal: float, rate: float, time: int) -> float:
    """
    Calcula o montante final usando a fórmula de Juros Simples: M = P(1 + rt)
    """
    try:
        # 1. Validação: Tentamos criar o objeto. Se os dados forem inválidos, pula para o 'except'
        request = InterestRequest(principal=principal, annual_rate=rate, years=time)
        
        # 2. Lógica: P * (1 + (taxa * tempo))
        # O Pydantic garante que 'request.principal', etc., sejam do tipo correto aqui.
        final_amount: float = request.principal * (1 + (request.annual_rate * request.years))
        
        # 3. Retorno: Arredonda para 2 casas decimais (padrão monetário)
        return round(final_amount, CURRENCY_PRECISION)

    except ValidationError as e:
        # Captura erros de validação do Pydantic (ex: taxa negativa, texto em vez de número)
        print(f"Erro de Validação de Dados: {e.json()}")
        raise  # Repassa o erro para ser tratado por quem chamou a função
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"Ocorreu um erro inesperado: {e}")
        raise