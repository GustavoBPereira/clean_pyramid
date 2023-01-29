from app.domain.token.gateway import InterfaceTokenConsultorGateway


class InterfaceCheckTokenUseCase:

    def __init__(self, token: str, gateway: InterfaceTokenConsultorGateway):
        raise NotImplementedError()

    def check(self) -> bool:
        raise NotImplementedError()

    def check_length(self) -> bool:
        raise NotImplementedError()

    def check_begin(self) -> bool:
        raise NotImplementedError()

    def check_final(self) -> bool:
        raise NotImplementedError()


class ImplementationCheckTokenUseCase:

    def __init__(self, token: str, gateway: InterfaceTokenConsultorGateway):
        self.token = str(token)
        self.gateway = gateway

    def check(self) -> bool:
        return self.check_length() and self.check_begin() and self.check_final() and self.check_is_registered()

    def check_length(self) -> bool:
        return len(self.token) == 5

    def check_begin(self) -> bool:
        try:
            return self.token[0].isalpha()
        except IndexError:
            return False

    def check_final(self) -> bool:
        try:
            return self.token[4].isdecimal()
        except IndexError:
            return False

    def check_is_registered(self) -> bool:
        return self.token in self.gateway.get_tokens()
