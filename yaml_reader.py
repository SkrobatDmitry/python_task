import os
import sys
import yaml


class YamlReader:
    @staticmethod
    def get_config(path: str) -> dict:
        try:
            path = os.path.abspath(os.path.dirname(__name__)) + '/' + path
            with open(path) as config_file:
                config = yaml.safe_load(config_file)
                return config
        except Exception as e:
            print(e.with_traceback, file=sys.stderr)
            raise SystemExit
