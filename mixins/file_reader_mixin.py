import os
import sys


class FileReaderMixin:
    @staticmethod
    def _get_file(path: str) -> str:
        try:
            path = os.path.abspath(os.path.dirname(__name__)) + '/' + path
            with open(path, 'r') as file:
                return file.read()
        except Exception as e:
            print(e.with_traceback, file=sys.stderr)
            raise SystemExit
