import configparser
import Logger
import Globals


def checkEulaStatus() -> None:
    Logger.logI(Globals.UserPrompts.PROMPT_EULA_CHECK)
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'Usage-Terms' in config.sections():
        if 'acceptUsageTerms' in config['Usage-Terms']:
            value = config['Usage-Terms']['acceptUsageTerms']
            if value == 'True':
                Logger.logI(Globals.UserPrompts.PROMPT_EULA_ACCEPTED)
            elif value == 'False':
                Logger.logI(Globals.UserPrompts.PROMPT_EULA_NOT_ACCEPTED)
            else:
                # value is neither true nor false
                # show appropriate message and exit
                exit(0)


def checkSafetySwitchStatus() -> None:
    Logger.logI(Globals.UserPrompts.PROMPT_MASTER_SWITCH_CHECK)
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'Master-Switch' in config.sections():
        if 'doNothing' in config['Master-Switch']:
            value = config['Master-Switch']['doNothing']
            if value == 'True':
                Logger.logI(Globals.UserPrompts.PROMPT_MASTER_SWITCH_ENABLED)
            elif value == 'False':
                Logger.logI(Globals.UserPrompts.PROMPT_MASTER_SWITCH_DISABLED)
            else:
                # value is neither true nor false
                # show appropriate message and exit
                exit(0)
