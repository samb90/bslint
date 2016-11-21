import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestIfParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_if_with_function_call_and_value_id(self):
        self.common.match_statement(const.IF_STMT, "if func_name(msg) = \"roVideoPlayerEvent\"")

    def test_if_with_var_as_id(self):
        self.common.match_statement(const.IF_STMT, "if x = 3")

    def test_if_with_function_call_id(self):
        self.common.match_statement(const.IF_STMT, "if test(param)")

    def test_if_with_complex_function_call(self):
        self.common.match_statement(const.IF_STMT, "if msg.isFullResult()")

    def test_if_with_value(self):
        self.common.match_statement(const.IF_STMT, "if msg.isFullResult()")

    def test_if_with_value_equals_value(self):
        self.common.match_statement(const.IF_STMT, "if 3 = 3")

    def test_if_with_value_equals_id(self):
        self.common.match_statement(const.IF_STMT, "if 3 = x")

    def test_if_with_value_equals_function_call(self):
        self.common.match_statement(const.IF_STMT, "if 3 = test()")

    def test_if_with_numeric_value(self):
        self.common.match_statement(const.IF_STMT, "if 3")

    def test_if_with_id(self):
        self.common.match_statement(const.IF_STMT, "if x")

    def test_if_with_anonymous_function(self):
        self.common.match_statement(const.IF_STMT, "if Function()")

    def test_if_with_function_call_and_value_id_then(self):
        self.common.match_statement(const.IF_STMT, "if func_name(msg) = \"roVideoPlayerEvent\" then")

    def test_if_with_var_as_id_then(self):
        self.common.match_statement(const.IF_STMT, "if x = 3 then")

    def test_else_if_with_value_equals_id(self):
        self.common.match_statement(const.ELSE_IF_STMT, "else if 3 = x")

    def test_else_if_with_numeric_value(self):
        self.common.match_statement(const.ELSE_IF_STMT, "else if 3")

    def test_else_if_with_id(self):
        self.common.match_statement(const.ELSE_IF_STMT, "else if x")

    def test_else_if_with_anonymous_function(self):
        self.common.match_statement(const.ELSE_IF_STMT, "else if Function()")

    def test_if_with_value_equals_value_then(self):
        self.common.match_statement(const.ELSE_IF_STMT, "else if 3 = 3 then")

    def test_if_with_value_equals_id_then(self):
        self.common.match_statement(const.ELSE_IF_STMT, "else if 3 = x then")

    def test_if_with_numeric_value_then(self):
        self.common.match_statement(const.ELSE_IF_STMT, "else if 3 then")

    def test_if_then_no_end_if_func_call(self):
        self.common.match_statement(const.IF_BLOCK_STMT, "if requiresUpdate then showRequiresUpdateScreen()")

    def test_else_if_then_no_end_if_func_call(self):
        self.common.match_statement(const.IF_BLOCK_STMT, "elseif requiresUpdate then showRequiresUpdateScreen()")

    def test_else_if_then_no_end_if_var_as(self):
        self.common.match_statement(const.IF_BLOCK_STMT, "elseif requiresUpdate then c = 3")

    def test_if_then_no_end_if_var_as(self):
        self.common.match_statement(const.IF_BLOCK_STMT, "if requiresUpdate then c = 3")

    def test_else(self):
        self.common.match_statement(const.ELSE_STMT, "else")

    def test_if_with_function_declaration_fails(self):
        self.common.status_error("if function x()")

    def test_if_with_print_fails(self):
        self.common.status_error("if print x")

    def test_else_if_with_function_declaration_fails(self):
        self.common.status_error("else if +")

    def test_else_if_with_print_fails(self):
        self.common.status_error("else if =")
