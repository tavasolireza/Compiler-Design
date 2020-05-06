from ply import yacc
from lexer import Lexer


class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program(self, p):
        """program : declist MAIN LRB RRB block"""
        print("program : declist MAIN LRB RRB block")

    def p_program_2(self, p):
        """program : MAIN LRB RRB block"""
        print("program : declist MAIN LRB RRB block")

    def p_declist_dec(self, p):
        """declist : dec"""
        print("declist : dec")

    def p_declist_declist(self, p):
        """declist : declist dec"""
        print("declist : declist dec")

    # def p_declist_lambda(self, p):
    #     """declist : """
    #     print("declist : ")

    def p_dec_vardec(self, p):
        """dec : vardec"""
        print("dec : vardec")

    def p_dec_funcdec(self, p):
        """dec : funcdec"""
        print("dec : funcdec")

    def p_type_int(self, p):
        """type : INTEGER"""
        print("type : INTEGER")

    def p_type_float(self, p):
        """type : FLOAT"""
        print("type : FLOAT")

    def p_type_bool(self, p):
        """type : BOOLEAN"""
        print("type : BOOLEAN")

    def p_iddec_id(self, p):
        """iddec : ID"""
        print("iddec : ID")

    def p_iddec_id_s_exp(self, p):
        """iddec : ID LSB exp RSB"""
        print("iddec : ID LSB exp RSB")

    def p_iddec_id_assign_exp(self, p):
        """iddec : ID ASSIGN exp"""
        print("iddec : ID ASSIGN exp")

    def p_idlist_iddec(self, p):
        """idlist : iddec"""
        print("idlist : iddec")

    def p_idlist_idlist(self, p):
        """idlist : idlist COMMA iddec"""
        print("idlist : idlist COMMA iddec")

    def p_vardec(self, p):
        """vardec : type idlist SEMICOLON"""
        print("vardec : type idlist SEMICOLON")

    def p_funcdec_type(self, p):
        """funcdec : type ID LRB paramdecs RRB block"""
        print("funcdec : type ID LRB paramdecs RRB block")

    def p_funcdec_type_2(self, p):
        """funcdec : type ID LRB RRB block"""
        print("funcdec : type ID LRB RRB block")

    def p_funcdec_void(self, p):
        """funcdec : VOID ID LRB paramdecs RRB block"""
        print("funcdec : VOID ID LRB RRB block")

    def p_funcdec_void_2(self, p):
        """funcdec : VOID ID LRB RRB block"""
        print("funcdec : VOID ID LRB RRB block")

    def p_paramdecs_list(self, p):
        """paramdecs : paramdecslist"""
        print("paramdecs : paramdecslist")

    # def p_paramdecs_lambda(self, p):
    #     """paramdecs : """
    #     print("paramdecs : ")

    def p_paramdecslist_paramdec(self, p):
        """paramdecslist : paramdec"""
        print("paramdecslist : paramdec")

    def p_paramdecslist_paramdecslist(self, p):
        """paramdecslist : paramdecslist COMMA paramdec"""
        print("paramdecslist : paramdecslist COMMA paramdec")

    def p_paramdec(self, p):
        """paramdec : type ID"""
        print("paramdec : type ID")

    def p_paramdec_s(self, p):
        """paramdec : type ID LSB RSB"""
        print("paramdec : type ID LSB RSB")

    def p_varlist_vardec(self, p):
        """varlist : vardec"""
        print("varlist : vardec")

    def p_varlist_varlist(self, p):
        """varlist : varlist vardec"""
        print("varlist : varlist vardec")

    # def p_varlist_lambda(self, p):
    #     """varlist : """
    #     print("varlist : ")

    def p_block(self, p):
        """block : LCB varlist stmtlist RCB"""
        print("block : LCB varlist stmtlist RCB")

    def p_block_12(self, p):
        """block : LCB varlist RCB"""
        print("block : LCB varlist RCB")

    def p_block_2(self, p):
        """block : LCB stmtlist RCB"""
        print("block : LCB stmtlist RCB")

    def p_block_22(self, p):
        """block : LCB RCB"""
        print("block : LCB RCB")

    def p_stmtlist_stmt(self, p):
        """stmtlist : stmt"""
        print("stmtlist : stmt")

    def p_stmtlist_stmtlist(self, p):
        """stmtlist : stmtlist stmt"""
        print("stmtlist : stmtlist stmt")

    # def p_stmtlist_lambda(self, p):
    #     """stmtlist : """
    #     print("stmtlist : ")

    def p_lvalue_id(self, p):
        """lvalue : ID"""
        print("lvalue : ID COMMA ID LSB exp RSB")

    def p_lvalue_exp(self, p):
        """lvalue : ID LSB exp RSB"""
        print("lvalue : ID COMMA ID LSB exp RSB")

    def p_stmt_return(self, p):
        """stmt : RETURN exp SEMICOLON"""
        print("stmt : RETURN exp SEMICOLON")

    def p_stmt_exp(self, p):
        """stmt : exp SEMICOLON"""
        print("stmt : exp SEMICOLON")

    def p_stmt_block(self, p):
        """stmt : block"""
        print("stmt : block")

    def p_stmt_while(self, p):
        """stmt : WHILE LRB exp RRB stmt"""
        print("stmt : WHILE LRB exp RRB stmt")

    def p_stmt_for(self, p):
        """stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt"""
        print("stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt")

    # def p_stmt_if_addy(self, p):
    #     """stmt : IF LRB exp RRB stmt addy"""
    #
    # def p_stmt_if_addy_2(self, p):
    #     """stmt : IF LRB exp RRB stmt"""

    # def p_addy_1(self, p):
    #     """addy : """

    # def p_addy_2(self, p):
    #     """addy : elseiflist"""
    #
    # def p_addy_3(self, p):
    #     """addy : elseiflist ELSE stmt"""
    #
    # def p_addy_4(self, p):
    #     """addy : ELSE stmt"""

    # def p_stmt_if(self, p):
    #     """stmt : IF LRB exp RRB stmt elseiflist"""
    #     print("stmt : IF LRB exp RRB stmt elseiflist")

    # def p_stmt_if_2(self, p):
    #     """stmt : IF LRB exp RRB stmt"""
    #     print("stmt : IF LRB exp RRB stmt")

    # def p_stmt_if_long(self, p):
    #     """stmt : IF LRB exp RRB stmt elseiflist ELSE stmt"""
    #     print("stmt : IF LRB exp RRB stmt elseiflist ELSE stmt")

    # def p_stmt_if_long_2(self, p):
    #     """stmt : IF LRB exp RRB stmt ELSE stmt"""
    #     print("stmt : IF LRB exp RRB stmt ELSE stmt")

    def p_stmt_if(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist"""
        print("stmt : IF LRB exp RRB stmt elseiflist")

    def p_stmt_if_long(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist ELSE stmt"""
        print("stmt : IF LRB exp RRB stmt elseiflist ELSE stmt")

    def p_stmt_print(self, p):
        """stmt : PRINT LRB ID RRB SEMICOLON"""
        print("stmt : PRINT LRB ID RRB SEMICOLON")

    # def p_elseiflist_elif(self, p):
    #     """elseiflist : ELIF LRB exp RRB stmt"""
    #     print("elseiflist : ELIF LRB exp RRB stmt")
    #
    # def p_elseiflist_elseiflist(self, p):
    #     """elseiflist : elseiflist ELIF LRB exp RRB stmt"""
    #     print("elseiflist : elseiflist ELIF LRB exp RRB stmt")

    # def p_elseiflist_lambda(self, p):
    #     """elseiflist : """
    #     print("elseiflist : ")

    def p_elseiflist_elif(self, p):
        """elseiflist : ELIF LRB exp RRB stmt"""
        print("elseiflist : ELIF LRB exp RRB stmt")

    def p_elseiflist_elseiflist(self, p):
        """elseiflist : elseiflist ELIF LRB exp RRB stmt"""
        print("elseiflist : elseiflist ELIF LRB exp RRB stmt")

    def p_elseiflist_lambda(self, p):
        """elseiflist : """
        print("elseiflist : ")

    def p_exp_lvalue_exp(self, p):
        """exp : lvalue ASSIGN exp"""
        print("exp : lvalue ASSIGN exp")

    def p_exp_operator(self, p):
        """exp : exp operator exp"""
        print("exp : exp operator exp")



    def p_exp_relop(self, p):
        """exp : exp relop exp"""
        print("exp : exp relop exp")

    def p_exp_const(self, p):
        """exp : const"""
        print("exp : const")

    def p_exp_lvalue(self, p):
        """exp : lvalue"""
        print("exp : lvalue")

    def p_exp_id_explist(self, p):
        """exp : ID LRB explist RRB"""
        print("exp : ID LRB explist RRB")

    def p_exp_r_exp(self, p):
        """exp : LRB exp RRB"""
        print("exp : LRB exp RRB")

    def p_exp_id(self, p):
        """exp : ID LRB RRB"""
        print("exp : ID LRB RRB")

    def p_exp_sub_exp(self, p):
        """exp : SUB exp"""
        print("exp : SUB exp")

    def p_exp_not_exp(self, p):
        """exp : NOT exp"""
        print("exp : NOT exp")

    def p_operator_or(self, p):
        """operator : OR"""
        print("operator : OR")

    def p_operator_and(self, p):
        """operator : AND"""
        print("operator : AND")

    def p_operator_sum(self, p):
        """operator : SUM"""
        print("operator : SUM")

    def p_operator_sub(self, p):
        """operator : SUB"""
        print("operator : SUB")

    def p_operator_mul(self, p):
        """operator : MUL"""
        print("operator : MUL")

    def p_operator_div(self, p):
        """operator : DIV"""
        print("operator : DIV")

    def p_operator_mod(self, p):
        """operator : MOD"""
        print("operator : MOD")

    def p_const_int(self, p):
        """const : INTEGERNUMBER"""
        print("const : INTEGERNUMBER")

    def p_const_float(self, p):
        """const : FLOATNUMBER"""
        print("const : FLOATNUMBER")

    def p_const_true(self, p):
        """const : TRUE"""
        print("const : TRUE")

    def p_const_false(self, p):
        """const : FALSE"""
        print("const : FALSE")

    def p_relop_gt(self, p):
        """relop : GT"""
        print("relop : GT")

    def p_relop_lt(self, p):
        """relop : LT"""
        print("relop : LT")

    def p_relop_ne(self, p):
        """relop : NE"""
        print("relop : NE")

    def p_relop_eq(self, p):
        """relop : EQ"""
        print("relop : EQ")

    def p_relop_le(self, p):
        """relop : LE"""
        print("relop : LE")

    def p_relop_ge(self, p):
        """relop : GE"""
        print("relop : GE")

    def p_explist_exp(self, p):
        """explist : exp"""
        print("explist : exp")

    def p_explist_explist(self, p):
        """explist : explist COMMA exp"""
        print("explist : explist COMMA exp")

    precedence = (
        ('right', 'ASSIGN'),
        ('left', 'NOT'),
        ('left', 'ELIF'),
        ('left', 'ELSE'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'LT'),
        ('left', 'GT'),
        ('left', 'GE'),
        ('left', 'NE'),
        ('left', 'EQ'),
        ('left', 'LE'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV')
    )

    def p_error(self, p):
        print(p.value)
        raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
