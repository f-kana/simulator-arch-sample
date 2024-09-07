from src.interfaces import AbstractInterface, InterfaceFactory, InterfaceType
from src.simulator import Simulator

def main():
    Simulator.initialize_class()
    interface: AbstractInterface = InterfaceFactory.create_interface(InterfaceType.SIMULATOR)
    Simulator.initialize_platform()
    Simulator.initialize_planner(interface)
    Simulator.exec()


if __name__ == "__main__":
    main()