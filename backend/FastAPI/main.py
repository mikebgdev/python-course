from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

@app.get("/")
async def root():
    return "Hi FastApi"


@app.get("/url")
async def url():
    return {"url": "https://mikebgdev.com"}

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc