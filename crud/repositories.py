from sqlalchemy.orm import Session
from models import Cliente

class ClienteRepository:
    @staticmethod
    def find_all(db: Session) -> list[Cliente]:
        return db.query(Cliente).all()

    @staticmethod
    def save(db: Session, cliente: Cliente) -> Cliente:
        if cliente.id:
            db.merge(cliente)
        else:
            db.add(cliente)
        db.commit()
        return cliente

    @staticmethod
    def find_by_id(db: Session, id: int) -> Cliente:
        return db.query(Cliente).filter(Cliente.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Cliente).filter(Cliente.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        cliente = db.query(Cliente).filter(Cliente.id == id).first()
        if Cliente is not None:
            db.delete(cliente)
            db.commit()