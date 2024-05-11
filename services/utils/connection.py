from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = "{}+{}://{}:{}@{}:{}/{}".format("postgresql", "asyncpg", "codingnowuser", "codingnowpassword","localhost", 5492, "codingnow" )

# create an instance connection
engine = create_async_engine(
    url=url
)

# create session async
async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False
)

metadata = MetaData()
Base = declarative_base(metadata=metadata)


async def get_async_session():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()

