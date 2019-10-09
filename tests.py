import unittest

class Test(unittest.TestCase):
    ''' Test case to see if the scripts run when called as standalone.
    '''
    def test_bin():
        ''' Tests scripts in the bin folder.
        '''
        pass

    def test_plugins():
        ''' Test scripts in the plugins folder.
        '''
        pass
    
    def test_py3_compatability(filename):
        ''' Tests a scripts physical compatability with Python 3.
        '''
        import ast
        f = open(filename).read()
        try:
            ast.parset(f)
        except SyntaxError:
            return False

if __name__ == '__main__':
    unittest.main()
