import abc

class AwesomeABC(abc.ABC):

    @abc.abstractmethod
    def must_implement(self, value):    
        pass 

    def concrete_method(self, value):
        return f'Value is: {value}'

class ThisIsAwesome(AwesomeABC):

    def must_implement(self, value):
        return value * 42
    