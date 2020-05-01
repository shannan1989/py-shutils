import configparser
import os
import sys


class Settings(configparser.ConfigParser):
    __instance = None

    @classmethod
    def instance(cls, *args, **kwargs):
        if(cls.__instance is None):
            cls.__instance = cls(*args, **kwargs)
            cls.__instance.__load()
        return cls.__instance

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
        self.read(files)
