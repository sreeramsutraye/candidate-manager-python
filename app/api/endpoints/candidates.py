from fastapi import FastAPI
from api.request_body.candidate import Candidate
from api.db.db_manager import execute_query

app = FastAPI()

@app.post("/")
async def create_candidate():
    pass


@app.get("/get_candidates")
async def get_candidates():
    query = "SELECT * FROM candidate;"
    user_data = await execute_query(query)
    return user_data


@app.put("/update_candidate/{id}")
async def update_candidate():
    pass

@app.delete("/delete_candidate/{candidate_id}")
async def delete_candidate(candidate_id: int):
    query = """
        UPDATE users
        SET is_deleted = TRUE
        WHERE id = $1
    """
    params = (candidate_id,)
    await execute_query(query, params)
    return {"message": "User soft deleted successfully"}