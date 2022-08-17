from os.path import join

import Globals
import RegUtils
from TaskRunner import runnableTask


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
    value_name = 'ShowCortanaButton'
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
    value_name = 'ShowTaskViewButton'
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
    value_name = 'SearchboxTaskbarMode'
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
    value_name = 'ShellFeedsTaskbarViewMode'
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
    value_name = 'HideFileExt'
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
    value_name = 'LaunchTo'
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
    value_name = 'ShowRecent'
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
    value_name = 'ShowFrequent'
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
    value_name = 'Start'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 2 if toggle else 4
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def addIconsToDesktop() -> bool:
    """
    Add This PC, Control Panel and Users Files icons to the desktop.

    :rtype: bool.
    :return: True if operation was successful, False otherwise.
    """
    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'HideDesktopIcons',
                    'NewStartPanel')

    key_type = RegUtils.Consts.REG_DWORD

    result = RegUtils.addOrUpdateRegValue(root_path, key_path, Globals.RegKeys.KEY_HIDE_THIS_PC_ICON, key_type, 0) and \
             RegUtils.addOrUpdateRegValue(root_path, key_path, Globals.RegKeys.KEY_HIDE_CONTROL_PANEL_ICON, key_type, 0) and \
             RegUtils.addOrUpdateRegValue(root_path, key_path, Globals.RegKeys.KEY_HIDE_USERS_FILES_ICON, key_type, 0)

    return result
