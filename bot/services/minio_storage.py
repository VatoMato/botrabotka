# bot/services/minio_storage.py
from minio import Minio
from datetime import timedelta

minio_client = Minio(
    "minio.example.com",
    access_key="your-access-key",
    secret_key="your-secret-key",
    secure=True
)

async def store_media(file_id: str):
    url = minio_client.presigned_put_object(
        "telegram-media",
        file_id,
        expires=timedelta(hours=3)
    )
    return url