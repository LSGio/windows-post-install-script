import configparser


class ConfigProvider:
    Config = None
    CONFIG_FILENAME = "config.ini"

    SECTION_EULA = 'Usage-Terms'
    SECTION_SAFE_MODE = 'Safe-Mode'
    SECTION_TASKS = 'Tasks'

    KEY_ACCEPT_EULA = 'acceptUsageTerms'
    KEY_SAFE_MODE = 'runInSafeMode'

    @staticmethod
    def maybeReadConfigFile() -> None:
        if ConfigProvider.Config is not None:
            return
        else:
            ConfigProvider.Config = configparser.ConfigParser()
            ConfigProvider.Config.read(ConfigProvider.CONFIG_FILENAME)

    @staticmethod
    def getBoolean(section: str, key: str, defaultValue: bool) -> bool:
        ConfigProvider.maybeReadConfigFile()
        return ConfigProvider.Config.getboolean(section, key, fallback=defaultValue)

    @staticmethod
    def getTasksAsString() -> str:
        ConfigProvider.maybeReadConfigFile()
        return ConfigProvider.Config[ConfigProvider.SECTION_TASKS]
