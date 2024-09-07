from src.dto import XxxDataResponse

class Platform:
    pass


class PlatformXxxApi:
    def get(self) -> XxxDataResponse:
        return XxxDataResponse("response from platform")
    
    def post(self) -> None:
        raise NotImplementedError("Not implemented yet")
