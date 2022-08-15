from argparse import ArgumentParser


class ArgParser:
    def __init__(self) -> None:
        self.__parser = self.__get_parser()
        self.__args = self.__parser.parse_args()

    @staticmethod
    def __get_parser() -> ArgumentParser:
        parser = ArgumentParser()
        parser.add_argument('--students', required=True, help='path to students file')
        parser.add_argument('--rooms', required=True, help='path to rooms file')
        parser.add_argument('--format', required=True, choices=['xml', 'json'], help='output format')
        return parser

    def get_args(self) -> dict:
        return vars(self.__args)
