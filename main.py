from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.item import Item

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hola World"}


#  Path Parameters
@app.get("/items/{item_id}")
async def read_item(item_id): # http://127.0.0.1:8000/items/4
    return {"item_id": item_id}


# Query Parameters
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): # http://127.0.0.1:8000/items/?skip=0&limit=10
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

    return fake_items_db[skip : skip + limit]


# Post API
@app.post("/items/")
async def create_item(item: Item):
    '''
    http://127.0.0.1:8000/items/
    request body: {
      "name": "string",
      "description": "string",
      "price": 11,
      "tax": 2
    }
    '''
    return item


# TEMPLATE View
@app.get("/items/show/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item_template.html", context={"id": id}
    )