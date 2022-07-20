'''
An example class for testing doxygen output
'''

class Test1Class(object):
    '''Test Class

    Attributes:
        param1: Storage of the first parameter.
        param2: Storage of the second parameter.
    '''

    def __init__(self, param1='param1', param2='param2'):
        '''Class initialiser.
        Args:
            param1: First parameter.
            param2: Second parameter.
        '''
        self.param1 = param1
        self.param2 = param2

    def test1(self, opts1, opts2=None):
        '''Test function 1
        Args:
            opts1: First set of options.
            opts2: Second set of options.
        Returns:
            Text string "Hello World".
        '''
        return "Hello World"

    def test2(self, opts1, opts2=None):
        '''Test function 2
        Args:
            opts1: First set of options.
            opts2: Second set of options.
        Returns:
            Text string "Hello World".
        '''
        return "Hello World"

    def test3(self, opts1, opts2=None):
        '''Test function 3
        Args:
            opts1: First set of options.
            opts2: Second set of options.
        Returns:
            Text string "Hello World".
        '''
        return "Hello World"
