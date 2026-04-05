import asyncio
from pydantic import BaseModel, Field, ValidationError
from typing import List

class GradeReport(BaseModel):
    """
    Data contract for student grades.
    Uses Pydantic V2 for automatic validation.
    """
    # ge = Greater than or Equal | le = Less than or Equal
    grades: List[float] = Field(..., min_length=1)

    # Validando se todas as notas estão entre 0 e 10 de forma robusta
    def validate_values(self):
        for grade in self.grades:
            if not (0 <= grade <= 10):
                raise ValueError(f"Grade {grade} is out of bounds (0-10)")

async def get_student_average(report: GradeReport) -> float:
    """
    Core business logic. Decoupled from the input source.
    """
    # Garantindo a regra de negócio antes do cálculo
    report.validate_values()
    
    total = sum(report.grades)
    return total / len(report.grades)

async def calculate_average(grades_list: List[float]) -> float:
    """
    Entrypoint function that orchestrates validation and calculation.
    """
    try:
        # Pydantic validates types and min_length here
        report = GradeReport(grades=grades_list)
        return await get_student_average(report)
    except (ValidationError, ValueError) as e:
        print(f"Validation Error: {e}")
        raise

if __name__ == "__main__":
    # Quick manual test
    sample_grades = [7.5, 8.0, 10.0]
    result = asyncio.run(calculate_average(sample_grades))
    print(f"✅ Calculation successful! Average: {result:.2f}")