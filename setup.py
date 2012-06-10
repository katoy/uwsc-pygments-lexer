""" 
A UWSC lexer for Pygments
""" 
from setuptools import setup 

setup( 
    name         = 'UWSCLexer', 
    version      = '0.1', 
    description  = __doc__, 
    author       = "Youichi Kato", 
    install_requires=['pygments'],
    packages     = ['uwsclexer'], 
    entry_points = '''
    [pygments.lexers]
    UWSCLexer = uwsclexer:UWSCLexer
    '''
) 
