class BusinessException(Exception):
    pass

class NotFoundException(BusinessException):
    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(self.message)

class BadRequestException(BusinessException):
    def __init__(self, message="Bad request"):
        self.message = message
        super().__init__(self.message)
