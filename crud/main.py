from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Cliente
from database import engine, Base, get_db
from repositories import ClienteRepository
from schemas import ClienteRequest, ClienteResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

#CREATE
@app.post("/api/clientes", response_model=ClienteResponse, status_code= status.HTTP_201_CREATED)
def create(request: ClienteRequest, db: Session = Depends(get_db)):
    cliente = ClienteRepository.save(db, Cliente(**request.dict()))
    return ClienteResponse.from_orm(cliente)
#READ
@app.get("/api/clientes", response_model=list[ClienteResponse])
def find_all(db: Session = Depends(get_db)):
    clientes = ClienteRepository.find_all(db)
    return [ClienteResponse.from_orm(cliente) for cliente in clientes]

#UPDATE
@app.put("/api/clientes/{id}", response_model=ClienteResponse)
def update(id: int, request: ClienteRequest, db: Session = Depends(get_db)):
    if not ClienteRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )
    curso = ClienteRepository.save(db, Cliente(**request.dict()))
    return ClienteResponse.from_orm(curso)


#DELETE
@app.delete("/api/cursos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not ClienteRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )
    ClienteRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
