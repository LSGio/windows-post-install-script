import winreg

Consts = winreg


def add_or_update_reg_value(root_path: int, key_path: str, value_name: str, key_type: int, new_value: str) -> bool:
    """
    Add a new registry key with the provided value.

    :param int root_path: an HKEY constant , must be one of RegUtils.HK*
    :param str key_path: the full path of the key
    :param value_name: the registry value to be modified inside the key
    :param int key_type: the type of the registry key TODO: finish later
    :param str new_value: the value to be set
    :rtype: bool
    :return: True if key is successfully added/updated, False otherwise.
    """

    try:
        with winreg.ConnectRegistry(None, root_path) as root_key:
            with winreg.CreateKeyEx(root_key, key_path, 0, winreg.KEY_WRITE) as sub_key:
                winreg.SetValueEx(sub_key, value_name, 0, key_type, new_value)
                return True
    except (OSError, WindowsError):
        return False


def delete_reg_value(root_path: int, key_path: str, value_name: str) -> bool:
    """
    Delete a given registry value if it exists.

    :param int root_path: an HKEY constant , must be one of RegUtils.HK*
    :param str key_path: the full path of the key
    :param str value_name: the registry value name to be deleted
    :rtype: bool
    :return: True if key is successfully deleted, False otherwise.
    """

    try:
        with winreg.ConnectRegistry(None, root_path) as root_key:
            with winreg.CreateKeyEx(root_key, key_path, 0, winreg.KEY_ALL_ACCESS) as sub_key:
                winreg.DeleteValue(sub_key, value_name)
                return True
    except (OSError, WindowsError):
        return False

    pass


def get_value_of_reg_key(root_path: int, key_path: str, value_name: str) -> str:
    """
    Read the value of a given registry value name.

    :param int root_path: an HKEY constant , must be one of RegUtils.HK*
    :param str key_path: the full path of the key
    :param str value_name: the registry value to read from
    :rtype: str
    :return: the value as a string if it exists, an empty string otherwise.
    """

    try:
        with winreg.ConnectRegistry(None, root_path) as root_key:
            with winreg.CreateKeyEx(root_key, key_path, 0, winreg.KEY_READ) as sub_key:
                return winreg.QueryValueEx(sub_key, value_name)[0]
    except (OSError, WindowsError) as e:
        return ""
