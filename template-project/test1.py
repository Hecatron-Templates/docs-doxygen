'''
An example class for testing doxygen output
'''

class Test1Class(object):

    def __init__(self, param1='param1', param2='param2'):
        self.param1 = param1
        self.param2 = param2

    def test1(self, opts1, opts2=None):
        return "Hello World"

    def test2(self, opts1, opts2=None):
        return "Hello World"

    def test3(self, opts1, opts2=None):
        return "Hello World"
