from TaskRunner import runnableTask
import Globals
import RegUtils


"""
All functions in this file can be called directly from main.py to produce your own custom script
For now, all the functions simply change registry values to achieve their goal,
and all functions return either True or False based on their success.
"""


@runnableTask
def hideCortanaButton(hide: bool = True) -> bool:
    """
    Hide Cortana button in taskbar.
    [True] to hide, False to show.
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
    [True] to hide, False to show.
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
    [True] to hide, False to show.
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
    [True] to hide, False to show.
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
    [True] to show, False to hide.
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
    [True] to open This PC, False to open Quick access.
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
    [True] to hide, False to show.
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
    [True] to hide, False to show.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_SHOW_FREQUENT_FILES_IN_EXPLORER
    value_name = Globals.RegValueNames.VALUENAME_SHOW_FREQUENT_FILES_IN_EXPLORER
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def toggleDeliveryOptimization(toggle: bool = True) -> bool:
    """
    Enable or disable Delivery Optimization service.
    True to enable, [False] to disable.
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
    [True] to show, False to hide.
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
    [True] to show, False to hide.
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
    [True] to show, False to hide.
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
    [True] to show, False to hide.
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
    [True] to show, False to hide.
    """

    root_path = RegUtils.Consts.HKEY_LOCAL_MACHINE
    key_path = Globals.RegKeys.KEY_HIDE_DESKTOP_ICONS
    value_name = Globals.RegValueNames.VALUENAME_HIDE_USERS_FILES_ICON
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if show else 1
    return RegUtils.addOrUpdateRegValue(root_path, key_path, value_name, key_type, new_value)


@runnableTask
def disableGameMode(disable: bool = True) -> bool:
    """
    Enable or disable Game Mode that was introduced in build 1703 of Windows 10.
    [True] to disable, False to enable.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = Globals.RegKeys.KEY_TOGGLE_GAME_MODE
    value_name_1 = Globals.RegValueNames.VALUENAME_TOGGLE_GAME_MODE_1
    value_name_2 = Globals.RegValueNames.VALUENAME_TOGGLE_GAME_MODE_2
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if disable else 1
    res_1 = RegUtils.addOrUpdateRegValue(root_path, key_path, value_name_1, key_type, new_value)
    res_2 = RegUtils.addOrUpdateRegValue(root_path, key_path, value_name_2, key_type, new_value)
    return res_1 and res_2


@runnableTask
def disableStickyKeys(disable: bool = True) -> bool:
    """
    Enable or disable Sticky Keys
    Note: when enabled, user still must use the keyboard shortcut to activate the feature.
    [True] to disable, False to enable.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path_1 = Globals.RegKeys.KEY_TOGGLE_STICKY_KEYS_1
    key_path_2 = Globals.RegKeys.KEY_TOGGLE_STICKY_KEYS_2
    key_path_3 = Globals.RegKeys.KEY_TOGGLE_STICKY_KEYS_3
    value_name = Globals.RegValueNames.VALUENAME_TOGGLE_STICKY_KEYS
    key_type = RegUtils.Consts.REG_SZ
    new_value_1 = "506" if disable else "510"
    new_value_2 = "58" if disable else "62"
    new_value_3 = "122" if disable else "126"
    res_1 = RegUtils.addOrUpdateRegValue(root_path, key_path_1, value_name, key_type, new_value_1)
    res_2 = RegUtils.addOrUpdateRegValue(root_path, key_path_2, value_name, key_type, new_value_2)
    res_3 = RegUtils.addOrUpdateRegValue(root_path, key_path_3, value_name, key_type, new_value_3)
    return res_1 and res_2 and res_3
