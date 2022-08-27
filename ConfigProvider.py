import configparser

import Globals


def maybeReadConfigFile(filename) -> None:
    if Globals.Config.config is None:
        Globals.Config.config = configparser.ConfigParser()
        Globals.Config.config.read(filename)

def getConfigValue(section: str, key: str) -> str:
    pass