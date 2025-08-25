from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from models import Category, CategoryCreate, CategoryUpdate
from db import get_session
from models.User import UserModel
from auth import get_current_user
from logger import logger

router = APIRouter(prefix="/category", tags=["Category"])


@router.post("/create")
async def create_category(category: CategoryCreate, session: AsyncSession = Depends(get_session), current_user: UserModel = Depends(get_current_user)):

    logger.info(f"User '{current_user.username}' attempting to create category '{category.category_name}'")

    result = await session.exec(
        select(Category).where(Category.category_name == category.category_name)
    )
    
    existing_category = result.one_or_none()

    if existing_category:
        logger.warning(f"Category creation failed: '{category.category_name}' already exists")
        raise HTTPException(status_code=400, detail="Category already exists")
    
    db_category = Category(
        **category.model_dump(),
        created_by=current_user.username,
        updated_by=current_user.username
    )
    
    session.add(db_category)
    await session.commit()
    await session.refresh(db_category)

    logger.info(f"Category '{db_category.category_name}' created successfully by user '{current_user.username}' (ID={db_category.category_id})")
    return db_category


@router.patch("/update/{id}")
async def update_category(id: int, data: CategoryUpdate, current_user: UserModel = Depends(get_current_user), session: AsyncSession = Depends(get_session)):

    logger.info(f"User '{current_user.username}' attempting to update category ID={id}")

    category = await session.get(Category, id)
    if not category:
        logger.error(f"Category update failed: ID={id} not found")
        raise HTTPException(status_code=404, detail="Category not found")
    
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(category, key, value)
    
    category.updated_by = current_user.username

    await session.commit()
    await session.refresh(category)

    logger.info(f"Category ID={id} updated successfully by user '{current_user.username}'")
    return category


@router.delete("/delete/{id}")
async def delete_category(id: int, current_user: UserModel = Depends(get_current_user), session: AsyncSession = Depends(get_session)):

    logger.info(f"User '{current_user.username}' attempting to delete category ID={id}")

    category = await session.get(Category, id)

    if not category:
        logger.error(f"Category deletion failed: ID={id} not found")
        raise HTTPException(status_code=400, detail="Category not found")

    category.is_deleted = True
    category.updated_by = current_user.username
    await session.commit()
    await session.refresh(category)

    logger.info(f"Category ID={id} marked as deleted by user '{current_user.username}'")
    return {"message": "Category deleted"}


@router.get("/all")
async def get_all_categories(session: AsyncSession = Depends(get_session)):

    logger.info("Fetching all active categories")
    results = await session.exec(select(Category).where(Category.is_deleted == False))
    categories = results.all()
    logger.info(f"Retrieved {len(categories)} categories")
    return categories


@router.get("/{id}")
async def get_single_category(id: int, session: AsyncSession = Depends(get_session)):

    logger.info(f"Fetching category with ID={id}")
    result = await session.exec(
        select(Category).where((Category.category_id == id) & (Category.is_deleted == False))
    )
    
    category = result.one_or_none()
    
    if not category:
        logger.error(f"Category fetch failed: ID={id} not found")
        raise HTTPException(status_code=404, detail="Category not found")

    logger.info(f"Category retrieved successfully: {category.category_name} (ID={id})")
    return category
