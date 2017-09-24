class EthereumError(Exception):
    pass


class BadResponseError(EthereumError):

    def __init__(self, msg, code, *args, **kwargs):
        super().__init__(msg, code, *args, **kwargs)
        self.msg = msg
        self.code = code


class BadStatusError(EthereumError):
    pass


class BadJsonError(EthereumError):
    pass
