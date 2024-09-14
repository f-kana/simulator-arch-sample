from src.dto import XxxResponse, YyyResponse
from src.interfaces.abstract_interface import AbstractXxxRequestInterface, AbstractYyyRequestInterface


class XxxRequestInterfaceInReal(AbstractXxxRequestInterface):
    def get(self) -> XxxResponse:
        raise NotImplementedError


class YyyRequestInterfaceInReal(AbstractYyyRequestInterface):
    def get(self) -> YyyResponse:
        raise NotImplementedError
