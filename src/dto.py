from dataclasses import dataclass


@dataclass
class BaseResponse:
    status_code: int


@dataclass
class XxxResponse(BaseResponse):
    data: str


@dataclass
class YyyResponse(BaseResponse):
    data: str
