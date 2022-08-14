from os.path import join
import RegUtils


def hide_cortana_button(hide: bool = True) -> bool:
    root_path = RegUtils.HKCU
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Advanced')
    value_name = 'ShowCortanaButton'
    key_type = RegUtils.DWORD
    if hide:
        new_value = '0'
    else:
        new_value = '1'
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


def hide_task_view_button(hide: bool = True) -> bool:
    root_path = RegUtils.HKCU
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Advanced')
    value_name = 'ShowTaskViewButton'
    key_type = RegUtils.DWORD
    if hide:
        new_value = '0'
    else:
        new_value = '1'
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


def hide_search_bar(hide: bool = True) -> bool:
    root_path = RegUtils.HKCU
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Search')
    value_name = 'SearchboxTaskbarMode'
    key_type = RegUtils.DWORD
    if hide:
        new_value = '0'
    else:
        new_value = '2'
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


def hide_news_and_weather(hide: bool = True) -> bool:
    root_path = RegUtils.HKCU
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Feeds')
    value_name = 'ShellFeedsTaskbarViewMode'
    key_type = RegUtils.DWORD
    if hide:
        new_value = '2'
    else:
        new_value = '0'
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


def show_extensions_for_known_filetypes(show: bool = True) -> bool:
    root_path = RegUtils.HKCU
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Advanced')
    value_name = 'HideFileExt'
    key_type = RegUtils.DWORD
    if show:
        new_value = '0'
    else:
        new_value = '1'
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


def open_this_pc_instead_of_quick_access(toggle: bool = True) -> bool:
    root_path = RegUtils.HKCU
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Advanced')
    value_name = 'LaunchTo'
    key_type = RegUtils.DWORD
    if toggle:
        new_value = '1'
    else:
        new_value = '2'
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


def hide_recent_files_in_explorer(hide: bool = True) -> bool:
    root_path = RegUtils.HKCU
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer')
    value_name = 'ShowRecent'
    key_type = RegUtils.DWORD
    if hide:
        new_value = '0'
    else:
        new_value = '1'
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)


def hide_frequent_files_in_explorer(hide: bool = True) -> bool:
    root_path = RegUtils.HKCU
    key_path = join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer')
    value_name = 'ShowFrequent'
    key_type = RegUtils.DWORD
    if hide:
        new_value = '0'
    else:
        new_value = '1'
    return RegUtils.add_or_update_reg_value(root_path, key_path, value_name, key_type, new_value)
