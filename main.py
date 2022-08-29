import InteractionUtils
import Logger
from Tasks import *


if __name__ == '__main__':

    Logger.logDisclaimer()
    Logger.logBuildInfo()
    InteractionUtils.checkEulaStatus()
    InteractionUtils.checkSafetySwitchStatus()

    hideCortanaButton()
    hideTaskViewButton()
    hideSearchBar()
    hideNewsAndInterests()
    showExtensionsForKnownFiletypes()
    openThisPcInsteadOfQuickAccess()
    hideRecentFilesInExplorer()
    hideFrequentFilesInExplorer()
    toggleDeliveryOptimization()
    showThisPcDesktopIcon()
    showControlPanelDesktopIcon()
    showRecycleBinDesktopIcon()
    showNetworkDesktopIcon()
    showUserFolderDesktopIcon()
    disableGameMode()
    disableStickyKeys()