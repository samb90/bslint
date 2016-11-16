from bslint.messages import builder as build

ERROR = "ERROR"
WARNING = "WARNING"

TRAILING_COMMA_IN_OBJECTS = "TRAILING_COMMA_IN_OBJECTS"
COMMAS_IN_OBJECTS = "COMMAS_IN_OBJECTS"
LINE_LENGTH = "LINE_LENGTH"
FILE_ENCODING = "FILE_ENCODING"
CONSECUTIVE_EMPTY_LINES = "CONSECUTIVE_EMPTY_LINES"
UPPERCASE_VARIABLE = "UPPERCASE_VARIABLE"
TAB_INDENTATION_ERROR = "TAB_INDENTATION_ERROR"
TAB_AND_SPACES = "TAB_AND_SPACES"
TYPO_IN_CODE = "TYPO_IN_CODE"
TRACEABLE_CODE = "TRACEABLE_CODE"
NON_CONVENTIONAL_TODO = "NON_CONVENTIONAL_TODO"
COMMENTS_NOT_ALLOWED = "COMMENTS_NOT_ALLOWED"
NO_RETURN_AND_PARAMETERS_TYPES = "NO_RETURN_AND_PARAMETERS_TYPES"
NOT_CAPITALISED_VARIABLE_NAMES = "NOT_CAPITALISED_VARIABLE_NAMES"
NO_SPACE_AROUND_OPERATORS = "NO_SPACE_AROUND_OPERATORS = {NO_SPACE_AROUND_OPERATORS"
NO_SPACE_BETWEEN_METHOD_AND_PARAMETERS = "NO_SPACE_BETWEEN_METHOD_AND_PARAMETERS"
UNMATCHED_QUOTATION_MARK = "UNMATCHED_QUOTATION_MARK"
NON_CONVENTIONAL_TODO_AND_NO_COMMENTS = "NON_CONVENTIONAL_TODO_AND_NO_COMMENTS"
NO_TODOS = "NO_TODOS"
METHOD_DECLARATION_SPACING = "METHOD_DECLARATION_SPACING"
UNMATCHED_TOKEN = "UNMATCHED_TOKEN"
NO_MATCH_FOUND = "NO_MATCH_FOUND"
STMT_PARSING_FAILED = "STMT_PARSING_FAILED"
PROGRAM_PARSING_FAILED = "PROGRAM_PARSING_FAILED"
NO_SUCH_KEY = "NO_SUCH_KEY"

MESSAGE_TABLE = {
    TRAILING_COMMA_IN_OBJECTS: build.Message(WARNING + ": Trailing comma in object literal. Line number: {}"),
    COMMAS_IN_OBJECTS: build.Message(WARNING + ": Object literal name value-pair missing comma. Line number: {}"),
    LINE_LENGTH: build.Message(WARNING + ": Line length exceeds {} number of characters. Line number: {}"),
    FILE_ENCODING: build.Message(WARNING + ": Your files should conform to {} encoding"),
    CONSECUTIVE_EMPTY_LINES: build.Message(
        WARNING + ": Cannot have more than {} consecutive empty lines. Line number: {}"),
    UPPERCASE_VARIABLE: build.Message(WARNING + ": Variables should begin with a lowercase letter: line number: {}"),
    TAB_INDENTATION_ERROR: build.Message(WARNING + ": Tab indentation should be set to {} spaces. Line number: {}"),
    TAB_AND_SPACES: build.Message(WARNING + ": Invalid indentation, you must indent with tabs. Line number: {}"),
    TYPO_IN_CODE: build.Message(WARNING + ": You have spelling mistakes in your code. Line number: {}"),
    TRACEABLE_CODE: build.Message(WARNING + ": Print statements not allowed. Line number: {}"),
    NON_CONVENTIONAL_TODO_AND_NO_COMMENTS: build.Message(
        WARNING + ": comments must be TODOs and must follow convention. Line number: {}"),
    COMMENTS_NOT_ALLOWED: build.Message(WARNING + ": No comments allowed. Line number: {}"),
    NO_RETURN_AND_PARAMETERS_TYPES: build.Message(
        WARNING + ": No return and parameter types declared. Line number: {}"),
    NOT_CAPITALISED_VARIABLE_NAMES: build.Message(WARNING + ": Variable types must be capitalised. Line number: {}"),
    NO_SPACE_AROUND_OPERATORS: build.Message(
        WARNING + ": Operators must be surrounded by {} space(s). Line number: {}"),
    NO_SPACE_BETWEEN_METHOD_AND_PARAMETERS: build.Message(
        WARNING + ": You must put a space between method name and parameter list. Line number: {}"),
    UNMATCHED_QUOTATION_MARK: build.Message(ERROR + ": You have unmatched quotation marks at {} on line number: {}"),
    NON_CONVENTIONAL_TODO: build.Message(WARNING + ": TODOs must follow convention. Line number: {}"),
    NO_TODOS: build.Message(WARNING + ": comments must not be TODOs. Line number: {}"),
    METHOD_DECLARATION_SPACING: build.Message(WARNING + ": The spacing on the method declaration is incorrect: {}"),
    UNMATCHED_TOKEN: build.Message(ERROR + ": Unmatched tokens, expected {}, but got {}"),
    STMT_PARSING_FAILED: build.Message(ERROR + ": Parsing statement failed. Line number: {}"),
    PROGRAM_PARSING_FAILED: build.Message(ERROR + ": Parsing program failed. Line number: {}")
}
