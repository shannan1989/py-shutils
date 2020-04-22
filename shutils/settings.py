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
            if os.path.exists(os.path.join(path, 'config.ini')):
                files.append(os.path.join(path, 'config.ini'))
            if path == os.path.dirname(path):
                break
            path = os.path.dirname(path)
        files.reverse()
        self.__settings.read(files)

    def get(self, section, option, **kwargs):
        return self.__settings.get(section, option, **kwargs)
