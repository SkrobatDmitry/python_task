import sys

from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from serializers.serializer import Serializer


class XmlSerializer(Serializer):
    def serialize(self, data: list) -> str:
        try:
            xml_data = dicttoxml(data)
            dom = parseString(xml_data)
            return dom.toprettyxml()
        except Exception as e:
            print(e.with_traceback, file=sys.stderr)
            raise SystemExit

    def deserialize(self, path: str):
        pass
