import ctypes
import sys
from os.path import join

import RegUtils


def requestElevatedPermissions() -> None:
    """
    Prompt the user to re-run the program as admin.
    """

    if not isRunningAsAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def isRunningAsAdmin() -> bool:
    """
    Check if current process is running as admin.

    :rtype: bool
    :return: True if current process is running as admin, and False otherwise
    """

    return ctypes.windll.shell32.IsUserAnAdmin() == 1


def getWindowsBuildNumber() -> str:
    """
    Get the current windows build version.

    :rtype: str
    :return: The current build version
    """

    root_path = RegUtils.Consts.HKEY_LOCAL_MACHINE
    key_path = join('SOFTWARE', 'Microsoft', 'Windows NT', 'CurrentVersion')
    value_name = 'DisplayVersion'
    return str(RegUtils.getValueOfRegKey(root_path, key_path, value_name))
