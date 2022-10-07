import winreg

import Logger

Consts = winreg


def addOrUpdateRegValue(rootPath: int, keyPath: str, valueName: str, valueType: int, newValue: str | int) -> bool:
    """
    Add a new registry key with the provided value.

    Parameters:

    int rootPath : an HKEY constant , should be one of RegUtils.Consts.HK*
    str keyPath : the full path of the key
    str valueName : the registry value to be modified inside the key
    int valueType : the type of the registry value
    str | int newValue : the value to be set

    return type:
    bool

    return:
    True if key is successfully added/updated, False otherwise.
    """

    try:
        with winreg.ConnectRegistry(None, rootPath) as root_key:
            with winreg.CreateKeyEx(root_key, keyPath, 0, winreg.KEY_WRITE) as sub_key:
                winreg.SetValueEx(sub_key, valueName, 0, valueType, newValue)
                return True
    except (OSError, WindowsError) as e:
        Logger.logE(e)
        return False


def deleteRegValue(rootPath: int, keyPath: str, valueName: str) -> bool:
    """
    Delete a given registry value if it exists.

    Parameters:
    int rootPath : an HKEY constant , should be one of RegUtils.Consts.HK*
    str keyPath : the full path of the key
    str valueName : the registry value name to be deleted

    return type:
    bool

    return:
    True if key is successfully deleted, False otherwise.
    """

    try:
        with winreg.ConnectRegistry(None, rootPath) as root_key:
            with winreg.CreateKeyEx(root_key, keyPath, 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.DeleteValue(sub_key, valueName)
                return True
    except (OSError, WindowsError) as e:
        Logger.logE(e)
        return False


def getValueOfRegKey(rootPath: int, keyPath: str, valueName: str) -> str:
    """
    Read the value of a given registry value name.

    Parameters:
    int rootPath : an HKEY constant , should be one of RegUtils.Consts.HK*
    str keyPath : the full path of the key
    str valueName : the registry value to read from

    return type:
    str

    return:
    The value as a string if it exists, an empty string otherwise.
    """

    try:
        with winreg.ConnectRegistry(None, rootPath) as root_key:
            with winreg.CreateKeyEx(root_key, keyPath, 0, winreg.KEY_READ) as sub_key:
                return winreg.QueryValueEx(sub_key, valueName)[0]
    except (OSError, WindowsError) as e:
        Logger.logE(e)
        return ""
