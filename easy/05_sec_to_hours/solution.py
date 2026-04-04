import asyncio
from pydantic import BaseModel, Field, ValidationError

# --- Data Design ---
class TimeInput(BaseModel):
    """Schema to validate that input is a non-negative integer."""
    seconds: int = Field(ge=0, description="Total seconds must be zero or positive")

# --- Core Logic ---
async def convert_seconds_to_hms(total_seconds: int) -> str:
    """
    Converts total seconds into HH:MM:SS format using optimized math.
    """
    # divmod(a, b) retorna (a // b, a % b) - Quociente e Resto
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # f-string formatting: :02d garante 2 dígitos com padding de zero
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# --- Execution ---
async def main():
    try:
        # Simulando um input (poderia vir de uma API ou CLI)
        raw_data = {"seconds": 3661}
        validated_data = TimeInput(**raw_data)
        
        result = await convert_seconds_to_hms(validated_data.seconds)
        print(f"Formatted Time: {result}")
        
    except ValidationError as e:
        print(f"Validation Error: {e.json()}")

if __name__ == "__main__":
    asyncio.run(main())