from fastapi import FastAPI
from app.routes import file
app = FastAPI()

@app.get("/")
def landing_page():
    return{
        "message": "Hi buddy"
    }
@app.get("/health")
def health():
    return{
        "status" : "Done"
    }

app.include_router(file.router)



