from fastapi import FastAPI
from fastapi import APIRouter
#from .models import Student
from pydantic import BaseModel

class Student(BaseModel):
    first_name: str
    last_name: str
    address: str
    date_of_birth: str
    email: str

app = FastAPI(title="Student Management System", openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.get("/students", status_code=200)
def get_all_students() -> dict:
    """Get all student records."""
    # Implement logic to fetch student data from the database
    # Return the data as a dictionary
    return {"message": "All student records retrieved successfully"}

@app.post("/students")
async def create_student(student: Student):
    # Process the student data (e.g., save to database)
    return student

@app.put("/students/{student_id}")
async def update_student(student_id: int, updated_student: Student):
    # Update the student with ID=student_id using the data in updated_student
    return {"message": f"Student {student_id} updated successfully"}

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

