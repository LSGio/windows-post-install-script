import ConfigProvider
import Logger
import Globals


def exitIfEulaDeclined() -> None:
    Logger.logD(Globals.UserPrompts.PROMPT_EULA_CHECK)
    eulaValue = ConfigProvider.getBoolean(Globals.Config.SECTION_EULA, Globals.Config.KEY_ACCEPT_EULA)
    if eulaValue:
        Logger.logI(Globals.UserPrompts.PROMPT_EULA_ACCEPTED)
        return
    else:
        Logger.logI(Globals.UserPrompts.PROMPT_EULA_NOT_ACCEPTED)
        exit(0)


def exitIfSafetySwitchIsOn() -> None:
    Logger.logD(Globals.UserPrompts.PROMPT_SAFE_MODE_CHECK)
    safeModeValue = ConfigProvider.getBoolean(Globals.Config.SECTION_SAFE_MODE, Globals.Config.KEY_SAFE_MODE)
    if not safeModeValue:
        Logger.logI(Globals.UserPrompts.PROMPT_SAFETY_SWITCH_DISABLED)
        return
    else:
        Logger.logI(Globals.UserPrompts.PROMPT_SAFETY_SWITCH_ENABLED)
        exit(0)
