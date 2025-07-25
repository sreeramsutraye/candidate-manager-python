import uvicorn
from app.api.endpoints.users import app

if __name__ == "__main__":
    uvicorn.run("app.api.endpoints.users:app", host="127.0.0.1", port=8000, reload=True)