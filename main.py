from fastapi import FastAPI
import uvicorn
app = FastAPI()
from app import fun

@app.get("/")
async def root():
    return {"message": "Hello World"}

@fun.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=8080, reload=True)
