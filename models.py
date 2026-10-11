from enum import Enum
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

# Order Status (Enum) -> Preparing, Picked Up, In Transit, Delivered
class OrderStatus(str, Enum):
    preparing = "preparing"
    picked_up = "picked Up"
    in_transit = "in_Transit"
    delivered = "delivered"

# Database Model for Order
class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_name: str
    customer_address: str
    items: str
    order_status: OrderStatus = Field(default=OrderStatus.preparing)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

# Schema for creating a new order
class OrderCreate(SQLModel):
    customer_name: str
    customer_address: str
    items: str

# Schema for updating an existing order
class OrderUpdate(SQLModel):
    order_status: Optional[OrderStatus] = None
    customer_address: Optional[str] = None
  
# Status Log
class StatusLog(SQLModel):
    order_id: int
    old_status: str
    new_status: str
    changed_at: datetime