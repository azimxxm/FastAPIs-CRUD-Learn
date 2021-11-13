from fastapi import FastAPI, Path
from typing import Optional
from modeles import Student, UpdateStudent

app = FastAPI()

# GET - get information
# POST - create something new
# PUT - update
# DELETE - delete something

# How to runing this app ?
# uvicorn main:app --reload

students = {
    1: {
        "name": "Azimjon",
        "age": 17,
        "class": "year 12"
    }
}


@app.get("/")
async def index():
    return {"name": "First data"}


@app.get("/get-student/{student_id}")
async def get_student(student_id: int = Path(None, description="The ID of the student you wont to view")):
    return students[student_id]


# query parameters
# google.com/result?search=Python
@app.get("/get-by-name")
async def get_student(name: Optional[str] = Path(None, description="Search by name")):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
async def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
async def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exists"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    return students[student_id]

@app.delete("/delete-student/{student_id}")
async def delete_student (student_id: int):
    if student_id not in students:
        return {"Error":"Student does not exists"}
    del students[student_id]
    return {"Message":"Student deleted successfully"}