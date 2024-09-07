from src.interfaces import AbstractInterface
class Planner:
    def __init__(self, interface: AbstractInterface):
        self._interface = interface
    
    def exec_scenario1(self) -> None:
        response = self._interface.get_xxx_data()
        print(response.data)