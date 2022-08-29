import configparser

import Globals


def maybeReadConfigFile(filename) -> None:
    if Globals.Config.config is None:
        Globals.Config.config = configparser.ConfigParser()
        Globals.Config.config.read(filename)


def getBoolean(section: str, key: str) -> bool:
    maybeReadConfigFile(Globals.Config.configFilename)
    return Globals.Config.config.getboolean(section, key)


