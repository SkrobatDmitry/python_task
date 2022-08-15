from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize(self, data: list):
        pass

    @abstractmethod
    def deserialize(self, path: str):
        pass
