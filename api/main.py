from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount('/static', StaticFiles(directory='../ui/dist'))

templates = Jinja2Templates(directory='../ui')

class Item(BaseModel):
    name: str
    description: str

@app.get('/', response_model=Item)
async def index(request: Request):
    item = Item(name='123', description='234')
    return templates.TemplateResponse('index.html', {'request': request, 'item': item})
