import unittest
from bslint.lexer.lexer import Lexer as Lexer
from tests.resources.common.test_methods import CommonMethods as Common


class TestEndOfMultiLineStatement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test__statement__ends__with__curly__brace(self):
        identifier = "myVar = {\n"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertFalse(lexer.handle_style.end_of_statement)

    def test_statement_with_2curly_braces(self):
        identifier = "myVar = {\n{\n}"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertFalse(lexer.handle_style.end_of_statement)

    def test_basic_statement_counting(self):
        expected = 2
        self.common.lex_identifier(expected, "c = 3\n x = 4")

    def test_statement_counter_with_colon(self):
        expected = 2
        self.common.lex_identifier(expected, "c = 3: x = 4")

    def test_statement_with_2matching_curly_braces(self):
        expected = 1
        self.common.lex_identifier(expected, "myVar = {\n{\n}\n}")

    def test_statement_with_2matchin_curly_braces(self):
        expected = 1
        self.common.lex_identifier(expected, "myVar = {\na: {b:\"Test String\",\n c:\"Test String\"}\n}")
