import bslint.constants as const
import bslint.parser.rule_builder as rule_builder


RULES_LIST = {
    const.PRIORITY_ZERO: {
        const.END_FOR_TOKEN: [([const.END_FOR_TOKEN], const.END_FOR)],
        const.END_IF_TOKEN: [([const.END_IF_TOKEN], const.END_IF)],
        const.END_WHILE_TOKEN: [([const.END_WHILE_TOKEN], const.END_WHILE)],
        const.END_SUB_TOKEN: [([const.END_SUB_TOKEN], const.END_FUNCTION)],
        const.END_FUNCTION_TOKEN: [([const.END_FUNCTION_TOKEN], const.END_FUNCTION)],
        const.END_TOKEN: [([const.END_TOKEN], const.END)],
        const.RETURN: [([const.RETURN], const.RETURN_STMT)],
        const.EXIT: [([const.EXIT], const.EXIT_STMT)],
        const.ELSE: [([const.ELSE], const.ELSE_STMT)],
        const.CLOSE_PARENTHESIS: [
            ([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.ID, const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.ID, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.ID, const.OPEN_PARENTHESIS, const.VAR_AS, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.ID, const.OPEN_PARENTHESIS, const.FUNCTION_CALL, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.ID, const.OPEN_PARENTHESIS, const.ENUMERABLE_OBJECT, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.ID, const.OPEN_PARENTHESIS, const.VALUE, const.ARGUMENT, const.CLOSE_PARENTHESIS],
             const.FUNCTION_CALL),
            ([const.BUILT_IN_FUNCTION, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
             const.FUNCTION_CALL),
            ([const.BUILT_IN_FUNCTION, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.BUILT_IN_FUNCTION, const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS],
             const.FUNCTION_CALL),
            ([const.BUILT_IN_FUNCTION, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS],
             const.FUNCTION_CALL),
            ([const.BUILT_IN_FUNCTION, const.OPEN_PARENTHESIS, const.FUNCTION_CALL, const.CLOSE_PARENTHESIS],
             const.FUNCTION_CALL),
            ([const.BUILT_IN_FUNCTION, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
             const.FUNCTION_CALL),
            ([const.BUILT_IN_FUNCTION, const.OPEN_PARENTHESIS, const.FUNCTION_CALL, const.ARGUMENT,
              const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
            ([const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS], const.ID),
        ],
        const.ENUMERABLE_OBJECT: [
            ([const.ID, const.ENUMERABLE_OBJECT], const.ID),
        ],
        const.ID: [
            ([const.ID, const.DOT, const.ID], const.ID),
            ([const.FUNCTION_CALL, const.DOT, const.ID], const.ID),
        ],
        const.FUNCTION_CALL: [
            ([const.FUNCTION_CALL, const.DOT, const.FUNCTION_CALL], const.FUNCTION_CALL),
            ([const.ID, const.DOT, const.FUNCTION_CALL], const.FUNCTION_CALL),
        ],
        const.BUILT_IN_FUNCTION: [
            ([const.ID, const.DOT, const.BUILT_IN_FUNCTION], const.ID)
        ],
        const.KEYWORD: [
            ([const.ID, const.DOT, const.KEYWORD], const.ID)
        ]
    },
    const.PRIORITY_ONE: {
        const.VALUE: [
            ([const.VALUE, const.PLUS, const.VALUE], const.VALUE),
            ([const.VALUE, const.PLUS, const.PLUS, const.VALUE], const.VALUE),
            ([const.VALUE, const.PLUS, const.MINUS, const.VALUE], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.VALUE], const.VALUE),
            ([const.ID, const.PLUS, const.VALUE], const.VALUE),
            ([const.ID, const.PLUS, const.PLUS, const.VALUE], const.VALUE),
            ([const.ID, const.PLUS, const.MINUS, const.VALUE], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.VALUE], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.VALUE], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.VALUE], const.VALUE),
            ([const.VALUE, const.MINUS, const.PLUS, const.VALUE], const.VALUE),
            ([const.ID, const.MINUS, const.PLUS, const.VALUE], const.VALUE),
            ([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.VALUE], const.VALUE),
            ([const.WHILE, const.PLUS, const.VALUE], const.WHILE_STMT),
            ([const.VALUE, const.MINUS, const.VALUE], const.VALUE),
            ([const.VALUE, const.MINUS, const.MINUS, const.VALUE], const.VALUE),
            ([const.ID, const.MINUS, const.VALUE], const.VALUE),
            ([const.ID, const.MINUS, const.MINUS, const.VALUE], const.VALUE),
            ([const.FUNCTION_CALL, const.MINUS, const.VALUE], const.VALUE),
            ([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.VALUE], const.VALUE),
            ([const.WHILE, const.MINUS, const.VALUE], const.WHILE_STMT),
        ],
        const.ID: [
            ([const.ID, const.PLUS, const.ID], const.VALUE),
            ([const.ID, const.PLUS, const.PLUS, const.ID], const.VALUE),
            ([const.ID, const.PLUS, const.MINUS, const.ID], const.VALUE),
            ([const.VALUE, const.PLUS, const.ID], const.VALUE),
            ([const.VALUE, const.PLUS, const.PLUS, const.ID], const.VALUE),
            ([const.VALUE, const.PLUS, const.MINUS, const.ID], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.ID], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.ID], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.ID], const.VALUE),
            ([const.ID, const.MINUS, const.PLUS, const.ID], const.VALUE),
            ([const.VALUE, const.MINUS, const.PLUS, const.ID], const.VALUE),
            ([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.ID], const.VALUE),
            ([const.WHILE, const.PLUS, const.ID], const.WHILE_STMT),
            ([const.ID, const.MINUS, const.ID], const.VALUE),
            ([const.ID, const.MINUS, const.MINUS, const.ID], const.VALUE),
            ([const.VALUE, const.MINUS, const.ID], const.VALUE),
            ([const.VALUE, const.MINUS, const.MINUS, const.ID], const.VALUE),
            ([const.FUNCTION_CALL, const.MINUS, const.ID], const.VALUE),
            ([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.ID], const.VALUE),
            ([const.WHILE, const.MINUS, const.ID], const.WHILE_STMT),
        ],
        const.FUNCTION_CALL: [
            ([const.VALUE, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.ID, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.ID, const.PLUS, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.ID, const.PLUS, const.MINUS, const.FUNCTION_CALL], const.VALUE),
            ([const.VALUE, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.VALUE, const.PLUS, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.VALUE, const.PLUS, const.MINUS, const.FUNCTION_CALL], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.FUNCTION_CALL], const.VALUE),
            ([const.ID, const.MINUS, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.VALUE, const.MINUS, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.FUNCTION_CALL], const.VALUE),
            ([const.WHILE, const.PLUS, const.FUNCTION_CALL], const.WHILE_STMT),
            ([const.ID, const.MINUS, const.FUNCTION_CALL], const.VALUE),
            ([const.ID, const.MINUS, const.MINUS, const.FUNCTION_CALL], const.VALUE),
            ([const.VALUE, const.MINUS, const.FUNCTION_CALL], const.VALUE),
            ([const.VALUE, const.MINUS, const.MINUS, const.FUNCTION_CALL], const.VALUE),
            ([const.FUNCTION_CALL, const.MINUS, const.FUNCTION_CALL], const.VALUE),
            ([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.FUNCTION_CALL], const.VALUE),
            ([const.WHILE, const.MINUS, const.FUNCTION_CALL], const.WHILE_STMT),
        ],
    },
    const.PRIORITY_TWO: {
        const.ID: [([const.ID, const.COLON, const.ID], const.ASSOCIATIVE_ARRAY_ARGUMENT)],
        const.CLOSE_SQUARE_BRACKET: [
            ([const.OPEN_SQUARE_BRACKET, const.CLOSE_SQUARE_BRACKET], const.ENUMERABLE_OBJECT),
            ([const.OPEN_SQUARE_BRACKET, const.VALUE, const.CLOSE_SQUARE_BRACKET], const.ENUMERABLE_OBJECT),
            ([const.OPEN_SQUARE_BRACKET, const.ID, const.CLOSE_SQUARE_BRACKET], const.ENUMERABLE_OBJECT),
            ([const.OPEN_SQUARE_BRACKET, const.ARGUMENT, const.CLOSE_SQUARE_BRACKET],
             const.ENUMERABLE_OBJECT),
        ],
        const.FUNCTION_CALL: [([const.ID, const.COLON, const.FUNCTION_CALL], const.ASSOCIATIVE_ARRAY_ARGUMENT)],
        const.ANONYMOUS_FUNCTION_BLOCK: [([const.ID, const.COLON, const.ANONYMOUS_FUNCTION_BLOCK],
                                          const.ASSOCIATIVE_ARRAY_ARGUMENT)],
        const.VALUE: [
            ([const.ID, const.COLON, const.VALUE], const.ASSOCIATIVE_ARRAY_ARGUMENT),
            ([const.VALUE, const.COLON, const.VALUE], const.ASSOCIATIVE_ARRAY_ARGUMENT),
            ([const.VALUE, const.OPERATOR, const.VALUE], const.VALUE),
            ([const.ID, const.OPERATOR, const.VALUE], const.VALUE),
            ([const.FUNCTION_CALL, const.OPERATOR, const.VALUE], const.VALUE),
        ],
        const.ENUMERABLE_OBJECT: [([const.ID, const.COLON, const.ENUMERABLE_OBJECT], const.ASSOCIATIVE_ARRAY_ARGUMENT)],
    },
    const.PRIORITY_THREE: {
        const.VALUE: [
            ([const.ID, const.EQUALS, const.VALUE], const.VAR_AS),
            ([const.ID, const.EQUALS, const.MINUS, const.VALUE], const.VAR_AS),
            ([const.ID, const.EQUALS, const.PLUS, const.VALUE], const.VAR_AS),
            ([const.VALUE, const.EQUALS, const.VALUE], const.CONDITION),
            ([const.FUNCTION_CALL, const.EQUALS, const.VALUE], const.CONDITION),
            ([const.ANONYMOUS_FUNCTION_DECLARATION, const.EQUALS, const.VALUE], const.CONDITION),
            ([const.ELSE_IF, const.FUNCTION_CALL, const.EQUALS, const.VALUE], const.ELSE_IF_STMT),
        ],
        const.ENUMERABLE_OBJECT: [
            ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT], const.VAR_AS)
        ],
        const.FUNCTION_CALL: [
            ([const.ID, const.EQUALS, const.FUNCTION_CALL], const.VAR_AS),
            ([const.ID, const.EQUALS, const.MINUS, const.FUNCTION_CALL], const.VAR_AS),
            ([const.ID, const.EQUALS, const.PLUS, const.FUNCTION_CALL], const.VAR_AS),
            ([const.VALUE, const.EQUALS, const.FUNCTION_CALL], const.CONDITION),
            ([const.FUNCTION_CALL, const.EQUALS, const.FUNCTION_CALL], const.CONDITION),
            ([const.ANONYMOUS_FUNCTION_DECLARATION, const.EQUALS, const.FUNCTION_CALL], const.CONDITION),
        ],
        const.ID: [
            ([const.ID, const.EQUALS, const.ID], const.VAR_AS),
            ([const.ID, const.EQUALS, const.MINUS, const.ID], const.VAR_AS),
            ([const.ID, const.EQUALS, const.PLUS, const.ID], const.VAR_AS),
            ([const.VALUE, const.EQUALS, const.ID], const.CONDITION),
            ([const.FUNCTION_CALL, const.EQUALS, const.ID], const.CONDITION),
            ([const.ANONYMOUS_FUNCTION_DECLARATION, const.EQUALS, const.ID], const.CONDITION),
        ],
        const.ANONYMOUS_FUNCTION_BLOCK: [
            ([const.ID, const.EQUALS, const.ANONYMOUS_FUNCTION_BLOCK], const.VAR_AS),
        ],
    },
    const.PRIORITY_FOUR: {
        const.ID: [
            ([const.ID, const.COMMA, const.ID], const.ARGUMENT),
            ([const.VALUE, const.COMMA, const.ID], const.ARGUMENT),
            ([const.FUNCTION_CALL, const.COMMA, const.ID], const.ARGUMENT),
            ([const.VAR_AS, const.COMMA, const.ID], const.ARGUMENT),
            ([const.ARGUMENT, const.COMMA, const.ID], const.ARGUMENT),
            ([const.PRINT_ARGUMENT, const.COMMA, const.ID], const.PRINT_ARGUMENT),
            ([const.ENUMERABLE_OBJECT, const.COMMA, const.ID], const.ARGUMENT),
            ([const.PARAM, const.COMMA, const.ID], const.ARGUMENT),
            ([const.PRINT_STMT, const.COMMA, const.ID], const.PRINT_STMT)
        ], const.VALUE: [
            ([const.ID, const.COMMA, const.VALUE], const.ARGUMENT),
            ([const.VALUE, const.COMMA, const.VALUE], const.ARGUMENT),
            ([const.FUNCTION_CALL, const.COMMA, const.VALUE], const.ARGUMENT),
            ([const.VAR_AS, const.COMMA, const.VALUE], const.ARGUMENT),
            ([const.ARGUMENT, const.COMMA, const.VALUE], const.ARGUMENT),
            ([const.PRINT_ARGUMENT, const.COMMA, const.VALUE], const.PRINT_ARGUMENT),
            ([const.ENUMERABLE_OBJECT, const.COMMA, const.VALUE], const.ARGUMENT),
            ([const.PARAM, const.COMMA, const.VALUE], const.ARGUMENT),
            ([const.PRINT_STMT, const.COMMA, const.VALUE], const.PRINT_STMT)
        ], const.FUNCTION_CALL: [
            ([const.ID, const.COMMA, const.FUNCTION_CALL], const.ARGUMENT),
            ([const.VALUE, const.COMMA, const.FUNCTION_CALL], const.ARGUMENT),
            ([const.FUNCTION_CALL, const.COMMA, const.FUNCTION_CALL], const.ARGUMENT),
            ([const.VAR_AS, const.COMMA, const.FUNCTION_CALL], const.ARGUMENT),
            ([const.ARGUMENT, const.COMMA, const.FUNCTION_CALL], const.ARGUMENT),
            ([const.PRINT_ARGUMENT, const.COMMA, const.FUNCTION_CALL], const.PRINT_ARGUMENT),
            ([const.ENUMERABLE_OBJECT, const.COMMA, const.FUNCTION_CALL], const.ARGUMENT),
            ([const.PARAM, const.COMMA, const.FUNCTION_CALL], const.ARGUMENT),
            ([const.PRINT_STMT, const.COMMA, const.FUNCTION_CALL], const.PRINT_STMT)
        ], const.VAR_AS: [
            ([const.ID, const.COMMA, const.VAR_AS], const.ARGUMENT),
            ([const.VALUE, const.COMMA, const.VAR_AS], const.ARGUMENT),
            ([const.FUNCTION_CALL, const.COMMA, const.VAR_AS], const.ARGUMENT),
            ([const.VAR_AS, const.COMMA, const.VAR_AS], const.ARGUMENT),
            ([const.ARGUMENT, const.COMMA, const.VAR_AS], const.ARGUMENT),
            ([const.PRINT_ARGUMENT, const.COMMA, const.VAR_AS], const.PRINT_ARGUMENT),
            ([const.ENUMERABLE_OBJECT, const.COMMA, const.VAR_AS], const.ARGUMENT),
            ([const.PARAM, const.COMMA, const.VAR_AS], const.ARGUMENT)
        ], const.ARGUMENT: [
            ([const.ID, const.COMMA, const.ARGUMENT], const.ARGUMENT),
            ([const.VALUE, const.COMMA, const.ARGUMENT], const.ARGUMENT),
            ([const.FUNCTION_CALL, const.COMMA, const.ARGUMENT], const.ARGUMENT),
            ([const.VAR_AS, const.COMMA, const.ARGUMENT], const.ARGUMENT),
            ([const.ARGUMENT, const.COMMA, const.ARGUMENT], const.ARGUMENT),
            ([const.PRINT_ARGUMENT, const.COMMA, const.ARGUMENT], const.PRINT_ARGUMENT),
            ([const.ENUMERABLE_OBJECT, const.COMMA, const.ARGUMENT], const.ARGUMENT),
            ([const.PARAM, const.COMMA, const.ARGUMENT], const.ARGUMENT),
            ([const.PRINT_STMT, const.COMMA, const.ARGUMENT], const.PRINT_STMT)
        ], const.ENUMERABLE_OBJECT: [
            ([const.ID, const.COMMA, const.ENUMERABLE_OBJECT], const.ARGUMENT),
            ([const.VALUE, const.COMMA, const.ENUMERABLE_OBJECT], const.ARGUMENT),
            ([const.FUNCTION_CALL, const.COMMA, const.ENUMERABLE_OBJECT], const.ARGUMENT),
            ([const.VAR_AS, const.COMMA, const.ENUMERABLE_OBJECT], const.ARGUMENT),
            ([const.ARGUMENT, const.COMMA, const.ENUMERABLE_OBJECT], const.ARGUMENT),
            ([const.PRINT_ARGUMENT, const.COMMA, const.ENUMERABLE_OBJECT], const.PRINT_ARGUMENT),
            ([const.ENUMERABLE_OBJECT, const.COMMA, const.ENUMERABLE_OBJECT], const.ARGUMENT),
            ([const.PARAM, const.COMMA, const.ENUMERABLE_OBJECT], const.ARGUMENT),
            ([const.PRINT_STMT, const.COMMA, const.ENUMERABLE_OBJECT], const.PRINT_STMT)
        ], const.PARAM: [
            ([const.ID, const.COMMA, const.PARAM], const.ARGUMENT),
            ([const.VALUE, const.COMMA, const.PARAM], const.ARGUMENT),
            ([const.FUNCTION_CALL, const.COMMA, const.PARAM], const.ARGUMENT),
            ([const.VAR_AS, const.COMMA, const.PARAM], const.ARGUMENT),
            ([const.ARGUMENT, const.COMMA, const.PARAM], const.ARGUMENT),
            ([const.PRINT_ARGUMENT, const.COMMA, const.PARAM], const.PRINT_ARGUMENT),
            ([const.ENUMERABLE_OBJECT, const.COMMA, const.PARAM], const.ARGUMENT),
            ([const.PARAM, const.COMMA, const.PARAM], const.PARAM)
        ],
        const.ASSOCIATIVE_ARRAY_ARGUMENT: [
            ([const.ASSOCIATIVE_ARRAY_ARGUMENT, const.COMMA, const.ASSOCIATIVE_ARRAY_ARGUMENT],
             const.ASSOCIATIVE_ARRAY_ARGUMENT)
        ],
        const.ARRAY_ARGUMENT: [
            ([const.ARRAY_ARGUMENT, const.COMMA, const.ARRAY_ARGUMENT], const.ARRAY_ARGUMENT),
            ([const.ARGUMENT, const.COMMA, const.ARRAY_ARGUMENT], const.ARRAY_ARGUMENT)
        ],
        const.PRINT_ARGUMENT: [
            ([const.ID, const.COMMA, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.VALUE, const.COMMA, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.FUNCTION_CALL, const.COMMA, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.VAR_AS, const.COMMA, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.ARGUMENT, const.COMMA, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.PRINT_ARGUMENT, const.COMMA, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.ENUMERABLE_OBJECT, const.COMMA, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.PARAM, const.COMMA, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.PRINT_STMT, const.COMMA, const.PRINT_ARGUMENT], const.PRINT_STMT)
        ],
    },
    const.PRIORITY_FIVE: {
        const.ID: [
            ([const.ID, const.SEMI_COLON, const.ID], const.PRINT_ARGUMENT),
            ([const.VALUE, const.SEMI_COLON, const.ID], const.PRINT_ARGUMENT),
            ([const.FUNCTION_CALL, const.SEMI_COLON, const.ID], const.PRINT_ARGUMENT),
            ([const.VAR_AS, const.SEMI_COLON, const.ID], const.PRINT_ARGUMENT),
        ],
        const.VALUE: [
            ([const.VALUE, const.SEMI_COLON, const.VALUE], const.PRINT_ARGUMENT),
            ([const.ID, const.SEMI_COLON, const.VALUE], const.PRINT_ARGUMENT),
            ([const.FUNCTION_CALL, const.SEMI_COLON, const.VALUE], const.PRINT_ARGUMENT),
            ([const.VAR_AS, const.SEMI_COLON, const.VALUE], const.PRINT_ARGUMENT),
        ],
        const.ARGUMENT: [
            ([const.VALUE, const.SEMI_COLON, const.ARGUMENT], const.PRINT_ARGUMENT),
            ([const.FUNCTION_CALL, const.SEMI_COLON, const.ARGUMENT], const.PRINT_ARGUMENT)
        ],
        const.FUNCTION_CALL: [
            ([const.FUNCTION_CALL, const.SEMI_COLON, const.FUNCTION_CALL], const.PRINT_ARGUMENT),
            ([const.ID, const.SEMI_COLON, const.FUNCTION_CALL], const.PRINT_ARGUMENT),
            ([const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL], const.PRINT_ARGUMENT),
            ([const.VAR_AS, const.SEMI_COLON, const.FUNCTION_CALL], const.PRINT_ARGUMENT),
        ],
        const.VAR_AS: [
            ([const.VAR_AS, const.SEMI_COLON, const.VAR_AS], const.PRINT_ARGUMENT),
            ([const.ID, const.SEMI_COLON, const.VAR_AS], const.PRINT_ARGUMENT),
            ([const.VALUE, const.SEMI_COLON, const.VAR_AS], const.PRINT_ARGUMENT),
            ([const.FUNCTION_CALL, const.SEMI_COLON, const.VAR_AS], const.PRINT_ARGUMENT)
        ],
        const.ENUMERABLE_OBJECT: [
            ([const.ENUMERABLE_OBJECT, const.SEMI_COLON, const.ENUMERABLE_OBJECT], const.PRINT_ARGUMENT),
            ([const.FUNCTION_CALL, const.SEMI_COLON, const.ENUMERABLE_OBJECT], const.PRINT_ARGUMENT),
            ([const.ID, const.SEMI_COLON, const.ENUMERABLE_OBJECT], const.PRINT_ARGUMENT),
            ([const.VALUE, const.SEMI_COLON, const.ENUMERABLE_OBJECT], const.PRINT_ARGUMENT),
            ([const.VAR_AS, const.SEMI_COLON, const.ENUMERABLE_OBJECT], const.PRINT_ARGUMENT),
        ],
        const.PARAM: [
            ([const.PARAM, const.SEMI_COLON, const.PARAM], const.PRINT_ARGUMENT)
        ],
        const.PRINT_ARGUMENT: [
            ([const.FUNCTION_CALL, const.SEMI_COLON, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.ID, const.SEMI_COLON, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.VAR_AS, const.SEMI_COLON, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
        ]
    },
    const.PRIORITY_SIX: {
        const.ID: [
            ([const.ID, const.OPERATOR, const.ID], const.VALUE),
            ([const.VALUE, const.OPERATOR, const.ID], const.VALUE),
            ([const.FUNCTION_CALL, const.OPERATOR, const.ID], const.VALUE),
            ([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.ID], const.FOR_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.ID], const.FOR_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.ID], const.FOR_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.ID], const.FOR_STMT),
            ([const.WHILE, const.ID], const.WHILE_STMT),
            ([const.PRINT_KEYWORD, const.ID], const.PRINT_STMT),
            ([const.FOR_EACH, const.ID, const.IN, const.ID], const.FOR_EACH_STMT),
            ([const.IF, const.ID], const.IF_STMT),
            ([const.VALUE, const.COMPARISON_OPERATOR, const.ID], const.CONDITION),
            ([const.ID, const.COMPARISON_OPERATOR, const.ID], const.CONDITION),
            ([const.FUNCTION_CALL, const.COMPARISON_OPERATOR, const.ID], const.CONDITION),
            ([const.ANONYMOUS_FUNCTION_DECLARATION, const.COMPARISON_OPERATOR, const.ID], const.CONDITION),
            ([const.ELSE_IF, const.ID], const.ELSE_IF_STMT),
            ([const.RETURN_STMT, const.ID], const.RETURN_STMT),
        ],
        const.VALUE: [
            ([const.FOR, const.VAR_AS, const.TO, const.VALUE], const.FOR_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.VALUE], const.FOR_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.VALUE], const.FOR_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.VALUE], const.FOR_STMT),
            ([const.FOR_EACH, const.ID, const.IN, const.VALUE], const.FOR_EACH_STMT),
            ([const.IF, const.VALUE], const.IF_STMT),
            ([const.VALUE, const.COMPARISON_OPERATOR, const.VALUE], const.CONDITION),
            ([const.ID, const.COMPARISON_OPERATOR, const.VALUE], const.CONDITION),
            ([const.FUNCTION_CALL, const.COMPARISON_OPERATOR, const.VALUE], const.CONDITION),
            ([const.ANONYMOUS_FUNCTION_DECLARATION, const.COMPARISON_OPERATOR, const.VALUE], const.CONDITION),
            ([const.ELSE_IF, const.VALUE], const.ELSE_IF_STMT),
            ([const.RETURN_STMT, const.VALUE], const.RETURN_STMT),
            ([const.WHILE, const.VALUE], const.WHILE_STMT),
            ([const.PRINT_KEYWORD, const.VALUE], const.PRINT_STMT),

        ],
        const.FUNCTION_CALL: [
            ([const.ID, const.OPERATOR, const.FUNCTION_CALL], const.VALUE),
            ([const.VALUE, const.OPERATOR, const.FUNCTION_CALL], const.VALUE),
            ([const.FUNCTION_CALL, const.OPERATOR, const.FUNCTION_CALL], const.VALUE),
            ([const.FUNCTION, const.FUNCTION_CALL], const.FUNCTION_DECLARATION),
            ([const.SUB, const.FUNCTION_CALL], const.FUNCTION_DECLARATION),
            ([const.FOR_EACH, const.ID, const.IN, const.FUNCTION_CALL], const.FOR_EACH_STMT),
            ([const.IF, const.FUNCTION_CALL], const.IF_STMT),
            ([const.VALUE, const.COMPARISON_OPERATOR, const.FUNCTION_CALL], const.CONDITION),
            ([const.ID, const.COMPARISON_OPERATOR, const.FUNCTION_CALL], const.CONDITION),
            ([const.FUNCTION_CALL, const.COMPARISON_OPERATOR, const.FUNCTION_CALL], const.CONDITION),
            ([const.ANONYMOUS_FUNCTION_DECLARATION, const.COMPARISON_OPERATOR, const.FUNCTION_CALL], const.CONDITION),
            ([const.ELSE_IF, const.FUNCTION_CALL], const.ELSE_IF_STMT),
            ([const.RETURN_STMT, const.FUNCTION_CALL], const.RETURN_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.FUNCTION_CALL], const.FOR_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.FUNCTION_CALL], const.FOR_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL], const.FOR_STMT),
            ([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.FUNCTION_CALL], const.FOR_STMT),
            ([const.WHILE, const.FUNCTION_CALL], const.WHILE_STMT),
            ([const.PRINT_KEYWORD, const.FUNCTION_CALL], const.PRINT_STMT),
        ],
        const.TYPE: [
            ([const.FUNCTION, const.FUNCTION_CALL, const.AS, const.TYPE], const.FUNCTION_DECLARATION),
            ([const.ID, const.AS, const.TYPE], const.PARAM),
            ([const.VAR_AS, const.AS, const.TYPE], const.PARAM),
            ([const.ANONYMOUS_FUNCTION_DECLARATION, const.AS, const.TYPE], const.ANONYMOUS_FUNCTION_DECLARATION)
        ],
        const.VAR_AS: [
            ([const.WHILE, const.VAR_AS], const.WHILE_STMT),
            ([const.PRINT_KEYWORD, const.VAR_AS], const.PRINT_STMT),
            ([const.IF, const.VAR_AS], const.IF_STMT),
            ([const.ELSE_IF, const.VAR_AS], const.ELSE_IF_STMT),
            ([const.RETURN_STMT, const.VAR_AS], const.RETURN_STMT),
            ([const.VAR_AS, const.AND, const.VAR_AS], const.CONDITION),
            ([const.VAR_AS, const.OR, const.VAR_AS], const.CONDITION),
            ([const.CONDITION, const.AND, const.VAR_AS], const.CONDITION),
            ([const.CONDITION, const.OR, const.VAR_AS], const.CONDITION)
        ],
        const.CLOSE_PARENTHESIS: [
            ([const.FUNCTION, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS], const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.FUNCTION, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.FUNCTION, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.FUNCTION, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.FUNCTION, const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.FUNCTION, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.SUB, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS], const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.SUB, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.SUB, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.SUB, const.OPEN_PARENTHESIS, const.PARAM, const.ARGUMENT, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.SUB, const.OPEN_PARENTHESIS, const.ID, const.ARGUMENT, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.SUB, const.OPEN_PARENTHESIS, const.VALUE, const.ARGUMENT, const.CLOSE_PARENTHESIS],
             const.ANONYMOUS_FUNCTION_DECLARATION),
            ([const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS], const.ID),
            ([const.OPEN_PARENTHESIS, const.VAR_AS, const.CLOSE_PARENTHESIS], const.VAR_AS)
        ],
        const.CLOSE_CURLY_BRACKET: [
            ([const.OPEN_CURLY_BRACKET, const.CLOSE_CURLY_BRACKET], const.ENUMERABLE_OBJECT),
            ([const.OPEN_CURLY_BRACKET, const.ASSOCIATIVE_ARRAY_ARGUMENT, const.CLOSE_CURLY_BRACKET],
             const.ENUMERABLE_OBJECT)
        ],


        const.ARGUMENT: [
            ([const.ARRAY_ARGUMENT, const.ARGUMENT], const.ARRAY_ARGUMENT),
            ([const.PRINT_KEYWORD, const.ARGUMENT], const.PRINT_STMT),
            ([const.ARGUMENT, const.ARGUMENT], const.ARGUMENT),
        ],
        const.PRINT_ARGUMENT: [
            ([const.ARRAY_ARGUMENT, const.PRINT_ARGUMENT], const.ARRAY_ARGUMENT),
            ([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], const.PRINT_STMT),
            ([const.ARGUMENT, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
            ([const.PRINT_ARGUMENT, const.ARGUMENT], const.PRINT_ARGUMENT),
            ([const.PRINT_ARGUMENT, const.PRINT_ARGUMENT], const.PRINT_ARGUMENT),
        ],
        const.ENUMERABLE_OBJECT: [
            ([const.PRINT_KEYWORD, const.ENUMERABLE_OBJECT], const.PRINT_STMT),
            ([const.RETURN_STMT, const.ENUMERABLE_OBJECT], const.RETURN_STMT),
        ],
        const.ANONYMOUS_FUNCTION_DECLARATION: [
            ([const.IF, const.ANONYMOUS_FUNCTION_DECLARATION], const.IF_STMT),
            ([const.VALUE, const.COMPARISON_OPERATOR, const.ANONYMOUS_FUNCTION_DECLARATION], const.CONDITION),
            ([const.ID, const.COMPARISON_OPERATOR, const.ANONYMOUS_FUNCTION_DECLARATION], const.CONDITION),
            ([const.FUNCTION_CALL, const.COMPARISON_OPERATOR, const.ANONYMOUS_FUNCTION_DECLARATION], const.CONDITION),
            ([const.ANONYMOUS_FUNCTION_DECLARATION, const.COMPARISON_OPERATOR, const.ANONYMOUS_FUNCTION_DECLARATION],
             const.CONDITION),
            ([const.ELSE_IF, const.ANONYMOUS_FUNCTION_DECLARATION], const.ELSE_IF_STMT),
            ([const.RETURN_STMT, const.ANONYMOUS_FUNCTION_DECLARATION], const.RETURN_STMT),
            ([const.VALUE, const.EQUALS, const.ANONYMOUS_FUNCTION_DECLARATION], const.CONDITION),
            ([const.FUNCTION_CALL, const.EQUALS, const.ANONYMOUS_FUNCTION_DECLARATION], const.CONDITION),
            ([const.ANONYMOUS_FUNCTION_DECLARATION, const.EQUALS, const.ANONYMOUS_FUNCTION_DECLARATION],
             const.CONDITION),
        ],
        const.THEN: [
            ([const.IF, const.CONDITION, const.THEN], const.IF_STMT),
            ([const.IF_STMT, const.THEN], const.IF_STMT),
            ([const.ELSE_IF, const.CONDITION, const.THEN], const.ELSE_IF_STMT),
            ([const.ELSE_IF_STMT, const.THEN], const.ELSE_IF_STMT),
        ],
        const.CONDITION: [
            ([const.CONDITION, const.AND, const.CONDITION], const.CONDITION),
            ([const.CONDITION, const.OR, const.CONDITION], const.CONDITION),
            ([const.IF, const.CONDITION], const.IF_STMT),
            ([const.ELSE_IF, const.CONDITION], const.ELSE_IF_STMT),
            ([const.VAR_AS, const.AND, const.CONDITION], const.CONDITION),
            ([const.VAR_AS, const.OR, const.CONDITION], const.CONDITION)
        ],
        const.WHILE: [([const.EXIT, const.WHILE], const.EXIT)],
        const.FOR: [([const.EXIT, const.FOR], const.EXIT)],
    }

}
RULES = rule_builder.load_grammar_rules(RULES_LIST)
