from fastapi import APIRouter

# import modul api
from .users_api import *

api_router = APIRouter()

api_router.include_router(users_api.router, prefix="/account", tags=["User Account"])