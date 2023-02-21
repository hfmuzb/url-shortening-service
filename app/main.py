import uvicorn
from fastapi import FastAPI

from routers import base_router

app = FastAPI()

app.include_router(base_router.router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
