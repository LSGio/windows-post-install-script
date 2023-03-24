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
        sys.exit()
    else:
        Logger.logD('Already running as admin.')


def isRunningAsAdmin() -> bool:
    """
    Check if current process is running as admin.

    return type:
    bool

    return:
    True if current process is running as admin, and False otherwise
    """

    return ctypes.windll.shell32.IsUserAnAdmin() == 1


def getOsBuildNumber() -> int:
    """
    Get the current OS build number.

    return type:
    int

    return:
    The current build number
    """

    rootPath = RegUtils.Consts.HKEY_LOCAL_MACHINE
    keyPath = Globals.RegKeys.KEY_OS_INFO
    valueName = Globals.RegValueNames.VALUENAME_OS_BUILD_NUMBER
    return int(RegUtils.getValueOfRegKey(rootPath, keyPath, valueName))


def getOsEditionId() -> str:
    """
    Get the current OS edition id.

    return type:
    str

    return:
    The current edition id
    """

    rootPath = RegUtils.Consts.HKEY_LOCAL_MACHINE
    keyPath = Globals.RegKeys.KEY_OS_INFO
    valueName = Globals.RegValueNames.VALUENAME_OS_EDITION
    return RegUtils.getValueOfRegKey(rootPath, keyPath, valueName)


def getOsProductName() -> str:
    """
    Get the current OS product name.

    return type:
    str

    return:
    The current product name
    """

    rootPath = RegUtils.Consts.HKEY_LOCAL_MACHINE
    keyPath = Globals.RegKeys.KEY_OS_INFO
    valueName = Globals.RegValueNames.VALUENAME_OS_PRODUCT_NAME
    return RegUtils.getValueOfRegKey(rootPath, keyPath, valueName)


def getOsInfo() -> str:
    """
    Get the current OS product name.

    rtype:
    str

    return:
    The current product name
    TODO : finish later
    """

    productName = getOsProductName()
    editionID = getOsEditionId()
    buildNumber = getOsBuildNumber()

    if 'Windows 10' in productName:
        if buildNumber >= Globals.WindowsBuilds.WINDOWS_11_INITAL_BUILD_NUMBER:
            productName = 'Windows 11'
        elif buildNumber >= Globals.WindowsBuilds.WINDOWS_10_INITIAL_BUILD_NUMBER:
            productName = 'Windows 10'
    elif 'Windows 8' in productName:
        if buildNumber >= Globals.WindowsBuilds.WINDOWS_8_1_INITIAL_BUILD_NUMBER:
            productName = 'Windows 8.1'
        elif buildNumber >= Globals.WindowsBuilds.WINDOWS_8_INITIAL_BUILD_NUMBER:
            productName = 'Windows 8'
    return productName + ' ' + editionID
