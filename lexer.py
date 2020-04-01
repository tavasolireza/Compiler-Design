from ply import lex


class Lexer:
    tokens = [
        'ID', 'INTEGERNUMBER', 'FLOATNUMBER',  # 'ERROR!',
        'INTEGER', 'FLOAT', 'BOOLEAN', 'VOID', 'TRUE', 'FALSE', 'PRINT', 'RETURN', 'MAIN', 'IF', 'ELSE', 'ELIF',
        'WHILE', 'FOR', 'AND', 'OR', 'NOT', 'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV', 'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ',
        'NE', 'LCB', 'RCB', 'LRB', 'RRB', 'LSB', 'RSB', 'SEMICOLON', 'COMMA',
    ]

    reserved = {
        'int': "INTEGER",
        'float': "FLOAT",
        'bool': "BOOLEAN",
        'void': "VOID",
        'true': "TRUE",
        'false': "FALSE",
        'print': "PRINT",
        'return': "RETURN",
        'main': "MAIN",
        'if': "IF",
        'else': "ELSE",
        'elif': "ELIF",
        'while': "WHILE",
        'for': "FOR",
    }

    # t_INTEGER = r'int'
    # t_FLOAT = r'float'
    # t_BOOLEAN = r'bool'
    # t_VOID = r'void'
    # t_TRUE = r'true'
    # t_FALSE = r'false'
    # t_PRINT = r'print'
    # t_RETURN = r'return'
    # t_MAIN = r'main'
    # t_IF = r'if'
    # t_ELSE = r'else'
    # t_ELIF = r'elif'
    # t_WHILE = r'while'
    # t_FOR = r'for'
    t_AND = r'\&\&'
    t_OR = r'\|\|'
    t_NOT = r'\!'
    t_ASSIGN = r'\='
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD = r'\%'
    t_GT = r'\>'
    t_GE = r'\>\='
    t_LT = r'\<'
    t_LE = r'\<\='
    t_EQ = r'\=\='
    t_NE = r'\!\='
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\['
    t_RSB = r'\]'
    t_SEMICOLON = r';'
    t_COMMA = r'\,'

    # # COLONS
    # t_SEMICOLON = r';'
    # # BRACKETS
    # t_LRB = r'\('
    # t_RRB = r'\)'
    # t_LCB = r'\{'
    # t_RCB = r'\}'
    # # OPERATOR
    # t_SUM = r'\+'
    # t_SUB = r'\-'
    # t_MUL = r'\*'
    # t_DIV = r'\/'
    # t_LT = r'\<'
    # t_GT = r'\>'
    # # KW
    # t_IF = r'if'
    # t_WHILE = r'while'
    # t_PRINT = r'print'

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')  # Check for reserved words
        print('this is length ', t.value.__len__(), t.value[1])
        return t

    def t_FLOATNUMBER(self, t):
        r'[0-9]{1,10}\.[0-9]+'
        t.value = float(t.value)
        return t

    def t_INTEGERNUMBER(self, t):
        r'[0-9]{1,10}'
        # r'((?!^0\d+)^0)|((?!0+)\d{1,10})'
        t.value = int(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t'

    def t_error(self, t):
        # raise Exception('Error at', t.value)
        print("*************", t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
