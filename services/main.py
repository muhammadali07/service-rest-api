from typing import Union
import requests
import json
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from fastapi import FastAPI, Request


class DataDiri(BaseModel):
    name : str
    age : int
    asal : str

class LoginUserWeb(BaseModel):
    username: str
    password: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login")
async def login_user(request: LoginUserWeb):
    print(request)
    if request.username == 'ali' and request.password == "123":
        resp = {
            "status_code": "00",
            "message": "success",
            "data": {
                "username": request.username,
                "password": request.password
            }
        }
        return resp
    else:
        resp = {
            "status_code": "02",
            "message": "gagal",
            "data": {}
        }
        return resp
    
@app.get("/tiket")
async def tiketFlight():
    resp = {
        "status_code": "00",
        "message": "success",
        "data": [
            {
                "provider": "etihad",
                "price": 1500000
            },
            {
                "provider": "qatar",
                "price": 2070000
            }

            ]
    }
    return resp
        

@app.get("/namaku/{name}") # path parameter
def read_item(name: str):
    print(name)
    return {"message": f"nama saya adalah {name}"}


@app.get("/query-paramter/{name}") # query parameter
def read_item(name: str, age:int, asal:str):
    print(name)
    return {"message": f"nama saya adalah {name} usia saat ini adalah {age} dan saya berasal dari {asal}"}

@app.post("/json-body") # body request
def getJsonBody(request:DataDiri):
    return request

@app.get("/get-list-data-user")
def read_root(
    limit = int,
    page = int
):
    
    outres = {
        "status": "00",
        "message": "success",
        "data": {
            "page": page,
            "limit": limit
        }
    }
    return outres


@app.get("/wilayah-provinsi")
def getWilayahIndo():
    url = "https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json"
    out_resp = requests.get(url)
    print(out_resp)

    return out_resp