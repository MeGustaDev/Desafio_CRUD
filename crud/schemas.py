from pydantic import BaseModel

# classes para representar os dados que serão recebidos e retornados
class ClienteBase(BaseModel):
    id: int
    nome: str

class ClienteRequest(ClienteBase):
    ...

class ClienteResponse(ClienteBase):
    id: int

    class Config:
        orm_mode = True
