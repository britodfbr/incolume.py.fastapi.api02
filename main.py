import uvicorn
from incolume.py.fastapi.api02.server import app

if __name__ == '__main__':
    uvicorn.run(app, port = 5000, host = "0.0.0.0")
