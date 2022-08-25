

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
        print(Globals.LogTags.TAG_DEBUG, today, now, message)

def logI(message: str) -> None:
    """
    Print a log message, with current date and time info.

    :param message: The message to be printed
    """

    today = datetime.today().strftime("%d/%m/%Y")
    now = datetime.now().strftime("%H:%M:%S:%f")
    print(Globals.LogTags.TAG_INFO, today, now, message)


def logBuildInfo() -> None:
    """
    Print system and script info.
    mainly used for log purposes

    """

    logI(Globals.Build.appTitle)
    logI('Script running in debug mode : ' + str(Globals.Build.isDebug))
    logI('Script version : ' + Globals.Build.versionString)
    logI('Detected OS : ' + SystemUtils.getOsInfo())
    logI('OS Build Number : ' + str(SystemUtils.getOsBuildNumber()))
