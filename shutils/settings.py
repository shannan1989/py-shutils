import configparser
import os
import sys


class Settings(object):
    __instance = None

    @classmethod
    def instance(cls, *args, **kwargs):
        if(cls.__instance is None):
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.__settings = configparser.ConfigParser()
        self.__load()

    def __load(self):
        files = []
        path = os.path.dirname(os.path.realpath(sys.argv[0]))
        while True:
            files.append(os.path.join(path, 'config.ini'))
            if path == os.path.dirname(path):
                break
            path = os.path.dirname(path)

        config = configparser.ConfigParser()
        files.reverse()
        for i in range(len(files)):
            if os.path.exists(files[i]) == False:
                continue
            config.read(files[i])
            for section in config.sections():
                if self.__settings.has_section(section) == False:
                    self.__settings.add_section(section)
                for option in config.options(section):
                    value = config.get(section, option)
                    self.__settings.set(section, option, value)

    def get(self, section, option):
        return self.__settings.get(section, option)
