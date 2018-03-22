import ply.lex as lex
import sys

# list of tokens
tokens = (
    # Reserverd words
     '__HALT_COMPILER',
     'ABSTRACT',
     'AND', 
     'ARRAY', 
     'AS',
     'BREAK', 
     'CALLABLE', 
     'CASE', 
     'CATCH', 
     'CLASS', 
     'CLONE', 
     'CONST', 
     'CONTINUE', 
     'DECLARE', 
     'DEFAULT',
     'DIE', 
     'DO', 
     'ECHO', 
     'ELSE', 
     'ELSEIF', 
     'EMPTY', 
     'ENDDECLARE',
     'ENDFOR', 
     'ENDFOREACH',
     'ENDIF', 
     'ENDSWITCH', 
     'ENDWHILE', 
     'EVAL', 
     'EXIT', 
     'EXTENDS', 
     'FINAL', 
     'FOR', 
     'FOREACH', 
     'FUNCTION', 
     'GLOBAL', 
     'GOTO', 
     'IF', 
     'IMPLEMENTS', 
     'INCLUDE', 
     'INCLUDE_ONCE', 
     'INSTANCEOF', 
     'INSTEADOF', 
     'INTERFACE', 
     'ISSET', 
     'LIST', 
     'NAMESPACE', 
     'NEW', 
     'OR', 
     'PRINT', 
     'PRIVATE', 
     'PROTECTED', 
     'PUBLIC', 
     'REQUIRE', 
     'REQUIRE_ONCE', 
     'RETURN',
     'STATIC', 
     'SWITCH', 
     'THROW', 
     'TRAIT', 
     'TRY', 
     'UNSET', 
     'USE', 
     'VAR', 
     'WHILE', 
     'XOR',

     # Symbols
     'PLUS',
     'PLUSPLUS',
     #'PLUSEQUAL',
     'MINUS',
     'MINUSMINUS',
     #'MINUSEQUAL',
     'TIMES',
     'DIVIDE',
     'LESS',
     'LESSEQUAL',
     'GREATER',
     'GREATEREQUAL',
     'EQUAL',
     'DEQUAL',
     'DISTINT',
     'ISEQUAL',
     'SEMICOLON',
     'COMMA',
     'LPAREN',
     'RPAREN',
     'LBRACKET',
     'RBRACKET',
     'LBLOCK',
     'RBLOCK',
     'COLON',
     'QUOTATIONMARKS',
     'QUOTATIONMARKS1',
     'QUESTIONMARK',
     'AMPERSANT',
     'HASHTAG',
     'DOT',
     'DOLLARSIGN',
     'ATSIGN',
     # Others
     'ID',
     'VAR',
     'NUMBER',
     'Cadena1',
     'Cadena2',
 )

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_QUOTATIONMARKS = r'\"'
t_QUOTATIONMARKS1 = r'\''
t_DOLLARSIGN = r'\$'
t_ATSIGN = r'\@'
t_QUESTIONMARK = r'\?'
t_PERCENT = r'\%'


def t_ABS(t):
    r'abs'
    return t
def t_XOR(t):
    r'xor'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_VAR(t):
    r'var'
    return t
def t_USE(t):
    r'user'
    return t
def t_UNSET(t):
    r'unset'
    return t
def t_TRY(t):
    r'try'
    return t
def t_TRAIT(t):
    r'trait'
    return t
def t_THROW(t):
    r'throw'
    return t
def t_SWITCH(t):
    r'switch'
    return t
def t_STATIC(t):
    r'static'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_REQUIRE_ONCE(t):
    r'require_once'
    return t
def t_REQUIRE(t):
    r'require'
    return t
def t_PUBLIC(t):
    r'public'
    return t
def t_PROTECTED(t):
    r'protected'
    return t
def t_PRIVATE(t):
    r'private'
    return t
def t_PRINT(t):
    r'print'
    return t
def t_OR(t):
    r'or'
    return t
def t_NEW(t):
    r'new'
    return t
def t_NAMESPACE(t):
    r'namespace'
    return t
def t_LIST(t):
    r'list'
    return t
def t_ISSET(t):
    r'isset'
    return t
def t_INTERFACE(t):
    r'interface'
    return t
def t_INSTEADOF(t):
    r'insteadof'
    return t
def t_instanceof(t):
    r'instranceof'
    return t
def t_INCLUDE_ONCE(t):
    r'include_once'
    return t
def t_INCLUDE(t):
    r'include'
    return t
def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t

def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_VAR(t):
    r'(\$|\@|\%)\w+(_\d\w)*'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comments(t):
    r'\#(.)*?\n'
    t.lexer.lineno += t.value.count('\n')


def t_Cadena1(t):
    r'(\")(.)*(\")'
    return t

def t_Cadena2(t):
    r'(\')(.)*(\')'
    return t


def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()


if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion.pl'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()
