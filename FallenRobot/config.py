class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "27777452"
    API_HASH = "140003cf869abdd2dfcf3ba27edf7ec4"

    CASH_API_KEY = "D31QL4STIWPSLALL"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://ovkhfxkp:d6SvqcZmnYmhLQBqGVmt9AMyB0DzqXPS@isilo.db.elephantsql.com/ovkhfxkp"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1002004616638"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://starxrobo:starxrobo@cluster0.efstcnr.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/612122f0681220f8a49f4.jpg"

    SUPPORT_CHAT = "raghavsupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "MGUSGI8E7QEP"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "6156380294"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = "6682780648"  # User id of sudo users
    DEV_USERS = "6682780648"  # User id of dev users
    DEMONS = "6682780648"  # User id of support users
    TIGERS = "6682780648"  # User id of tiger users
    WOLVES = "6682780648"  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
