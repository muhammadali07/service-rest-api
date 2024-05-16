from schema import registerAccount, updateDataAccount, deleteDataAccount
from model import Users
from sqlalchemy import select, and_
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
        user = session.query(Users).filter_by(username=data.username).update({Users.password: data.new_password})
        session.commit()
        return user
    except Exception as e:
        return None

async def deleteAccount(data: deleteDataAccount, session):
    try:
        user = session.query(Users).filter_by(username=data.username).delete()
        if user:
            session.delete(user)
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
