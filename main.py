from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="To-Do API", version="1.0.0")

# In-memory storage
todos = {}
task_id_counter = 1

class TaskRequest(BaseModel):
    task: str

class TaskResponse(BaseModel):
    id: int
    task: str

@app.post("/todos/", response_model=TaskResponse)
async def create_todo(task_request: TaskRequest):
    """Create a new todo task"""
    global task_id_counter
    task_id = task_id_counter
    todos[task_id] = task_request.task
    task_id_counter += 1
    return TaskResponse(id=task_id, task=task_request.task)

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "To-Do API is running", "port": 8000}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



