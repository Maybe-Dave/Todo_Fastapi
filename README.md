# Todo App with FastAPI

## Description
This project is a simple Todo application built using FastAPI. It allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks. The app uses Tortoise ORM for interacting with a SQLite database.

## Features
- **Create Todo**: Users can create new todo tasks.
- **Read Todo**: Users can retrieve a list of all todo tasks or get details of a specific task.
- **Update Todo**: Users can update existing todo tasks.
- **Delete Todo**: Users can delete todo tasks.
- **Error Handling**: Proper error handling for scenarios like non-existent tasks.

## Dependencies
- **Python 3.9+**
- **FastAPI**
- **Tortoise ORM**
- **SQLite**
- **Pydantic**
- **Uvicorn**

All dependencies are listed in the `requirements.txt` file.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Maybe-Dave/Todo_App_FastApi.git
    cd todo-app-fastapi
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    Tortoise ORM will automatically create the necessary database tables based on the models.

    ```bash
    python main.py
    ```

## Running the Application

1. **Run the FastAPI app:**

    ```bash
    uvicorn app.main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

## Endpoints

### Todo Endpoints

- `GET /todos/` - Retrieve a list of all todos.
- `GET /todos/{id}` - Retrieve a specific todo by ID.
- `POST /todos/` - Create a new todo task.
- `PUT /todos/{id}` - Update an existing todo task.
- `DELETE /todos/{id}` - Delete a todo task.

## Example Requests

- **Create a Todo:**
    ```bash
    curl -X POST "http://127.0.0.1:8000/todos/" -H "Content-Type: application/json" -d '{"task": "Buy groceries"}'
    ```

- **Get all Todos:**
    ```bash
    curl -X GET "http://127.0.0.1:8000/todos/"
    ```

- **Update a Todo:**
    ```bash
    curl -X PUT "http://127.0.0.1:8000/todos/1" -H "Content-Type: application/json" -d '{"task": "Buy vegetables"}'
    ```

- **Delete a Todo:**
    ```bash
    curl -X DELETE "http://127.0.0.1:8000/todos/1"
    ```


