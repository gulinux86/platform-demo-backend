from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


async def create_item(db: AsyncSession, data: ItemCreate) -> Item:
    item = Item(**data.model_dump())
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


async def list_items(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Item]:
    result = await db.execute(select(Item).offset(skip).limit(limit))
    return list(result.scalars().all())


async def get_item(db: AsyncSession, item_id: int) -> Item | None:
    result = await db.execute(select(Item).where(Item.id == item_id))
    return result.scalar_one_or_none()


async def update_item(db: AsyncSession, item_id: int, data: ItemUpdate) -> Item | None:
    values = {k: v for k, v in data.model_dump().items() if v is not None}
    if values:
        await db.execute(update(Item).where(Item.id == item_id).values(**values))
        await db.commit()
    return await get_item(db, item_id)


async def delete_item(db: AsyncSession, item_id: int) -> bool:
    result = await db.execute(delete(Item).where(Item.id == item_id))
    await db.commit()
    return result.rowcount > 0
