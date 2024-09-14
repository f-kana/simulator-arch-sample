from __future__ import annotations

from src.interfaces.abstract_interface import AbstractXxxRequestInterface, AbstractYyyRequestInterface


class Planner:
    def __init__(
        self,
        xxx_req_if: AbstractXxxRequestInterface,
        yyy_req_if: AbstractYyyRequestInterface,
    ):
        self._xxx_req_if = xxx_req_if
        self._yyy_req_if = yyy_req_if

    def exec_scenario1(self) -> None:
        response = self._xxx_req_if.get()
        print(response.data)
