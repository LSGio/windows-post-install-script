import winreg

import Logger

Consts = winreg


def addOrUpdateRegValue(rootPath: int, keyPath: str, valueName: str, keyType: int, newValue: str | int) -> bool:
    """
    Add a new registry key with the provided value.

    :param int rootPath: an HKEY constant , must be one of RegUtils.HK*
    :param str keyPath: the full path of the key
    :param valueName: the registry value to be modified inside the key
    :param int keyType: the type of the registry key TODO: finish later
    :param str newValue: the value to be set
    :rtype: bool
    :return: True if key is successfully added/updated, False otherwise.
    """

    try:
        with winreg.ConnectRegistry(None, rootPath) as root_key:
            with winreg.CreateKeyEx(root_key, keyPath, 0, winreg.KEY_WRITE) as sub_key:
                winreg.SetValueEx(sub_key, valueName, 0, keyType, newValue)
                return True
    except (OSError, WindowsError) as e:
        Logger.logD(e)
        return False


def deleteRegValue(rootPath: int, keyPath: str, valueName: str) -> bool:
    """
    Delete a given registry value if it exists.

    :param int rootPath: an HKEY constant , must be one of RegUtils.HK*
    :param str keyPath: the full path of the key
    :param str valueName: the registry value name to be deleted
    :rtype: bool
    :return: True if key is successfully deleted, False otherwise.
    """

    try:
        with winreg.ConnectRegistry(None, rootPath) as root_key:
            with winreg.CreateKeyEx(root_key, keyPath, 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.DeleteValue(sub_key, valueName)
                return True
    except (OSError, WindowsError) as e:
        Logger.logD(e)
        return False


def getValueOfRegKey(rootPath: int, keyPath: str, valueName: str) -> str:
    """
    Read the value of a given registry value name.

    :param int rootPath: an HKEY constant , must be one of RegUtils.HK*
    :param str keyPath: the full path of the key
    :param str valueName: the registry value to read from
    :rtype: str
    :return: the value as a string if it exists, an empty string otherwise.
    """

    try:
        with winreg.ConnectRegistry(None, rootPath) as root_key:
            with winreg.CreateKeyEx(root_key, keyPath, 0, winreg.KEY_READ) as sub_key:
                return winreg.QueryValueEx(sub_key, valueName)[0]
    except (OSError, WindowsError) as e:
        Logger.logD(e)
        return ""
