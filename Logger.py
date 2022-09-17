
import logging
import Globals
import SystemUtils


def initLogger() -> None:
    """
    Initialize the root logger
    """
    logFormat = '%(asctime)s :: %(levelname)s :: %(message)s'
    dateFormat = '%d/%m/%Y %H:%M:%S'
    logLevel = logging.DEBUG if Globals.Build.isDebug else logging.INFO
    logging.basicConfig(format=logFormat, level=logLevel, datefmt=dateFormat)


def logDisclaimer() -> None:
    """
    Print the readme file
    """

    with open('README.md') as readmeFile:
        rawReadme = readmeFile.read()
        print(rawReadme)


def logD(message: str) -> None:
    """
    Print a log message on Debug build-types, with current date and time info.

    Parameters:
    str message : The message to be printed
    """

    logging.debug(message)


def logI(message: str) -> None:
    """
    Print a log message on every Build-type, with current date and time info.

    Parameters:
    str message : The message to be printed
    """

    logging.info(message)


def logBuildInfo() -> None:
    """
    Print system and script info.
    """

    logI(Globals.Build.appTitle)
    logI(f'Script running in debug mode : {Globals.Build.isDebug}')
    logI(f'Script version : {Globals.Build.versionString}')
    logI(f'Detected OS : {SystemUtils.getOsInfo()}')
    logI(f'OS Build Number : {SystemUtils.getOsBuildNumber()}')
