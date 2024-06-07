from fastapi import FastAPI
from routers.users import router as user_router
from routers.company import router as company_router
from routers.task import router as task_router
app = FastAPI()

@app.get("/")
async def health_check():
    return "API Service is up and running"


app.include_router(user_router)
app.include_router(company_router)
app.include_router(task_router)