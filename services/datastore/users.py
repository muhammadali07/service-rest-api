from schema import registerAccount, updateDataAccount, deleteDataAccount
from model import Users
from sqlalchemy import select, and_, delete, update
from fastapi.encoders import jsonable_encoder

async def registrationNewAccount(data:registerAccount, session):
    try:
        paramsInsert = Users(
            username = data.username,
            email=data.email,
            password=data.password,
            role=data.role
        )
        session.add(paramsInsert)
        return data, None
    except Exception as e:
        return None, e

async def loginAccount(email:str, password:str, session):
    try:
        query = select(Users).filter(and_(Users.email == email, Users.password == password))
        data = await session.execute(query)
        proxy = data.scalars().first()
        
        if proxy not in (None, []):
            return jsonable_encoder(proxy), None
        else:
            raise Exception("data not found")
    except Exception as e:
        return None, e

async def updateAccount(data:updateDataAccount , session):
    try:
        query = update(Users).where(Users.username == data.username).values(password = data.new_password)
        await session.execute(query)
        await session.commit()
        return data, None
    except Exception as e:
        return None, e

async def deleteAccount(data: deleteDataAccount, session):
    try:
        query = delete(Users).where(Users.username == data.username)
        await session.execute(query)
        await session.commit()
        return data, None
    except Exception as e:
        return None, e
