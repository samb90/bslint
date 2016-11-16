import unittest
import bslint.lexer.handlers.regex_handler as regex_handler
from bslint.lexer.handlers.styling_handler import StylingHandler as StylingHandler
from bslint.lexer.lexer import Lexer as Lexer
import bslint.lexer.handlers.styling_dispatcher as styling_dispatcher


class TestColon(unittest.TestCase):

    def test_statement_ends_with_colon(self):
        identifier = ":"
        regex_match = regex_handler.find_match(identifier)
        styling_handler = StylingHandler(identifier, Lexer())
        styling_handler.dispatcher = styling_dispatcher.Dispatcher(styling_handler)
        styling_handler.apply_styling(regex_match)
        styling_handler.check_end_of_statement()
        self.assertTrue(styling_handler.end_of_statement)

    def test_statement_ends_with_colon_no_change_line(self):
        identifier = "myVar = value: otherVar = otherValue"
        result = Lexer().lex(identifier)
        self.assertEqual(1, result["Tokens"].pop().line_number)
