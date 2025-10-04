from fastmcp import FastMCP
from typing import Literal
import requests

# Initialize FastMCP server
mcp = FastMCP("todo_mcp_server")

@mcp.tool()
def add_todo_task(description: str, priority: Literal['Low', 'High']) -> str:
    """
    Add a new todo task with specified priority.
    
    Args:
        description: The task description
        priority: Task priority (Low or High)
    
    Returns:
        str: Success message or error message
    """
    try:
        # Format task with priority
        formatted_task = f"[{priority} Priority] {description}"
        
        # Make HTTP POST request to the FastAPI app
        response = requests.post(
            "http://127.0.0.1:8000/todos/",
            json={"task": formatted_task},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            task_data = response.json()
            return f"Successfully added task: '{task_data['task']}' (ID: {task_data['id']})"
        else:
            return f"Failed to add task. Server responded with status code: {response.status_code}"
            
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to the To-Do API server. Please ensure the FastAPI app is running on port 8000."
    except requests.exceptions.Timeout:
        return "Error: Request timed out. The server may be overloaded."
    except requests.exceptions.RequestException as e:
        return f"Error: Request failed with error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="http", port=8080)



