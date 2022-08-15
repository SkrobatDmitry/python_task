import sys


class FileWriter:
    @staticmethod
    def write_file(data: str, path: str) -> None:
        try:
            with open(path, 'w') as file:
                file.write(data)
        except Exception as e:
            print(e.with_traceback, file=sys.stderr)
            raise SystemExit
