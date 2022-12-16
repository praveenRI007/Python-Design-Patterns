from ast import Sequence
from ast import BreakEgg
from ast import Expression
from ast import MixEggs
from ast import MeltButter
from ast import CookEggs
from ast import Repetition
from ast import Variable
from ast import Set
from context import Context

def main():
    context = Context()
    context.expression = '''
    break egg; break egg 
    mix in bowl; 
    melt butter in pan; 
    set NOTDONE true;
    while NOTDONE cook eggs; set NOTDONE false
    '''
    context.ast = Expression(
        Sequence([
            BreakEgg(), 
            BreakEgg(),
            MixEggs(),
            MeltButter(),
            Set('NOTDONE', 'true'),
            Repetition(Variable('NOTDONE'), 
                Sequence([CookEggs(), Set('NOTDONE', 'false')]))
            ]))
    context.variables = {}
    context.ast.interpret(context)
    print('Scrambled eggs ready!')
    
if __name__ == '__main__':
    main()
