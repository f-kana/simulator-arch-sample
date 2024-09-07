from abc import ABCMeta, abstractmethod
from src.dto import XxxDataResponse



class AbstractInterface(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_xxx_data(self) -> XxxDataResponse:
        pass


