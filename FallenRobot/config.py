class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "16051908"
    API_HASH = "abf9b83f9ca40cf9f5ba9bf6e6afaa8b"

    CASH_API_KEY = "V3GINZ5GSBYKPMF1"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://ovkhfxkp:d6SvqcZmnYmhLQBqGVmt9AMyB0DzqXPS@isilo.db.elephantsql.com/ovkhfxkp"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001954221487"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://starxrobo:starxrobo@cluster0.efstcnr.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/b8ec8da5949144c58aa89.jpg"

    SUPPORT_CHAT = "DabangTheBrand"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "G1VE375UCXVX"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5999224089"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = "6144223366"  # User id of sudo users
    DEV_USERS = "6144223366"  # User id of dev users
    DEMONS = "6144223366"  # User id of support users
    TIGERS = "6144223366"  # User id of tiger users
    WOLVES = "6144223366"  # User id of whitelist users

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
