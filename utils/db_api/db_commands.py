from asyncpg import UniqueViolationError

from utils.db_api.schemas import User, Media

# Profile
# ____________________________________________________________________________________
async def add_user(id: int,
                   username: str,
                   language: str = None,
                   gender: int = None,
                   age: int = None,
                   agreement: int = None):
    try:
        user = User(id=id, username=username, language=language, gender=gender, age=age, agreement=agreement)
        await user.create()
    except UniqueViolationError:
        pass


async def add_media(media_id=None, media=None):
    try:
        media = Media(media_id=media_id, media=media)
        await media.create()
    except UniqueViolationError:
        pass



async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user

async def select_user_id(lan: str):
    users = await User.query.where(User.language == lan).gino.all()
    return users

async def select_media(id: int):
    media = await Media.query.where(Media.id == id).gino.first()
    return media


async def update_user(id, gender, age, agreement):
    user = await User.get(id)
    await user.update(gender=gender, age=age, agreement=agreement).apply()


async def update_user_language(id, language):
    user = await User.get(id)
    await user.update(language=language).apply()


