import unittest

class Test(unittest.TestCase):
    ''' Test case to see if the scripts run when called as standalone.
    '''
    def test_bin(self):
        ''' Tests scripts in the bin folder.
        '''
        pass

    def test_plugins(self):
        ''' Test scripts in the plugins folder.
        '''
        pass
    
    def test_py3_compatability(self):
        ''' Tests a scripts physical compatability with Python 3.
        '''
        import ast, glob
        import fnmatch
        import os

        matches = []
        for root, dirnames, filenames in os.walk('long_baseline_pipeline'):
            for filename in fnmatch.filter(filenames, '*.py'):
                matches.append(os.path.join(root, filename))
        for filename in matches:
            with open(filename) as f:
                contents = f.read()
                try:
                    ast.parse(contents)
                except SyntaxError:
                    return False

if __name__ == '__main__':
    unittest.main()
