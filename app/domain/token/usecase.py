from app.domain.token.gateway import InterfaceTokenConsultorGateway
from app.domain.token.exceptions import TokenLengthError, TokenBeginError, TokenFinalError, TokenRegisteredError


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
        if len(self.token) == 5:
            return True
        else:
            raise TokenLengthError()


    def check_begin(self) -> bool:
        try:
            if self.token[0].isalpha():
                return True
            else:
                raise TokenBeginError()
        except IndexError:
            return False

    def check_final(self) -> bool:
        try:
            if self.token[4].isdecimal():
                return True
            else:
                raise TokenFinalError()
        except IndexError:
            return False

    def check_is_registered(self) -> bool:
        if self.token in self.gateway.get_tokens():
            return True
        else:
            raise TokenRegisteredError()
