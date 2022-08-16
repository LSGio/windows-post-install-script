from os.path import join

import RegUtils
from TaskRunner import runnable_task


@runnable_task
def hide_cortana_button(hide: bool = True) -> bool:
    """
    Hide Cortana button in taskbar.

    :param: bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Advanced')
    value_name = 'ShowCortanaButton'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 1
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


@runnable_task
def hide_task_view_button(hide: bool = True) -> bool:
    """
    Hide Task View button in taskbar.

    :param: bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Advanced')
    value_name = 'ShowTaskViewButton'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 1
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


@runnable_task
def hide_search_bar(hide: bool = True) -> bool:
    """
    Hide Search from taskbar.

    :param: bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Search')
    value_name = 'SearchboxTaskbarMode'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 2
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


@runnable_task
def hide_news_and_weather(hide: bool = True) -> bool:
    """
    Hide News and interests button in taskbar.

    :param: bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Feeds')
    value_name = 'ShellFeedsTaskbarViewMode'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 2 if hide else 0
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


@runnable_task
def show_extensions_for_known_filetypes(show: bool = True) -> bool:
    """
    Show file extensions for known filetypes.

    :param: bool show: True to show, False to hide.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Advanced')
    value_name = 'HideFileExt'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if show else 1
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


@runnable_task
def open_this_pc_instead_of_quick_access(toggle: bool = True) -> bool:
    """
    Open This PC instead of Quick access when opening a new explorer window.

    :param: bool toggle: True to open This PC, False to open Quick access.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Advanced')
    value_name = 'LaunchTo'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 1 if toggle else 2
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


@runnable_task
def hide_recent_files_in_explorer(hide: bool = True) -> bool:
    """
    Hide recently used files in Quick access.

    :param: bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer')
    value_name = 'ShowRecent'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 1
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


@runnable_task
def hide_frequent_files_in_explorer(hide: bool = True) -> bool:
    """
    Hide frequently used folders in Quick access.

    :param: bool hide: True to hide, False to show.
    :rtype: bool
    :return: True if operation was successful, False otherwise.
    """

    root_path = RegUtils.Consts.HKEY_CURRENT_USER
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer')
    value_name = 'ShowFrequent'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 0 if hide else 1
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


@runnable_task
def toggle_delivery_optimization(toggle: bool = False) -> bool:
    """
        Enable or disable Delivery Optimization

        :param: bool toggle: True to enable, False to disable.
        :rtype: bool
        :return: True if operation was successful, False otherwise.
        """

    root_path = RegUtils.Consts.HKEY_LOCAL_MACHINE
    key_path = join('SYSTEM', 'CurrentControlSet', 'Services', 'DoSvc')
    value_name = 'ShowFrequent'
    key_type = RegUtils.Consts.REG_DWORD
    new_value = 2 if toggle else 4
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)
