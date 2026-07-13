from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name:str='sakshi'
    age:Optional[int]=None

student=Student()

print(student)