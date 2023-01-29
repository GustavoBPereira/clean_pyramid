

class ImplementationTokenConsultorGateway:

    def get_tokens(self) -> list:
        with open('tokens.txt', 'r') as file:
            return [token.strip() for token in file.readlines()]
