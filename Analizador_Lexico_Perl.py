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

def t_BREAK(t):
    r'break'
    return t

def t_CASE(t):
    r'case'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_VOID(t):
    r'void'
    return t

def t_UNDEF(t):
    r'undef'
    return t

def t_STDIN(t):
    r'STDIN'
    return t

def t_CHMOD(t):
    r'chmod'
    return t

def t_CHOP(t):
    r'chop'
    return t

def t_CHOMP(t):
    r'chomp'
    return t

def t_CHOWN(t):
    r'chown'
    return t

def t_CLOSE(t):
    r'close'
    return t

def t_DEFINED(t):
    r'defined'
    return t

def t_DELETE(t):
    r'delete'
    return t

def t_DIE(t):
    r'die'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSIF(t):
    r'elsif'
    return t

def t_EOF(t):
    r'eof'
    return t

def t_EVAL(t):
    r'eval'
    return t

def t_EXEC(t):
    r'exec'
    return t

def t_EXIT(t):
    r'exit'
    return t

def t_FILENO(t):
    r'fileno'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FOR(t):
    r'for'
    return t


def t_FORK(t):
    r'fork'
    return t

def t_HEX(t):
    r'hex'
    return t

def t_IF(t):
    r'if'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_INDEX(t):
    r'index'
    return t

def t_INT(t):
    r'int'
    return t


def t_JOIN(t):
    r'join'
    return t

def t_KEYS(t):
    r'keys'
    return t

def t_LENGTH(t):
    r'length'
    return t

def t_LOCAL(t):
    r'local'
    return t

def t_LOG(t):
    r'log'
    return t

def t_MKDIR(t):
    r'mkdir'
    return t

def t_NEXT(t):
    r'next'
    return t

def t_NOT(t):
    r'not'
    return t

def t_OCT(t):
    r'oct'
    return t

def t_OPEN(t):
    r'open'
    return t

def t_POP(t):
    r'pop'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PUSH(t):
    r'push'
    return t

def t_RAND(t):
    r'rand'
    return t

def t_READ(t):
    r'read'
    return t

def t_RENAME(t):
    r'rename'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_RMDIR(t):
    r'rmdir'
    return t

def t_SEEK(t):
    r'seek'
    return t

def t_SELECT(t):
    r'select'
    return t

def t_SHIFT(t):
    r'shift'
    return t

def t_SIN(t):
    r'sin'
    return t

def t_SLEEP(t):
    r'sleep'
    return t

def t_SORT(t):
    r'sort'
    return t

def t_SPLIT(t):
    r'split'
    return t

def t_SQRT(t):
    r'sqrt'
    return t


def t_SUB(t):
    r'sub'
    return t

def t_SUBSTR(t):
    r'substr'
    return t

def t_SYSTEM(t):
    r'system'
    return t

def t_TELL(t):
    r'tell'
    return t

def t_VALUES(t):
    r'values'
    return t

def t_USE(t):
    r'use'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_WRITE(t):
    r'write'
    return t

def t_MY(t):
    r'my'
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
