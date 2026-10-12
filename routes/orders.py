from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from database import get_session
from models import Order, OrderCreate, OrderUpdate, OrderStatus, StatusLog
from datetime import datetime

router = APIRouter(prefix='/orders', tags=['Orders'])

@router.post('/', response_model=Order)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    db_order = Order(**order.model_dump())

    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    
    return db_order

@router.get('/',response_model=list[Order])
def get_orders(
    status: OrderStatus | None = Query(default = None, description="Filter orders by status"),
    created_date: str | None = Query(default = None, description="Filter orders by created date (YYYY-MM-DD)"),
    skip_limit: int = Query(default=0, ge=0, description="Number of records to skip"),
    limit: int = Query(default=20, ge=1, le=100, description="Maximum number of records to return"),
    session: Session = Depends(get_session)
):
    query = select(Order)

    if status:
        query = query.where(Order.order_status == status)
    
    if created_date:
        start = datetime.combine(created_date, datetime.min.time())
        end = datetime.combine(created_date, datetime.max.time())
        query = query.where(Order.created_at >= start and Order.created_at <= end)

    query = query.offset(skip_limit).limit(limit)

    return session.exec(query).all()