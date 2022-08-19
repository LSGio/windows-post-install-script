from os.path import join
from TaskRunner import runnableTask
import Globals
import RegUtils


@runnableTask
def hideCortanaButton(hide: bool = True) -> bool:
    """
    Hide Cortana button in taskbar.

    :param bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_SHOW_CORTANA_BUTTON
    value_name = Globals.RegValueNames.VALUENAME_SHOW_CORTANA_BUTTON
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def hideTaskViewButton(hide: bool = True) -> bool:
    """
    Hide Task View button in taskbar.

    :param bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_SHOW_TASK_VIEW_BUTTON
    value_name = Globals.RegValueNames.VALUENAME_SHOW_TASK_VIEW_BUTTON
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def hideSearchBar(hide: bool = True) -> bool:
    """
    Hide Search from taskbar.

    :param bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_SEARCHBAR_VIEW_MODE
    value_name = Globals.RegValueNames.VALUENAME_SEARCHBAR_VIEW_MODE
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 2
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def hideNewsAndInterests(hide: bool = True) -> bool:
    """
    Hide News and interests button in taskbar.

    :param bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_NEWS_AND_INTERESTS_VIEW_MODE
    value_name = Globals.RegValueNames.VALUENAME_NEWS_AND_INTERESTS_VIEW_MODE
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 2 if hide else 0
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def showExtensionsForKnownFiletypes(show: bool = True) -> bool:
    """
    Show file extensions for known filetypes.

    :param bool show: True to show, False to hide.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_HIDE_FILE_EXTENSIONS
    value_name = Globals.RegValueNames.VALUENAME_HIDE_FILE_EXTENSIONS
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if show else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def openThisPcInsteadOfQuickAccess(toggle: bool = True) -> bool:
    """
    Open This PC instead of Quick access when opening a new explorer window.

    :param bool toggle: True to open This PC, False to open Quick access.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_OPEN_THIS_PC_OR_QUICK_ACCESS
    value_name = Globals.RegValueNames.VALUENAME_OPEN_THIS_PC_OR_QUICK_ACCESS
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 1 if toggle else 2
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def hideRecentFilesInExplorer(hide: bool = True) -> bool:
    """
    Hide recently used files in Quick access.

    :param bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_SHOW_RECENT_FILES_IN_EXPLORER
    value_name = Globals.RegValueNames.VALUENAME_SHOW_RECENT_FILES_IN_EXPLORER
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def hideFrequentFilesInExplorer(hide: bool = True) -> bool:
    """
    Hide frequently used folders in Quick access.

    :param bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_SHOW_FREQUENT_FILES_IN_EXPLORER
    value_name = Globals.RegValueNames.VALUENAME_SHOW_FREQUENT_FILES_IN_EXPLORER
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def toggleDeliveryOptimization(toggle: bool = False) -> bool:
    """
    Enable or disable Delivery Optimization service.

    :param bool toggle: True to enable, False to disable.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_LOCAL_MACHINE
    key_path = Globals.RegKeys.KEY_TOGGLE_DELIVERY_OPTIMIZATION
    value_name = Globals.RegValueNames.VALUENAME_TOGGLE_DELIVERY_OPTIMIZATION
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 2 if toggle else 4
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)

@runnableTask
def showThisPcDesktopIcon(show: bool = True) -> bool:
    """
    Show or hide This PC desktop icon.

    :param bool show: True to show, False to hide.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_LOCAL_MACHINE
    key_path = Globals.RegKeys.KEY_HIDE_DESKTOP_ICONS
    value_name = Globals.RegValueNames.VALUENAME_HIDE_THIS_PC_ICON
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if show else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def showControlPanelDesktopIcon(show: bool = True) -> bool:
    """
    Show or hide Control Panel desktop icon.

    :param bool show: True to show, False to hide.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_LOCAL_MACHINE
    key_path = Globals.RegKeys.KEY_HIDE_DESKTOP_ICONS
    value_name = Globals.RegValueNames.VALUENAME_HIDE_CONTROL_PANEL_ICON
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if show else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def showRecycleBinDesktopIcon(show: bool = True) -> bool:
    """
    Show or hide Recycle Bin desktop icon.

    :param bool show: True to show, False to hide.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_LOCAL_MACHINE
    key_path = Globals.RegKeys.KEY_HIDE_DESKTOP_ICONS
    value_name = Globals.RegValueNames.VALUENAME_HIDE_RECYCLE_BIN_ICON
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if show else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def showNetworkDesktopIcon(show: bool = True) -> bool:
    """
    Show or hide Network desktop icon.

    :param bool show: True to show, False to hide.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_LOCAL_MACHINE
    key_path = Globals.RegKeys.KEY_HIDE_DESKTOP_ICONS
    value_name = Globals.RegValueNames.VALUENAME_HIDE_NETWORK_ICON
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if show else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def showUserFolderDesktopIcon(show: bool = True) -> bool:
    """
    Show or hide User folder desktop icon.

    :param bool show: True to show, False to hide.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_LOCAL_MACHINE
    key_path = Globals.RegKeys.KEY_HIDE_DESKTOP_ICONS
    value_name = Globals.RegValueNames.VALUENAME_HIDE_USERS_FILES_ICON
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if show else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)