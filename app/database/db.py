from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

Base = declarative_base()
engine = create_async_engine(settings.POSGR_URL, future= True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def init_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)