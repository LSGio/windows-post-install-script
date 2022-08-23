

class Build:

    appTitle = "Windows post install script"
    isDebug = True
    versionNumber = 106
    versionString = "1.0.6"


class WindowsBuilds:

    WINDOWS_11_INITAL_BUILD_NUMBER = 22000
    WINDOWS_10_INITIAL_BUILD_NUMBER = 10240


class RegKeys:

    # OS info
    KEY_OS_INFO = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion'

    # Desktop Icons
    KEY_HIDE_DESKTOP_ICONS = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\HideDesktopIcons\\NewStartPanel'

    # Taskbar
    KEY_SHOW_CORTANA_BUTTON = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced'
    KEY_SHOW_TASK_VIEW_BUTTON = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced'
    KEY_SEARCHBAR_VIEW_MODE = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Search'
    KEY_NEWS_AND_INTERESTS_VIEW_MODE = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Feeds'
    KEY_OPEN_THIS_PC_OR_QUICK_ACCESS = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced'

    # Explorer
    KEY_HIDE_FILE_EXTENSIONS = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced'
    KEY_SHOW_RECENT_FILES_IN_EXPLORER = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer'
    KEY_SHOW_FREQUENT_FILES_IN_EXPLORER = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer'

    # System-wide settings
    KEY_TOGGLE_DELIVERY_OPTIMIZATION = 'SYSTEM\\CurrentControlSet\\Services\\DoSvc'
    KEY_TOGGLE_GAME_MODE = 'SOFTWARE\\Microsoft\\GameBar'
    KEY_TOGGLE_STICKY_KEYS_1 = 'Control Panel\\Accessibility\\StickyKeys'
    KEY_TOGGLE_STICKY_KEYS_2 = 'Control Panel\\Accessibility\\ToggleKeys'
    KEY_TOGGLE_STICKY_KEYS_3 = 'Control Panel\\Accessibility\\Keyboard Response'


class RegValueNames:

    # OS info
    VALUENAME_OS_PRODUCT_NAME = 'ProductName'
    VALUENAME_OS_BUILD_NUMBER = 'CurrentBuildNumber'
    VALUENAME_OS_EDITION = 'EditionID'

    # Desktop Icons
    VALUENAME_HIDE_THIS_PC_ICON = '{20D04FE0-3AEA-1069-A2D8-08002B30309D}'
    VALUENAME_HIDE_USERS_FILES_ICON = '{59031a47-3f72-44a7-89c5-5595fe6b30ee}'
    VALUENAME_HIDE_NETWORK_ICON = '{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}'
    VALUENAME_HIDE_CONTROL_PANEL_ICON = '{5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0}'
    VALUENAME_HIDE_RECYCLE_BIN_ICON = '{645FF040-5081-101B-9F08-00AA002F954E}'

    # Taskbar
    VALUENAME_SHOW_CORTANA_BUTTON = 'ShowCortanaButton'
    VALUENAME_SHOW_TASK_VIEW_BUTTON = 'ShowTaskViewButton'
    VALUENAME_SEARCHBAR_VIEW_MODE = 'SearchboxTaskbarMode'
    VALUENAME_NEWS_AND_INTERESTS_VIEW_MODE = 'ShellFeedsTaskbarViewMode'
    VALUENAME_OPEN_THIS_PC_OR_QUICK_ACCESS = 'LaunchTo'

    # Explorer
    VALUENAME_HIDE_FILE_EXTENSIONS = 'HideFileExt'
    VALUENAME_SHOW_RECENT_FILES_IN_EXPLORER = 'ShowRecent'
    VALUENAME_SHOW_FREQUENT_FILES_IN_EXPLORER = 'ShowFrequent'

    # System-wide settings
    VALUENAME_TOGGLE_DELIVERY_OPTIMIZATION = 'Start'
    VALUENAME_TOGGLE_GAME_MODE_1 = 'AllowAutoGameMode'
    VALUENAME_TOGGLE_GAME_MODE_2 = 'AutoGameModeEnabled'
    VALUENAME_TOGGLE_STICKY_KEYS = 'Flags'
