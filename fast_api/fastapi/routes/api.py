<<<<<<< HEAD:fast_api/fastapi/routes/api.py
from typing import Dict
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from controller.model import Model, get_model

app = FastAPI()


class NewsRequest(BaseModel):
    text: str


class NewsResponse(BaseModel):
    sentiment: str
    

@app.post("/multilingual_news_detect", response_model=NewsResponse)
def multilingual_news_detect(request: NewsRequest, model: Model = Depends(get_model)):
    sentiment = model.multilingual_news_detect(request.text)
    return NewsResponse(
        sentiment=sentiment
    )
=======
from typing import Dict
from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from controller.model import Model, get_model

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/models", StaticFiles(directory="models"), name="models")

class NewsRequest(BaseModel):
    text: str


class NewsResponse(BaseModel):
    sentiment: str
 
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "home": "Home page"
    }
    return templates.TemplateResponse("home.html", {"request": request, "data": data})


@app.post("/multilingual_news_detect", response_model=NewsResponse)
def multilingual_news_detect(request: Request, news: str = Form(...), model: Model = Depends(get_model)):
    sentiment = model.multilingual_news_detect(news)
    return NewsResponse(
        sentiment=sentiment
    )
>>>>>>> 48e297e96e6ffcfe14c5237666c3e3b7024e0892:fast_api/routes/api.py
