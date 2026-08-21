from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 39170545))
        self.API_HASH = getenv("API_HASH","65959028b3bddfd808d52d0f93749bc0")

        self.BOT_TOKEN = getenv("BOT_TOKEN","8628186514:AAFru9OFAFdsRa3Lze31CA3jzPDrv8UajCE")
        self.MONGO_URL = getenv("MONGO_URL","mongodb+srv://Che3434:Che3434@cluster0.oemtavn.mongodb.net/?appName=Cluster0")

        self.LOGGER_ID = int(getenv("LOGGER_ID", -1003712681521))
        self.OWNER_ID = list(map(int, getenv("OWNER_ID", "8745446616").split(",")))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))
        self.STICKER_ID = getenv("STICKER_ID", "")
        self.SESSION1 = getenv("SESSION", "BAJVsfEAjln36gI4_N8S-QoXWRlNzAKrC88014MfiBvcSORRMc9x_B04zMs5LaWwIrguVqpvMH9fSdKsOIlwg7ab0dpu9Ucg5_CU6KNwnxtaOJ-fzY0xM0BYvwr7I054SoxlwEtoBJruiu_RE6IGIBSWBIqizUlRxO9ln6GdFLAW2dVfN5t6-iqPeKnppoICYxUp5MfDABQRpQeuLwqXG0mICjFTL91IxcqJvrRutiYAkrJJil0A0d61b16XgNxuPwQRqrDskpyg_mipsvg4ldLL8zPjr-sh5Sa_22UUe7c6gKkSlBMK5zMVkSGf60LdclUZYH7EofiPsMIhjp4h69qgCvlF9AAAAAII_dZ9AA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/destekkkk4")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/destekkkk4")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/ynwsxi.png")
        self.START_IMG = getenv("START_IMG", "").split()

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
