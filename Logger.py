
from datetime import datetime

import Globals


def log_d(msg: str) -> None:
    if Globals.DEBUG:
        today = datetime.today().strftime("%d/%m/%Y")
        now = datetime.now().strftime("%H:%M:%S:%f")
        print(today, now, msg)
