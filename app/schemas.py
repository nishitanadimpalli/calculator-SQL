from pydantic import BaseModel, Field

class CalculationCreate(BaseModel):
    operation: str
    operand_a: float
    operand_b: float
    user_id: int = Field(gt=0)

class CalculationOut(BaseModel):
    id: int
    operation: str
    operand_a: float
    operand_b: float
    result: float
    user_id: int
    class Config:
        from_attributes = True
