from fastapi import FastAPI
from fastapi import Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#from db.database import SessionLocal, engine




# Import all the required libraries:





# app code starts here:
app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")
#templates = Jinja2Templates(directory="templates")



#basic route
@app.get("/hello")
async def hello():
    return {"message": "Hello World"}



