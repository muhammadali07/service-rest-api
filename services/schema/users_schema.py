from pydantic import BaseModel

class registerAccount(BaseModel):
    username : str = "muh ali bakhtiar"
    email : str = "muhalibakhtiar@mail.com"
    password: str = "12233444"
    role : str = "admin"