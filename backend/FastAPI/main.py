from fastapi import FastAPI
from routers import products, users

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hi FastApi"


@app.get("/url")
async def url():
    return {"url": "https://mikebgdev.com"}

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc