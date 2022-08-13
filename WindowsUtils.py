
import ctypes
from os.path import join
import RegUtils
import sys


def request_elevated_permissions() -> None:
    """
    Prompt the user to re-run the program as admin.

    """
    if not is_running_as_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def is_running_as_admin() -> bool:
    """
    Check if current process is running as admin.

    :rtype: bool
    :return: True if current process is running as admin, and False otherwise
    """
    return ctypes.windll.shell32.IsUserAnAdmin() == 1


def get_windows_build_number():
    root_path = RegUtils.HKLM
    key_path = join('SOFTWARE', 'Microsoft', 'Windows NT', 'CurrentVersion')
    value_name = 'CurrentBuildNumber'
    return int(RegUtils.get_value_of_reg_key(root_path, key_path, value_name))
