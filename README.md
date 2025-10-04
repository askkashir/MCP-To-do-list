Video 
https://drive.google.com/file/d/1vb5aU91UIDHA-roG0NkJddj7SdQ7EhPc/view?usp=sharing

# To-Do List MCP Server

A minimal Python project that implements a basic To-Do list API with Model Context Protocol (MCP) server integration for Gemini CLI.

## Project Structure

```
todo-mcp-server/
├── main.py              # FastAPI To-Do application
├── mcp_server.py        # MCP server with FastMCP
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Features

- **FastAPI To-Do API**: Simple REST API for task management
- **MCP Server**: FastMCP-based server exposing tools to Gemini CLI
- **Priority Support**: Tasks can be marked as Low or High priority
- **In-Memory Storage**: Simple dictionary-based task storage
- **Error Handling**: Graceful connection error handling

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd todo-mcp-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Step 1: Start the FastAPI Application (Terminal 1)
```bash
python main.py
```
The API will be available at `http://127.0.0.1:8000`

### Step 2: Start the MCP Server (Terminal 2)
```bash
python mcp_server.py
```
The MCP server will be available at `http://127.0.0.1:8080`

## API Endpoints

### POST /todos/
Creates a new todo task.

**Request Body:**
```json
{
  "task": "Your task description"
}
```

**Response:**
```json
{
  "id": 1,
  "task": "Your task description"
}
```

### GET /
Returns API information.

**Response:**
```json
{
  "message": "To-Do API is running",
  "port": 8000
}
```

## MCP Tools

### add_todo_task
Adds a new todo task with specified priority.

**Parameters:**
- `description` (str): The task description
- `priority` (Literal['Low', 'High']): Task priority

**Example Usage in Gemini CLI:**
```
Use the add_todo_task tool to create a high priority task for "Buy groceries"
```

## Testing the Integration

### Test API Endpoints
```bash
# Test API connection
curl http://127.0.0.1:8000/

# Create a task
curl -X POST http://127.0.0.1:8000/todos/ \
  -H "Content-Type: application/json" \
  -d '{"task": "Test task"}'
```

### Test MCP Server
The MCP server exposes the `add_todo_task` tool that:
1. Takes a task description and priority
2. Formats the task as `[Priority Priority] description`
3. Sends it to the FastAPI application
4. Returns success or error message

## Gemini CLI Integration

1. **Configure Gemini CLI** to connect to your MCP server at `http://127.0.0.1:8080`
2. **Use the tool** with prompts like:
   ```
   Add a high priority task for "Call dentist" using the add_todo_task tool
   ```
   ```
   Use add_todo_task to create a low priority task for "Read documentation"
   ```

## Project Details

### FastAPI Application (main.py)
- **Port**: 8000
- **Storage**: In-memory dictionary
- **Endpoint**: `POST /todos/` for creating tasks
- **Response**: Task with generated ID

### MCP Server (mcp_server.py)
- **Port**: 8080
- **Transport**: HTTP
- **Tool**: `add_todo_task(description: str, priority: Literal['Low', 'High'])`
- **Functionality**: Makes HTTP POST requests to FastAPI app

## Dependencies

- `fastapi`: Web framework for building APIs
- `uvicorn[standard]`: ASGI server for running FastAPI
- `fastmcp`: FastMCP framework for MCP servers
- `requests`: HTTP library for making API calls

## Error Handling

The MCP server includes comprehensive error handling for:
- Connection errors to the FastAPI app
- Request timeouts
- HTTP errors
- Unexpected exceptions

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the integration
5. Submit a pull request

## Support

For issues or questions, please open an issue in the GitHub repository.

