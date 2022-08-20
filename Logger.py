

from datetime import datetime

import Globals
import SystemUtils


def logD(message: str) -> None:
    """
    Print a log message, with current date and time info.

    :param message: The message to be printed
    """

    if Globals.Build.isDebug:
        today = datetime.today().strftime("%d/%m/%Y")
        now = datetime.now().strftime("%H:%M:%S:%f")
        print(today, now, message)


def logBuildInfo() -> None:
    """
    Print system and script info.
    mainly used for log purposes

    """

    logD(Globals.Build.appTitle)
    logD('Script running in debug mode : ' + str(Globals.Build.isDebug))
    logD('Script version : ' + Globals.Build.versionString)
    logD('Detected OS : ' + SystemUtils.getOsProductName())
    logD('OS Build Number : ' + str(SystemUtils.getOsBuildNumber()))
