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
