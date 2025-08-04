import asyncpg
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

postgres_db = dict(
    host=os.getenv("DB_HOST", "localhost"),
    database=os.getenv("DB_NAME", "candidate-manager"),
    port=int(os.getenv("DB_PORT", 5432)),
    user=os.getenv("DB_USER", "sreeramsutraye"),
    password=os.getenv("DB_PASSWORD", ""),
)

_pool = None

async def get_pool():
    global _pool
    if _pool is None:
        _pool = await asyncpg.create_pool(**postgres_db)
    return _pool

async def validate_connection():
    try:
        pool = await get_pool()
        async with pool.acquire() as conn:
            result = await conn.fetchval("SELECT 1;")
        return result == 1
    except Exception as e:
        print(f"Error connecting to database from Python: {e}")
        return False

async def execute_query(query: str, params: tuple = ()):
    pool = await get_pool()
    async with pool.acquire() as conn:
        # Check if the query is a SELECT statement to determine the correct method
        if query.strip().upper().startswith("SELECT"):
            # Use fetch() for queries that return rows
            return await conn.fetch(query, *params)
        else:
            # Use execute() for queries that don't return data (e.g., INSERT, UPDATE, DELETE)
            await conn.execute(query, *params)
            return None

if __name__ == "__main__":
    async def main():
        is_valid = await validate_connection()
        print(f"Connection valid: {is_valid}")

    asyncio.run(main())