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
     'AND_EQUAL',
     'IS_NOT_IDENTICAL',
     'IS_NOT_EQUAL',
     'BOOLEAN_AND',
     'BOOLEAN_OR',
     'CLASS_C',
     'CONCAT_EQUAL',
     'CONSTANT_ENCAPSED_STRING',
     'DEC',
     'DIR',
     'DIV_EQUAL',
     'DOUBLE_ARROW',
     'DOUBLE_COLON',
     'ELLIPSIS',
     'FILE',
     'FINALLY',
     'FUNC_C',
     'METHOD_C',
     'NS_C',

     # Symbols
     'PLUS',
     'INC',
     #'PLUSEQUAL',
     'MINUS',
     #'MINUSMINUS',
     #'MINUSEQUAL',
     'TIMES',
     'DIVIDE',
     'LESS',
     'IS_SMALLER_OR_EQUAL',
     'GREATER',
     'GREATER_OR_EQUAL',
     'EQUAL',
     'IS_IDENTICAL',
     'SPACESHIP'
     'LPAREN',
     'RPAREN',
     'LBRACKET',
     'RBRACKET',
     'LBLOCK',
     'RBLOCK',
     'COLON',
     'SEMICOLON',
     'QUOTATIONMARKS',
     'QUOTATIONMARKS1',
     'QUESTIONMARK',
     'AMPERSANT',
     'HASHTAG',
     'DOT',
     'DOLLARSIGN',
     'ATSIGN',
     'PERCENT',
     'MINUS_EQUAL',
     'MOD_EQUAL',
     'IS_EQUAL'
     'MUL_EQUAL',
     # Others
     'ID',
     'VARI',
     'NUMBER',
     'Cadena1',
     'Cadena2',


 )

t_PLUS   = r'\+'
t_MINUS  = r'\-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LESS   = r'<'
t_GREATER = r'>'
#t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_SEMICOLON = r';'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_QUOTATIONMARKS = r'\"'
t_QUOTATIONMARKS1 = r'\''
t_DOLLARSIGN = r'\$'
t_ATSIGN = r'\@'
t_QUESTIONMARK = r'\?'
t_PERCENT = r'\%'




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

def t_IF(t):
    r'if'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_GLOBAL(t):
    r'global'
    return t

def t_FUNCTION(t):
    r'function|cfunction'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_EXIT(t):
    r'exit'
    return t

def t_EVAL(t):
    r'eval'
    return t

def t_ENDWHILE(t):
    r'endwhile'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_ENDFOREACH(t):
    r'endforeach'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_ENDDECLARE(t):
    r'enddeclare'
    return t

def t_EMPTY(t):
    r'empty'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_DO(t):
    r'do'
    return t

def t_DIE(t):
    r'die'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CALLABLE(t):
    r'callable'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_AS(t):
    r'as'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_AND(t):
    r'and'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t

def t___HALT_COMPILER(t):
    r'__halt_compiler'
    return t

def t_CLASS_C(t):
    r'__CLASS__'
    return t

def t_DIR(t):
    r'__DIR__'
    return t

def t_FILE(t):
    r'__FILE__'
    return t

def t_FUNC_C(t):
    r'__FUNCTION__'
    return t

def t_LINE(t):
    r'__LINE__'
    return t

def t_METHOD_C(t):
    r'__METHOD__'
    return t

def t_NS_C(t):
    r'__NAMESPACE__'
    return t

#def t_CONSTANT_ENCAPSED_STRING(t):
#    r'(\"foo"|\'bar')'
#    return t

def t_FINALLY(t):
    r'finally'
    return

def t_OBJECT_OPERATOR(t):
    r'->'
    return t
def t_OR_EQUAL(t):
    r'\|\='
    return t
def t_PLUS_EQUAL(t):
    r'\+='
    return t
def t_POW(t):
    r'\*\*'
    return t
def t_POW_EQUAL(t):
    r'\*\*\='
    return t
def t_SL(t):
    r'<<'
    return t

def t_SL_EQUAL(t):
    r'<<='
    return t
def t_SR(t):
    r'>>'
    return t
def t_SR_EQUAL(t):
    r'>>='
    return t
def t_START_HEREDOC(t):
    r'<<<'
    return t
def t_XOR_EQUAL(t):
    r'^='
    return t
def t_YIELD(t):
    r'yield'
    return t

def t_IS_SMALLER_OR_EQUAL(t):
	r'<='
	return t

def t_GREATER_OR_EQUAL(t):
	r'>='
	return t

def t_SPACESHIP(t):
	r'<=>'
	return t

def t_IS_NOT_EQUAL(t):
	r'(!=|<>)'
	return t

def t_IS_EQUAL(t):
	r'=='
	return t

def t_INC(t):
	r'\+\+'
	return t

def t_DEC(t):
	r'--'
	return t

def t_IS_NOT_IDENTICAL(t):
	r'\!=='
	return t

def t_AND_EQUAL(t):
	r'\&='
	return t

def t_BOOLEAN_AND(t):
	r'\&\&'
	return t

def t_BOOLEAN_OR(t):
	r'\|\|'
	return t

def t_CONCAT_EQUAL(t):
	r'\.\='
	return t

def t_DOUBLE_ARROW(t):
	r'=>'
	return t

def t_DIV_EQUAL(t):
	r'/='
	return t

def t_DOUBLE_COLON(t):
	r'\:\:'
	return t

def t_IS_IDENTICAL(t):
	r'==='
	return t

def t_ELLIPSIS(t):
	r'\.\.\.'
	return t

def t_MINUS_EQUAL(t):
	r'-='
	return t

def t_MOD_EQUAL(t):
	r'%='
	return t

def t_MUL_EQUAL(t):
	r'\*='
	return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_VARI(t):
    r'(\$|\@|\%)\w+(_\d\w)*'
    return t

t_ignore = ' \t| \n'


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
		fin = 'evaluacion.php'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()
