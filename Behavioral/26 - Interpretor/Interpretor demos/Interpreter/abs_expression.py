import abc

class AbsExpression(abc.ABC):
    @abc.abstractmethod
    def interpret(context):
        pass
