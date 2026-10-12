from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_session
from models import Order, OrderCreate, OrderUpdate, OrderStatus, StatusLog

router = APIRouter(prefix='/orders', tags=['Orders'])

