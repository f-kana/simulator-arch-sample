from abc import ABCMeta, abstractmethod

from src.dto import BaseResponse, XxxResponse, YyyResponse


class AbstractRequestInterface(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get(self) -> BaseResponse:
        pass

    @abstractmethod
    def post(self) -> BaseResponse:
        pass


class AbstractXxxRequestInterface(AbstractRequestInterface):
    @abstractmethod
    def get(self) -> XxxResponse:
        pass


class AbstractYyyRequestInterface(AbstractRequestInterface):
    @abstractmethod
    def get(self) -> YyyResponse:
        pass
