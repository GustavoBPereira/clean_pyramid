class TokenValidatorException(Exception):
    pass


class TokenLengthError(TokenValidatorException):
    pass


class TokenBeginError(TokenValidatorException):
    pass


class TokenFinalError(TokenValidatorException):
    pass


class TokenRegisteredError(TokenValidatorException):
    pass
