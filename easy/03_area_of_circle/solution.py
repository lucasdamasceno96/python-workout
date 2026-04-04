from math import pi
from typing import Final
from pydantic import BaseModel, PositiveFloat, Field, ValidationError

# Global Constant - Immutable
PRECISION_DECIMALS: Final[int] = 2

class CircleData(BaseModel):
    """Schema for circle data validation."""
    radius: PositiveFloat = Field(..., description="The radius must be a positive number.")

async def calculate_circle_area(radius: float) -> float:
    """
    Calculates the area of a circle using the formula: A = π * r²
    
    Args:
        radius: The distance from the center to the edge.
        
    Returns:
        float: The calculated area rounded to PRECISION_DECIMALS.
    """
    # Validating input using our Pydantic model
    # (This ensures the radius is positive and a valid float)
    data = CircleData(radius=radius)
    
    # Mathematical operation: Area = π * r^2
    area: float = pi * (data.radius ** 2)
    
    return round(area, PRECISION_DECIMALS)