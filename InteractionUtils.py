import sys

import Globals
import Logger
from ConfigProvider import ConfigProvider


def exitIfEulaDeclined() -> None:
    Logger.logD(Globals.UserPrompts.PROMPT_EULA_CHECK)
    eulaValue = ConfigProvider.getBoolean(ConfigProvider.SECTION_EULA, ConfigProvider.KEY_ACCEPT_EULA, False)
    if eulaValue:
        Logger.logI(Globals.UserPrompts.PROMPT_EULA_ACCEPTED)
        return
    else:
        Logger.logI(Globals.UserPrompts.PROMPT_EULA_NOT_ACCEPTED)
        sys.exit()


def exitIfSafetySwitchIsOn() -> None:
    Logger.logD(Globals.UserPrompts.PROMPT_SAFE_MODE_CHECK)
    safeModeValue = ConfigProvider.getBoolean(ConfigProvider.SECTION_SAFE_MODE, ConfigProvider.KEY_SAFE_MODE, True)
    if not safeModeValue:
        Logger.logI(Globals.UserPrompts.PROMPT_SAFETY_SWITCH_DISABLED)
        return
    else:
        Logger.logI(Globals.UserPrompts.PROMPT_SAFETY_SWITCH_ENABLED)
        sys.exit()


def showConfigToUserBeforeProceeding() -> None:
    Logger.logI(Globals.UserPrompts.PROMPT_CONFIG_BEFORE_APPLYING)
    Logger.logI(ConfigProvider.getTasksAsString())
    input(Globals.UserPrompts.PROMPT_PRESS_ANY_KEY)
