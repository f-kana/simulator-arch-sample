from __future__ import annotations

from abc import ABCMeta, abstractmethod

from src.dto import BaseResponse, XxxResponse, YyyResponse


class Platform:
    def __init__(self):
        self._xxx_api = XxxApi()
        self._yyy_api = YyyApi()

    @property
    def xxx_api(self) -> XxxApi:
        return self._xxx_api

    @property
    def yyy_api(self) -> YyyApi:
        return self._yyy_api


class Api(metaclass=ABCMeta):
    @abstractmethod
    def get(self) -> BaseResponse:
        pass


class XxxApi(Api):
    def get(self) -> XxxResponse:
        return XxxResponse(status_code=200, data="Hello Xxx World.")


class YyyApi(Api):
    def get(self) -> YyyResponse:
        return YyyResponse(status_code=200, data="Hello Yyy World.")
