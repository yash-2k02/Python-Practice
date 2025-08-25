from fastapi import FastAPI
from routes.customer import router as customer_router
from routes.product import router as product_router
from routes.order import router as order_router
app = FastAPI()

app.include_router(customer_router, prefix="/customer", tags=["Customers"])
app.include_router(product_router, prefix="/product", tags=["Products"])
app.include_router(order_router, prefix="/order", tags=["Orders"])


