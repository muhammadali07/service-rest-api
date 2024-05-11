from sqlalchemy.ext.asyncio import AsyncSession
import datastore.users
from schema import registerAccount
import datastore

async def registratioNnewAccount(data: registerAccount, db: AsyncSession):
    async with db as session:
        try:
            if data.username == "" and data.password == "":
                raise Exception(f"username and password not be valid")
            
            res, err = await datastore.registrationNewAccount(data, session)
            if err != None:
                raise Exception(err)
            
            await session.commit()
            
            return res, None
        except Exception as e :
            return None, e
