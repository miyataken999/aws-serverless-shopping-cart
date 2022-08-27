from fastapi import FastAPI


app = FastAPI(    
        title="test",
        openapi_prefix="/Prod"
        )

@app.get("/hello")
def root():
    return {"message": "Hello World"}
    
@app.get("/cognito")
def root():
    return {"message": "Hello World"}

from mangum import Mangum
#from asgi_app import app

lambda_handler = Mangum(app) 