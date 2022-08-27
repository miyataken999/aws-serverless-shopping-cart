from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def root():
    return {"message": "Hello World"}
    
from mangum import Mangum
#from asgi_app import app

lambda_handler = Mangum(app) 