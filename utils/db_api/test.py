import asyncio

from data import config
from utils.db_api.db_gino import db
import db_commands
import static_files


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()
    print("adding usres...")
    await db_commands.add_media(media='first.jpg')
loop = asyncio.get_event_loop()
loop.run_until_complete(test())