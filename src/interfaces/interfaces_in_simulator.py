from abc import ABCMeta

from src.dto import BaseResponse, XxxResponse, YyyResponse
from src.fj_platform import Platform
from src.interfaces.abstract_interface import AbstractXxxRequestInterface, AbstractYyyRequestInterface


class _AbstractInterfaceInSimulator(metaclass=ABCMeta):
    def __init__(self, platform: Platform) -> None:
        self._platform = platform


class XxxRequestInterfaceInSimulator(_AbstractInterfaceInSimulator, AbstractXxxRequestInterface):
    def get(self) -> XxxResponse:
        return self._platform.xxx_api.get()

    def post(self) -> BaseResponse:
        raise NotImplementedError


class YyyRequestInterfaceInSimulator(_AbstractInterfaceInSimulator, AbstractYyyRequestInterface):
    def get(self) -> YyyResponse:
        return self._platform.yyy_api.get()

    def post(self) -> BaseResponse:
        raise NotImplementedError
