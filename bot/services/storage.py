# bot/services/storage.py
from minio import Minio
from minio.error import S3Error
import json
from bot.config import settings

class MediaStorage:
    def __init__(self):
        self.client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_USE_SSL
        )
    
    async def upload_file(self, file_data, bucket: str, object_name: str) -> str:
        try:
            self.client.put_object(
                bucket_name=bucket,
                object_name=object_name,
                data=file_data,
                length=len(file_data)
            )
            return f"{bucket}/{object_name}"
        except S3Error as e:
            print(f"Error uploading file: {e}")
            raise
    
    async def delete_files(self, urls: list[str]):
        for url in urls:
            bucket, object_name = url.split('/', 1)
            try:
                self.client.remove_object(bucket, object_name)
            except S3Error as e:
                print(f"Error deleting {url}: {e}")

storage = MediaStorage()