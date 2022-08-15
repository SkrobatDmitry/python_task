import sys

from db.connector import DBConnector
from mixins.file_reader_mixin import FileReaderMixin


class DBSelecter(DBConnector, FileReaderMixin):
    def __init__(self, database: dict, path: str) -> None:
        super().__init__(database)
        self.__path = path

    def select(self, query: str) -> list:
        try:
            with self._conn.cursor() as cursor:
                cursor.execute(self._get_file(self.__path + query))
                records = cursor.fetchall()

                column_names = [column[0] for column in cursor.description]
                return [dict(zip(column_names, record)) for record in records]
        except Exception as e:
            print(e, file=sys.stderr)
            raise SystemExit
