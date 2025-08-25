""""
OrderItemCreate - to create a new order item ( contains product id and quantity )
OrderItem - display order item details ( id, order_ id and price )
OrderCreate - to create a new order ( customer id and list of items ie quantity and price )
Order - used to display order information
"""


from datetime import datetime
from pydantic import BaseModel
from typing import List

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
   
    
class OrderItem(OrderItemCreate):
    id: int
    order_id: int
    price_at_purchase: float

    
class OrderCreate(BaseModel):
    customer_id: int
    items: List[OrderItemCreate]


class Order(BaseModel):
   id: int
   customer_id: int
   order_date: datetime
   items: List[OrderItem]