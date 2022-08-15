from arg_parser import ArgParser
from yaml_reader import YamlReader
from serializers.json_serializer import JsonSerializer
from serializers.xml_serializer import XmlSerializer
from db.initializer import DBInitializer
from db.selecter import DBSelecter
from file_writer import FileWriter


def main():
    arg_parser = ArgParser()
    args = arg_parser.get_args()

    yaml_reader = YamlReader()
    database_config = yaml_reader.get_config('configs/database_config.yaml')
    path_config = yaml_reader.get_config('configs/path_config.yaml')

    serializer = JsonSerializer()
    rooms = serializer.deserialize(args['rooms'])
    students = serializer.deserialize(args['students'])

    DBInitializer(database_config['database'], path_config['database_path'])(rooms, students)
    if args['format'] == 'xml':
        serializer = XmlSerializer()

    selecter = DBSelecter(database_config['database'], path_config['database_path']['selects'])
    selects = {
        'rooms_with_student_count': selecter.select('select_rooms_with_student_count.sql'),
        'top_5_rooms_with_min_avg_age': selecter.select('select_top_5_rooms_with_min_avg_age.sql'),
        'top_5_rooms_with_max_diff_age': selecter.select('select_top_5_rooms_with_max_diff_age.sql'),
        'rooms_with_diff_sex': selecter.select('select_rooms_with_diff_sex.sql')
    }

    writer = FileWriter()
    for key, value in selects.items():
        serialized = serializer.serialize(value)
        writer.write_file(serialized, f"{path_config['result_path']}{key}.{args['format']}")


if __name__ == '__main__':
    main()
