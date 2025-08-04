from fastapi import FastAPI
from api.request_body.user import User
from api.db.db_manager import execute_query

app = FastAPI()


@app.post("/register")
async def register_user(user: User):
    query = "INSERT INTO users (first_name, last_name, email, password, image_url) VALUES ($1, $2, $3, $4, $5)"
    params = (user.first_name, user.last_name, user.email, user.password, None)
    await execute_query(query, params)
    return {"message": "User registered successfully"}


@app.get("/users")
async def get_users():
    query = "SELECT * FROM users;"
    user_data = await execute_query(query)
    print(user_data)
    return user_data
