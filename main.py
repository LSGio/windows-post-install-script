
import InteractionUtils
import Logger
import SystemUtils
import Tasks


if __name__ == '__main__':
    Logger.initLogger()
    Logger.logDisclaimer()
    Logger.logBuildInfo()
    InteractionUtils.exitIfEulaDeclined()
    InteractionUtils.exitIfSafetySwitchIsOn()
    SystemUtils.requestElevatedPermissions()
    InteractionUtils.showConfigToUserBeforeProceeding()

    Tasks.hideCortanaButton()
    Tasks.hideTaskViewButton()
    Tasks.hideSearchBar()
    Tasks.hideNewsAndInterests()
    Tasks.showExtensionsForKnownFiletypes()
    Tasks.openThisPcInsteadOfQuickAccess()
    Tasks.hideRecentFilesInExplorer()
    Tasks.hideFrequentFilesInExplorer()
    Tasks.toggleDeliveryOptimization()
    Tasks.showThisPcDesktopIcon()
    Tasks.showControlPanelDesktopIcon()
    Tasks.showRecycleBinDesktopIcon()
    Tasks.showNetworkDesktopIcon()
    Tasks.showUserFolderDesktopIcon()
    Tasks.disableGameMode()
    Tasks.disableStickyKeys()
