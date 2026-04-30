from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.config import settings
from app.dependencies import get_current_user
from app.services.storage import list_files, upload_file

router = APIRouter()


@router.post("/upload")
async def upload(
    file: UploadFile = File(...),
    _: dict = Depends(get_current_user),
):
    if not settings.gcs_bucket_name:
        raise HTTPException(status_code=503, detail="Storage not configured")
    content = await file.read()
    path = upload_file(
        settings.gcs_bucket_name,
        f"uploads/{file.filename}",
        content,
        file.content_type or "application/octet-stream",
    )
    return {"filename": file.filename, "path": path}


@router.get("/")
async def list_uploaded_files(_: dict = Depends(get_current_user)):
    if not settings.gcs_bucket_name:
        raise HTTPException(status_code=503, detail="Storage not configured")
    return list_files(settings.gcs_bucket_name, prefix="uploads/")
