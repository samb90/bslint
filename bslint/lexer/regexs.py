# this characters need escaping . ^ $ * + ? { } [ ] \ | ( )
import collections

import bslint.constants as const

Regex = collections.namedtuple('Token', ['regex', 'lexer_type', 'parser_type', 'indentation'])

List = [
    Regex._make([r"\n", const.NEW_LINE, const.NEW_LINE, const.NO_INDENTATION]),
    Regex._make([r"\s", None, None, const.NO_INDENTATION]),

    Regex._make(["\+=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["-=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["\*=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["/=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make([r"\\=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),  # divide integer
    Regex._make(["<<=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make([">>=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["<>", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make([">=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["<=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make([">=", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["=>", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["=<", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),

    Regex._make([">>", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["<<", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),

    Regex._make([";", const.SEMI_COLON, const.SEMI_COLON, const.NO_INDENTATION]),
    Regex._make(["@", const.AT_SYMBOL, const.AT_SYMBOL, const.NO_INDENTATION]),
    Regex._make(["#", const.HASH_SYMBOL, const.HASH_SYMBOL, const.NO_INDENTATION]),
    Regex._make([r"\.", const.SPECIAL_OPERATOR, const.DOT, const.NO_INDENTATION]),
    Regex._make([":", const.COLON, const.COLON, const.NO_INDENTATION]),
    Regex._make([r"\^", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make([r"\&", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make([r"\\", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["=", const.OPERATOR, const.EQUALS, const.NO_INDENTATION]),
    Regex._make(["-", const.OPERATOR, const.MINUS, const.NO_INDENTATION]),
    Regex._make(["\+", const.OPERATOR, const.PLUS, const.NO_INDENTATION]),
    Regex._make(["\*", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make([r"/", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make(["<", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),
    Regex._make([">", const.OPERATOR, const.OPERATOR, const.NO_INDENTATION]),

    Regex._make([r"\(", const.BRACKET, const.OPEN_PARENTHESIS, const.NO_INDENTATION]),
    Regex._make([r"\)", const.BRACKET, const.CLOSE_PARENTHESIS, const.NO_INDENTATION]),
    Regex._make([r"\[", const.SQUARE_BRACKET, const.OPEN_SQUARE_BRACKET, const.NO_INDENTATION]),
    Regex._make([r"\]", const.SQUARE_BRACKET, const.CLOSE_SQUARE_BRACKET, const.NO_INDENTATION]),
    Regex._make([r"\{", const.OPEN_CURLY_BRACKET, const.OPEN_CURLY_BRACKET, const.NO_INDENTATION]),
    Regex._make([r"\}", const.CLOSE_CURLY_BRACKET, const.CLOSE_CURLY_BRACKET, const.NO_INDENTATION]),
    Regex._make([",", const.SPECIAL_OPERATOR, const.COMMA, const.NO_INDENTATION]),
    Regex._make([r"(TRUE)\b", const.KEYWORD, const.VALUE, const.NO_INDENTATION]),
    Regex._make([r"(GETLASTRUNCOMPILEERROR)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(GETLASTRUNRUNTIMEERROR)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(GETGLOBALAA)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(ELSE IF)\b", const.KEYWORD, const.IF_STATEMENT, const.SPECIAL_INDENTATION]),

    Regex._make([r"(END IF)\b", const.KEYWORD, const.END_IF_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(EXIT FOR)\b", const.KEYWORD, const.KEYWORD, const.DECREMENT_INDENTATION]),
    Regex._make([r"(FOR EACH)\b", const.KEYWORD, const.FOR_EACH, const.INCREMENT_INDENTATION]),
    Regex._make([r"(END FOR)\b", const.KEYWORD, const.END_FOR_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(END WHILE)\b", const.KEYWORD, const.END_WHILE_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(EXIT WHILE)\b", const.KEYWORD, const.KEYWORD, const.DECREMENT_INDENTATION]),
    Regex._make([r"(END FUNCTION)\b", const.KEYWORD, const.END_FUNCTION_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(END SUB)\b", const.KEYWORD, const.END_SUB_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(LINE_NUM)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(GOTO)\b", const.KEYWORD, const.GOTO, const.NO_INDENTATION]),
    Regex._make([r"(CREATEOBJECT)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(ELSEIF)\b", const.KEYWORD, const.IF_STATEMENT, const.SPECIAL_INDENTATION]),
    Regex._make([r"(ENDIF)\b", const.KEYWORD, const.END_IF_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(ENDFOR)\b", const.KEYWORD, const.END_FOR_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(ENDWHILE)\b", const.KEYWORD, const.END_WHILE_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(EXITWHILE)\b", const.KEYWORD, const.KEYWORD, const.DECREMENT_INDENTATION]),
    Regex._make([r"(ENDFUNCTION)\b", const.KEYWORD, const.END_FUNCTION_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(ENDSUB)\b", const.KEYWORD, const.END_SUB_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(OBJFUN)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),

    Regex._make([r"(Tan)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Sqr)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Sin)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Sgn)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Log)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Int)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Fix)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Exp)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Cint)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Cdbl)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Csng)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Cos)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Atn)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Abs)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Substitute)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Tr)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Val)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Stringi)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Stri)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Str)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Right)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Len)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Left)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Instr)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Chr)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Asc)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(LCase)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Ucase)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(FormatJson)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(ParseJson)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(RunGarbageCollector)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(strtoi)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(FormatDrive)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(CreateDirectory)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(DeleteDirectory)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(DeleteFile)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(MatchFiles)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(MoveFile)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(CopyFile)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(WriteAsciiFile)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(ReadAsciiFile)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(RebootSystem)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(UpTime)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(GetInterface)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Wait)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Sleep)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Eval)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Run)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Box)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(FindMemberFunction)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Rnd)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Type)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Void)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Dynamic)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Float)\b", const.KEYWORD, const.TYPE, const.NO_INDENTATION]),
    Regex._make([r"(Double)\b", const.KEYWORD, const.TYPE, const.NO_INDENTATION]),
    Regex._make([r"(Integer)\b", const.KEYWORD, const.TYPE, const.NO_INDENTATION]),
    Regex._make([r"(LongInteger)\b", const.KEYWORD, const.TYPE, const.NO_INDENTATION]),
    Regex._make([r"(String)\b", const.KEYWORD, const.TYPE, const.NO_INDENTATION]),
    Regex._make([r"(Boolean)\b", const.KEYWORD, const.TYPE, const.NO_INDENTATION]),
    Regex._make([r"(Object)\b", const.KEYWORD, const.TYPE, const.NO_INDENTATION]),
    Regex._make([r"(Until)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(On)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Library)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Generates)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Implements)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Event)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Interface)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(Component)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),

    Regex._make([r"(IF)\b", const.KEYWORD, const.IF_STATEMENT, const.INCREMENT_INDENTATION]),
    Regex._make([r"(THEN)\b", const.KEYWORD, const.THEN, const.INCREMENT_INDENTATION]),
    Regex._make([r"(ELSE)\b", const.KEYWORD, const.KEYWORD, const.SPECIAL_INDENTATION]),
    Regex._make([r"(FOR)\b", const.KEYWORD, const.FOR, const.INCREMENT_INDENTATION]),
    Regex._make([r"(TO)\b", const.KEYWORD, const.TO, const.NO_INDENTATION]),
    Regex._make([r"(STEP)\b", const.KEYWORD, const.STEP, const.NO_INDENTATION]),
    Regex._make([r"(INVALID)\b", const.KEYWORD, const.INVALID, const.NO_INDENTATION]),
    Regex._make([r"(IN)\b", const.KEYWORD, const.IN, const.NO_INDENTATION]),
    Regex._make([r"(WHILE)\b", const.KEYWORD, const.WHILE, const.INCREMENT_INDENTATION]),
    Regex._make([r"(FUNCTION)\b", const.KEYWORD, const.FUNCTION, const.INCREMENT_INDENTATION]),
    Regex._make([r"(AS)\b", const.KEYWORD, const.AS, const.NO_INDENTATION]),
    Regex._make([r"(RETURN)\b", const.KEYWORD, const.RETURN, const.NO_INDENTATION]),
    Regex._make([r"(PRINT)\b", const.PRINT_KEYWORD, const.PRINT_KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(DIM)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(END)\b", const.KEYWORD, const.END_TOKEN, const.DECREMENT_INDENTATION]),
    Regex._make([r"(MOD)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(STOP)\b", const.KEYWORD, const.STOP, const.NO_INDENTATION]),
    Regex._make([r"(AND)\b", const.KEYWORD, const.AND, const.NO_INDENTATION]),
    Regex._make([r"(BOX)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(EACH)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(EVAL)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(EXIT)\b", const.KEYWORD, const.KEYWORD, const.DECREMENT_INDENTATION]),
    Regex._make([r"(FALSE)\b", const.KEYWORD, const.VALUE, const.NO_INDENTATION]),
    Regex._make([r"(LET)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(NEXT)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(NOT)\b", const.KEYWORD, const.NOT, const.NO_INDENTATION]),
    Regex._make([r"(OR)\b", const.KEYWORD, const.OR, const.NO_INDENTATION]),
    Regex._make([r"(POS)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"('|rem) *(BSLINT)_(?P<command>[a-z_]+)(:(?P<param>[0-9]+))?.*", const.BSLINT_COMMAND, const.BSLINT_COMMAND, const.NO_INDENTATION]),
    Regex._make([r"('|REM\b) *(.*)", const.COMMENT, const.COMMENT, const.NO_INDENTATION]),
    Regex._make([r"(RUN)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(SUB)\b", const.KEYWORD, const.SUB, const.INCREMENT_INDENTATION]),
    Regex._make([r"(TAB)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make([r"(TYPE)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),

    Regex._make([r"(MAIN)\b", const.KEYWORD, const.KEYWORD, const.NO_INDENTATION]),
    Regex._make(["\?", const.PRINT_KEYWORD, const.PRINT_KEYWORD, const.NO_INDENTATION]),

    Regex._make([r"(?P<value>^[a-z_][a-z0-9_]*)(?P<type>\$|%|!|#|&?)", const.ID, const.ID, const.NO_INDENTATION]),
    Regex._make(['\"(?P<value>.*)\"', const.STRING, const.VALUE, const.NO_INDENTATION]),
    Regex._make([r"^\d*(\.?\d+){1}", const.NUMERIC, const.VALUE, const.NO_INDENTATION]),
]