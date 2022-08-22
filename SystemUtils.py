import ctypes
import sys
import Globals
import Logger
import RegUtils


def requestElevatedPermissions() -> None:
    """
    Prompt the user to re-run the program as admin.
    """

    if not isRunningAsAdmin():
        # TODO : rewrite with process and return codes
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        Logger.logD('Already running as admin.')


def isRunningAsAdmin() -> bool:
    """
    Check if current process is running as admin.

    :rtype: bool
    :return: True if current process is running as admin, and False otherwise
    """

    return ctypes.windll.shell32.IsUserAnAdmin() == 1


def getOsBuildNumber() -> int:
    """
    Get the current OS build number.

    :rtype: int
    :return: The current build number
    """

    rootPath = RegUtils.Consts.HKEY_LOCAL_MACHINE
    keyPath = Globals.RegKeys.KEY_OS_INFO
    valueName = Globals.RegValueNames.VALUENAME_OS_BUILD_NUMBER
    return int(RegUtils.getValueOfRegKey(rootPath, keyPath, valueName))


def getOsEditionId() -> str:
    """
    Get the current OS edition id.

    :rtype: str
    :return: The current edition id
    """

    rootPath = RegUtils.Consts.HKEY_LOCAL_MACHINE
    keyPath = Globals.RegKeys.KEY_OS_INFO
    valueName = Globals.RegValueNames.VALUENAME_OS_EDITION
    return RegUtils.getValueOfRegKey(rootPath, keyPath, valueName)


def getOsProductName() -> str:

    editionID = getOsEditionId()
    buildNumber = getOsBuildNumber()
    if buildNumber >= Globals.WindowsBuilds.WINDOWS_11_INITAL_BUILD_NUMBER:
        return 'Windows 11 ' + editionID
    elif buildNumber >= Globals.WindowsBuilds.WINDOWS_10_INITIAL_BUILD_NUMBER:
        return 'Windows 10 ' + editionID


def notifyRegistryChanged() -> None:

    pass
