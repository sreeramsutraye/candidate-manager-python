from fastapi import FastAPI
from api.request_body.user import User
from api.db.db_manager import execute_query

app = FastAPI()


@app.post("/register")
async def register_user(user: User):
    query = "INSERT INTO users (first_name, last_name, email, password, image_url, is_deleted) VALUES ($1, $2, $3, $4, $5, $6)"
    params = (user.first_name, user.last_name, user.email, user.password, None, False)
    await execute_query(query, params)
    return {"message": "User registered successfully"}


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    query = """
        UPDATE users
        SET first_name = $1, last_name = $2, email = $3, password = $4, image_url = $5, is_deleted = $6
        WHERE id = $7
    """
    params = (user.first_name, user.last_name, user.email, user.password, user.image_url, getattr(user, "is_deleted", False), user_id)
    await execute_query(query, params)
    return {"message": "User updated successfully"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = """
        UPDATE users
        SET is_deleted = TRUE
        WHERE id = $1
    """
    params = (user_id,)
    await execute_query(query, params)
    return {"message": "User soft deleted successfully"}


@app.get("/users")
async def get_users():
    query = "SELECT * FROM users;"
    user_data = await execute_query(query)
    return user_data
