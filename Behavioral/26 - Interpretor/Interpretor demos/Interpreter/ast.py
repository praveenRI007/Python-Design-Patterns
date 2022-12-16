from abs_expression import AbsExpression
import time

class Expression(AbsExpression):
    def __init__(self, expression):
        self._expression = expression

    def interpret(self, context):
        self._expression.interpret(context)

class BreakEgg(AbsExpression):
    def interpret(self, context):
        print('Breaking an egg.')

class MixEggs(AbsExpression):
    def interpret(self, context):
        print('Mixing eggs in a bowl.')

class MeltButter(AbsExpression):
    def interpret(self, context):
        print('Melting butter in pan.')

class CookEggs(AbsExpression):
    def interpret(self, context):
        print('Cooking the eggs.')
        time.sleep(1)

class Sequence(AbsExpression):
    def __init__(self, sequence):
        self._sequence = sequence

    def interpret(self, context):
        for e in self._sequence:
            e.interpret(context)

class Repetition(AbsExpression):
    def __init__(self, variable, expression):
        self._variable = variable
        self._expression = expression

    def interpret(self, context):
        while self._variable.interpret(context) == 'true':
            self._expression.interpret(context)

class Variable(AbsExpression):
    def __init__(self, variable):
        self._variable = variable

    def interpret(self, context):
        return context.variables.get(self._variable, None)

class Set(AbsExpression):
    def __init__(self, variable, value):
        self._variable = variable
        self._value = value
    
    def interpret(self, context):
        context.variables[self._variable] = self._value
