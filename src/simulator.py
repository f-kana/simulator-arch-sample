from src.fj_platform import Platform
from src.interfaces.interfaces_in_simulator import XxxRequestInterfaceInSimulator, YyyRequestInterfaceInSimulator
from src.planner import Planner


class Simulator:
    _platform: Platform
    _planner: Planner

    def __init__(self):
        self._platform = Platform()

        self._planner = Planner(
            XxxRequestInterfaceInSimulator(self._platform),
            YyyRequestInterfaceInSimulator(self._platform),
        )

    def exec(self) -> None:
        self._planner.exec_scenario1()
