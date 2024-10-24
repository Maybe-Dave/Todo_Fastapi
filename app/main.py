from fastapi import FastAPI
from api.routers.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise
import uvicorn

app = FastAPI()

app.include_router(todo_router)

register_tortoise(  
    app=app,
    db_url="sqlite://todo.db",
    add_exception_handlers=True,
    generate_schemas=True,
    modules={"models": ["api.models.todo"]},
)
#Hi
@app.get("/")
def index():
    return{"status": "Todo App is Running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)