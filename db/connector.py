import sys

from mysql.connector import MySQLConnection


class DBConnector:
    def __init__(self, database: dict) -> None:
        self._conn = self.__get_conn(database)

    @staticmethod
    def __get_conn(database: dict) -> MySQLConnection:
        try:
            conn = MySQLConnection(**database)
            return conn
        except Exception as e:
            print(e, file=sys.stderr)
            raise SystemExit
