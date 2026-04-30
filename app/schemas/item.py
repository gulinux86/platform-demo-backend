from datetime import datetime

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "todo"


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None


class ItemResponse(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
