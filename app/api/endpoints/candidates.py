from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def create_candidate():
    pass


@app.get("/get_candidates")
async def get_candidates():
    pass


@app.put("/update_candidate/{id}")
async def update_candidate():
    pass

@app.delete("/delete_candidate/{id}")
async def delete_candidate():
    pass