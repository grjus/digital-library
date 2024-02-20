"""This module contains the configuration for the database connection."""
from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

from config.mock_data import populate_mock_data
from models import DocumentModels


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    MOCK_DATA: Optional[bool] = False

    class Config:
        env_file = ".env"
        from_attributes = True


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(
        database=client.get_default_database("digital_library"),
        document_models=DocumentModels.models,
    )
    if Settings().MOCK_DATA:
        await populate_mock_data()
