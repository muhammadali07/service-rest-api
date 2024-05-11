from schema import registerAccount
from model import Users

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