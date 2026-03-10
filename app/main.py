from fastapi import FastAPI
from app.route.serie import serie

app = FastAPI()

app.include_router(serie)

@app.get("/")
async def health_check():
    return {"status": "API Online"}