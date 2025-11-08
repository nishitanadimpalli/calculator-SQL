from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from schemas import CalculationCreate, CalculationOut
from crud import create_calculation, list_calculations

router = APIRouter(prefix="/calculations", tags=["calculations"])

@router.post("/", response_model=CalculationOut)
def create_calc(payload: CalculationCreate, db: Session = Depends(get_db)):
    try:
        return create_calculation(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[CalculationOut])
def fetch(db: Session = Depends(get_db)):
    return list_calculations(db)
