from src.interfaces.abstract_interface import AbstractInterface
from enum import IntEnum
from src.interfaces.concrete_interfaces import InterfaceToPlatformInSimulator, InterfaceToPlatformInReal


class InterfaceType(IntEnum):
    SIMULATOR = 1
    REAL = 2

class InterfaceFactory:
    @staticmethod
    def create_interface(if_type: InterfaceType) -> AbstractInterface:
        if if_type == InterfaceType.SIMULATOR:
            return InterfaceToPlatformInSimulator()
        elif if_type == InterfaceType.REAL:
            return InterfaceToPlatformInReal()
        else:
            raise ValueError("Invalid interface type")