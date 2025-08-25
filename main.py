from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session
from db import get_session, init_db
from models.User import UserLogin
from routes import customer_router, user_router, category_router, product_router, order_router
from auth import current_user_context, authenticate_user, create_access_token, get_current_user
from logger import logger

app = FastAPI(title="Ecommerce App | FastAPI")


app.include_router(user_router)
app.include_router(customer_router, dependencies=[Depends(get_current_user)])
app.include_router(category_router, dependencies=[Depends(get_current_user)])
app.include_router(product_router, dependencies=[Depends(get_current_user)])
app.include_router(order_router, dependencies=[Depends(get_current_user)])

@app.on_event("startup")
def start():
    init_db()


@app.post("/login")
def login(data: UserLogin, session: Session = Depends(get_session)):
    
    logger.info(f"Login attempt for username='{data.username}'")

    user = authenticate_user(data.username, data.password, session)
    if not user:
        logger.warning(f"Login failed: Incorrect credentials for username='{data.username}'")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    token = create_access_token({"sub": user.username})
    logger.info(f"Login successful for username='{user.username}' - Token issued")

    return {
        "access_token": token,
        "token_type": "bearer",
        "current_user_context": current_user_context.get(user)
    }