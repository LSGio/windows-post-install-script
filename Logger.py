import Globals
from datetime import datetime


def log_d(msg: str) -> None:
    if Globals.DEBUG:
        today = datetime.today().strftime("%d/%m/%Y")
        now = datetime.now().strftime("%H:%M")
        print(today, now, msg)
