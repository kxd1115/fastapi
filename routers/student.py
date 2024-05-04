from fastapi import APIRouter
from database.student import *

studentAPI = APIRouter()

@studentAPI.get('/student')
async def getAllStudents():
    students = await Student.all().values('name', 'clas__name', "courses__name")
    return students