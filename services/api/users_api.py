from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import users_app
from utils import get_async_session, respOutCustom
from schema import registerAccount

router = APIRouter()

@router.post("/registration-new-account")
async def registrationNewAccount(
    request: registerAccount,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await users_app.registratioNnewAccount(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)