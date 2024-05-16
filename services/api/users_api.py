from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import users_app
from utils import get_async_session, respOutCustom
from schema import registerAccount, loginUserAccount, updateDataAccount, deleteDataAccount

router = APIRouter()

@router.post("/registration-new-account")
async def registrationNewAccount(
    request: registerAccount,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await users_app.registrationNewAccount(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.post("/login-account")
async def loginAccount(
    request: loginUserAccount,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await users_app.loginAccount(request, db)
    if err != None:
        return respOutCustom("02", f"login failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.put("/update-account")
async def updateAccount(
    request: updateDataAccount,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await users_app.updateAccount(request, db)
    if err != None:
        return respOutCustom("02", f"update failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.delete("/delete-account")
async def deleteAccount(
    username: deleteDataAccount,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await users_app.deleteAccount(username, db)
    if err != None:
        return respOutCustom("02", f"delete failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)


@router.get("/get-list-acount")
async def getListAccount(
    page: int = 0,
    limit: int = 0,
    keyword: str = "",
    db: AsyncSession = Depends(get_async_session)
):
    # outResponse, err = await users_app.deleteAccount(username, db)
    # if err != None:
    #     return respOutCustom("02", f"delete failed: {err}", None)
    outResponse = ""
    
    return respOutCustom("00", "success", outResponse)
