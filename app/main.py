from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from strawberry.fastapi import GraphQLRouter
from typing import List, NewType, Optional, Any
import strawberry


import json
import os
from utils import get_json

# from data_model import ModelItem

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="templates")


@strawberry.type
class ItemList:
    ids: List[str]


# @strawberry.experimental.pydantic.type(model=ModelItem)
# class ModelItem:
#     id: strawberry.auto
#     Component: strawberry.auto
#     ToolModel_Name_Example: strawberry.auto


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def items(self) -> ItemList:
        """Query for model by id (example: 9bd1a6f7-003f-4137-b6e2-03aa48721657)"""
        data = [i.strip(".json") for i in os.listdir("../data/individual_json")]
        return ItemList(ids=data)

    # @strawberry.field
    # def item_query(self, record_id: strawberry.ID) -> ModelItem:
    #     """Query for individual model by id (example: 9bd1a6f7-003f-4137-b6e2-03aa48721657)"""
    #     print(record_id)
    #     record = get_json(record_id)
    #     print(record)
    #     return ModelItem(**record)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Home"}
    )


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    d = get_json(id)
    return templates.TemplateResponse(
        "item.html", {"request": request, "id": id, "data": d}
    )


@app.get("/api/items", response_class=JSONResponse)
async def read_items_json(request: Request):
    return [i.strip(".json") for i in os.listdir("../data/individual_json")]


@app.get("/api/items/{id}", response_class=JSONResponse)
async def read_item_json(request: Request, id: str):
    return get_json(id)


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
