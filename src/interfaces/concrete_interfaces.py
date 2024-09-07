from src.interfaces.abstract_interface import AbstractInterface
from src.dto import XxxDataResponse
from src.fj_platform import PlatformXxxApi

class InterfaceToPlatformInSimulator(AbstractInterface):
    def __init__(self):
        super().__init__()

    def get_xxx_data(self) -> XxxDataResponse:
        pf_api = PlatformXxxApi()
        return pf_api.get()
        


class InterfaceToPlatformInReal(AbstractInterface):
    def __init__(self):
        super().__init__()

    def get_xxx_data(self) -> XxxDataResponse:
        return XxxDataResponse("response in real")