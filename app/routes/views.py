import os
from typing import Optional

import db.schemas as schemas
import db.services as services
import fastapi
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import scoped_session

router = APIRouter()

# templates = Jinja2Templates(directory=os.path.abspath(os.path.expanduser("templates")))
templates = Jinja2Templates(directory="templates")

templates.env.globals["STATIC_URL"] = "/static"


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@router.get("/store")
async def search_store(keyword: Optional[str] = None, db: scoped_session = fastapi.Depends(services.get_db)):
    return await services.search_store(keyword, db)


@router.post("/store")
async def add_store(store: schemas.Store, db: scoped_session = fastapi.Depends(services.get_db)):
    return await services.add_store(store, db)


# https://stackoverflow.com/questions/62384392/python-fastapi-unprocessable-entity-error
@router.post("/update/{name}", response_class=HTMLResponse)
async def update_store(request: Request, name: str):
    data = jsonable_encoder(await request.form())

    return templates.TemplateResponse(
        "loading.html",
        {"request": data, "name": name},
    )


@router.post("/result/{name}")
def get_result(code: schemas.CodeNumber, name: str, db: scoped_session = fastapi.Depends(services.get_db)):
    return services.get_result(code, name, db)
