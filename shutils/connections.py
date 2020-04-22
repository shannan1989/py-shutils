import pymysql

from .settings import Settings


class MysqlConnection(object):
    __instances = {}

    @classmethod
    def instance(cls, name=''):
        setting = Settings.instance()

        if '' == name:
            name = setting.get('mysql', 'connection')

        if cls.__instances.get(name) is None:
            connection_string = setting.get('connection_strings', name)
            cls.__instances[name] = cls(connection_string)

        return cls.__instances.get(name)

    def __init__(self, connection_string):
        connection = {}
        for item in connection_string.split(';'):
            kv = item.split('=', 1)
            connection[kv[0].strip()] = kv[1].strip()

        self.__con = pymysql.connect(
            host=connection['host'],
            user=connection['user'],
            password=connection['password'])
        if connection.get('db') is not None:
            self.__con.select_db(connection['db'])
        if connection.get('charset') is not None:
            self.__con.set_charset(connection['charset'])
        self.__con.autocommit(True)

        self.__cursor = self.__con.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__con:
            self.__con.close()

    def execute(self, query, *args):
        self.__cursor.execute(query, args)
        return self.__cursor.rowcount

    def queryAll(self, query, *args):
        self.__cursor.execute(query, args)
        return self.__cursor.fetchall()

    def queryOne(self, query, *args):
        self.__cursor.execute(query, args)
        return self.__cursor.fetchone()
