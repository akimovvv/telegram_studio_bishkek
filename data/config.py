from pathlib import Path

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
# IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

PGHOST = env.str("PG_HOST")
DATABASE = env.str("PG_DATABASE")
PGUSER = env.str("PG_USER")
PGPASSWORD = env.str("PG_PASSWORD")
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}/{DATABASE}"
# f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}/{DATABASE}"

I18N_DOMAIN = 'bishkek_telegram_bot'
BASE_DIR = Path(__file__).parent.parent
LOCALES_DIR = BASE_DIR / 'locales'
