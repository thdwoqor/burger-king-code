from crawler.burgerking import BurgerKing
from sqlalchemy.orm import scoped_session

from . import database, schemas
from .models import ProductTable, TempTable


# https://pydantic-docs.helpmanual.io/usage/models/
def get_db():
    db = database.session
    try:
        yield db
    finally:
        db.close()


async def search_store(keyword: str, db: scoped_session):
    if keyword is None:
        keyword = "%"
    store_name = db.query(ProductTable).filter(ProductTable.name.like(f"%{keyword}%")).all()
    store_address = db.query(ProductTable).filter(ProductTable.address.like(f"%{keyword}%")).all()
    return max(store_name, store_address)


async def add_store(store: schemas.Store, db: scoped_session):
    store_obj = ProductTable(code=store.code, name=store.name, address=store.address, result=store.result)
    db.add(store_obj)
    db.commit()
    return store_obj


def get_result(code: schemas.CodeNumber, name: str, db: scoped_session):
    burgerking = BurgerKing()
    code_list = list(map(str, code.dict().values()))
    code = "-".join(code_list)
    result = burgerking.run(*code_list).split()[2]
    store = db.query(ProductTable).filter(ProductTable.name == name).first()
    store_obj = TempTable(code=code, name=name, address=store.address, result=result)
    db.add(store_obj)
    db.commit()
    return result
