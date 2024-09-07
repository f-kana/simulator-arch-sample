from src.fj_platform import Platform
from src.planner import Planner
from src.interfaces import AbstractInterface

class Simulator:
    _platform: Platform
    _planner: Planner

    def __init__(self):
        raise NotImplementedError("DO NOT Create an instance of this class. Use class methods.")
    
    @classmethod
    def initialize_class(cls):
        pass
        # cls._platform = Platform()
        # cls._planner = Planner()
    
    @classmethod
    def initialize_platform(cls):
        cls._platform = Platform()
    
    @classmethod
    def initialize_planner(cls, interface: AbstractInterface):
        cls._planner = Planner(interface)
    
    @classmethod
    def exec(cls):
        cls._planner.exec_scenario1()
    
    @classmethod
    def get_platform_singleton_instance(cls) -> Platform:
        return cls._platform
    
    @classmethod
    def get_planner_singleton_instance(cls) -> Planner:
        return cls._planner