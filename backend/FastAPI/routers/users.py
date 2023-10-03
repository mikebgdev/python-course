from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"message": "No encontrado"}})


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Mike", surname="Ballester", url="https://mikebgdev.dev", age=29),
              User(id=2, name="Miki", surname="Dev", url="https://mikebgdev.com", age=29),
              User(id=3, name="User", surname="Random", url="https://user.com", age=33)]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Mike", "surname": "Ballester", "url": "https://mikebgdev.com", "age": 29},
            {"name": "Miki", "surname": "Dev", "url": "https://mikebgdev.com", "age": 29},
            {"name": "User", "surname": "Random", "url": "https://user.com", "age": 33}]


@router.get("/")
async def users():
    return users_list


@router.get("/{id}")  # Path
async def user(id: int):
    return search_user(id)


@router.get("/")  # Query
async def user(id: int):
    return search_user(id)


@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.append(user)
    return user


@router.put("/")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user


@router.delete("/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
