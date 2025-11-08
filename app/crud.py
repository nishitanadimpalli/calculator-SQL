from sqlalchemy.orm import Session
from models import Calculation
from schemas import CalculationCreate

def compute(op: str, a: float, b: float) -> float:
    if op == "add": return a + b
    if op == "subtract": return a - b
    if op == "multiply": return a * b
    if op == "divide":
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    raise ValueError("Unsupported operation")

def create_calculation(db: Session, data: CalculationCreate) -> Calculation:
    result = compute(data.operation, data.operand_a, data.operand_b)
    calc = Calculation(
        operation=data.operation,
        operand_a=data.operand_a,
        operand_b=data.operand_b,
        result=result,
        user_id=data.user_id
    )
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc

def list_calculations(db: Session):
    return db.query(Calculation).all()
