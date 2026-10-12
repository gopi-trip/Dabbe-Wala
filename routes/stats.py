from datetime import datetime, date
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, func
from models import Order, OrderStatus
from database import get_session

router = APIRouter(prefix='/stats', tags=['Stats'])

@router.get('/daily')
def get_daily_summary(
    summary_date: date | None = Query(default=None, description="Date for which to get the summary (YYYY-MM-DD)"),
    session: Session = Depends(get_session)
):
    if summary_date is None:
        summary_date = date.today()

    start = datetime.combine(summary_date, datetime.min.time())
    end = datetime.combine(summary_date, datetime.max.time())

    summary = {

    }

    total = 0

    for status in OrderStatus:
        count = session.exec(
            select(func.count(Order.id)).where(Order.created_at >= start, Order.created_at <= end, Order.order_status == status)
        ).one()

        summary[status.value] = count
        total += count

    return {
        "date": summary_date.isoformat(),
        "summary": summary,
        "total_orders": total,
    }

