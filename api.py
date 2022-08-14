from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uuid

from main import app
# from Classes import *
import db


############################
#    Init the classes      #
############################

class Person(BaseModel):
    name: str
    id: Optional[str] = uuid.uuid4()


############################
#    API Of the Website    #
############################

@app.get("/api/v1/test/{name}")
async def test(name: str):
    return {"message": f"Hello {name}"}


@app.post("/api/v1/person")
async def addPerson(person: Person):
    try:
        db.insertPerson(person)
        return {"message": "Inserted person successfully"}, 200

    except Exception as e:
        return {"error": str(e)}, 500


@app.get("/api/v1/person")
async def getAllPeople():
    try:
        return db.SelectAllPeople()

    except Exception as e:
        return {"error": str(e)}, 500


@app.get("/api/v1/person/{id}")
async def getPersonById(id: str):
    try:
        return db.SelectPersonById(id)

    except Exception as e:
        return {"error": str(e)}, 500


@app.get("/api/v1/person/delete/{id}")
async def deletePersonById(id: str):
    try:
        return db.deletePersonById(id)

    except Exception as e:
        return {"error": str(e)}, 500


@app.get("/api/v1/person/update/{id}/{name}")
async def updatePersonById(id: str, name: str):
    try:
        return db.updatePersonById(id, name)

    except Exception as e:
        return {"error": str(e)}, 500
