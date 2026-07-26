import asyncio

from app.db.database import (
    check_database_connection,
    engine,
)


async def main() -> None:
    try:
        await check_database_connection()
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
