"""Main server file for FastAPI application."""
import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from routers import mygo
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from fastapi.staticfiles import StaticFiles



load_dotenv()

origins = [
    'http://localhost:3000',
    'http://localhost:4000',
    'https://mygo.miyago9267.com',
    'https://mygotest.miyago9267.com',
    '*'
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(
    mygo.router,
    prefix="/mygo",
    tags=["MyGo"]
)

@app.get('/PING')
def ping() -> str:
    """Return tesing PONG"""
    return 'PONG'

IMAGE_DIR = Path(__file__).parent / 'vv_image'

# 挂载静态文件目录到 /vv
if IMAGE_DIR.exists():
    app.mount("/vv", StaticFiles(directory=IMAGE_DIR), name="vv_images")

if __name__ == "__main__":
    uvicorn.run(
        'app:app',
        host='0.0.0.0',
        port=int(os.getenv("SERVER_PORT",'3030')),
        reload=True
    )