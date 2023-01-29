from pytest import raises

from app.domain.token.usecase import ImplementationCheckTokenUseCase
from app.infra.in_memory.token.gateway import ImplementationTokenConsultorGateway
from app.domain.token.exceptions import TokenLengthError, TokenBeginError, TokenFinalError, TokenRegisteredError


def test_correct_token():
    token = ImplementationCheckTokenUseCase('axxx1', ImplementationTokenConsultorGateway())
    assert token.check() is True


def test_length_error():
    token = ImplementationCheckTokenUseCase('axxzzzx1', ImplementationTokenConsultorGateway())
    with raises(TokenLengthError):
        token.check()


def test_begin_error():
    token = ImplementationCheckTokenUseCase('0xxx1', ImplementationTokenConsultorGateway())
    with raises(TokenBeginError):
        token.check()


def test_final_error():
    token = ImplementationCheckTokenUseCase('axxxy', ImplementationTokenConsultorGateway())
    with raises(TokenFinalError):
        token.check()


def test_registered_error():
    token = ImplementationCheckTokenUseCase('xxxx9', ImplementationTokenConsultorGateway())
    with raises(TokenRegisteredError):
        token.check()
