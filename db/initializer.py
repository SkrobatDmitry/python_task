import sys

from db.connector import DBConnector
from mixins.file_reader_mixin import FileReaderMixin


class DBInitializer(DBConnector, FileReaderMixin):
    def __init__(self, database: dict, path: dict) -> None:
        super().__init__(database)
        self.__path = path

    def __call__(self, rooms: dict, students: dict) -> None:
        self.__create_tables()
        self.__create_indexes()
        self.__insert_rooms_table(rooms)
        self.__insert_students_table(students)

    def __create_tables(self) -> None:
        try:
            path = self.__path['tables']
            with self._conn.cursor() as cursor:
                cursor.execute(self._get_file(path + 'drop_students_table.sql'))
                cursor.execute(self._get_file(path + 'drop_rooms_table.sql'))
                cursor.execute(self._get_file(path + 'create_rooms_table.sql'))
                cursor.execute(self._get_file(path + 'create_students_table.sql'))
            self._conn.commit()
        except Exception as e:
            print(e, file=sys.stderr)
            raise SystemExit

    def __create_indexes(self) -> None:
        try:
            path = self.__path['indexes']
            with self._conn.cursor() as cursor:
                cursor.execute(self._get_file(path + 'create_students_room_ind.sql'))
                cursor.execute(self._get_file(path + 'create_students_sex_ind.sql'))
            self._conn.commit()
        except Exception as e:
            print(e, file=sys.stderr)
            raise SystemExit

    def __insert_rooms_table(self, rooms: dict) -> None:
        try:
            query = self._get_file(self.__path['inserts'] + 'insert_rooms.sql')
            with self._conn.cursor() as cursor:
                for room in rooms:
                    cursor.execute(query.format(room['id'], room['name']))
            self._conn.commit()
        except Exception as e:
            print(e, file=sys.stderr)
            raise SystemExit

    def __insert_students_table(self, students: dict) -> None:
        try:
            query = self._get_file(self.__path['inserts'] + 'insert_students.sql')
            with self._conn.cursor() as cursor:
                for student in students:
                    cursor.execute(query.format(
                        student['id'], student['name'], student['room'], student['sex'], student['birthday']
                    ))
            self._conn.commit()
        except Exception as e:
            print(e, file=sys.stderr)
            raise SystemExit
