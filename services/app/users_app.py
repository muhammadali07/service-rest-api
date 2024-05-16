import datastore

from sqlalchemy.ext.asyncio import AsyncSession

from schema import registerAccount, loginUserAccount


async def registrationNewAccount(data: registerAccount, db: AsyncSession):
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

async def loginAccount(data: loginUserAccount, db: AsyncSession):
    async with db as session:
        try:
            if data.email == "" or data.password == "":
                raise Exception(f"username and password must be provided")
            
            res, err = await datastore.loginAccount(data.email, data.password, session)
            if err is not None or res["email"] != data.email:
                raise Exception("username and password not be valid")
            
            await session.commit()

            return res, None
        except Exception as e:
            return None, e

async def updateAccount(data: dict, db: AsyncSession):
    async with db as session:
        try:
            # Implement update logic here
            res, err = datastore.updateAccount()
            await session.commit()
            return "Account updated successfully", None
        except Exception as e:
            return None, e

async def deleteAccount(username: str, db:AsyncSession):
    async with db as session:
        try:
            res, err = datastore.deleteAccount(username, db)
            await session.commit()
            return "Account deleted successfully", None
        except Exception as e:
            return None, e

