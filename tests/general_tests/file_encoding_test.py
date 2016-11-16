import os
import unittest

import bslint
import bslint.messages.error_constants as err_const
import bslint.lexer.commands as commands
from bslint.interface_handler import InterfaceHandler as InterfaceHandler
from filepaths import TESTS_CONFIG_PATH
from filepaths import TESTS_RESOURCES_PATH
from filepaths import TEST_CONFIG_FILE_PATH


class TestEncodingCheck(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'
    TOKEN = "token"
    TYPE = "type"
    LINE_NUMBER = "line_number"

    @classmethod
    def setUpClass(cls):
        cls.ascii_encoding_config_path = os.path.join(TESTS_CONFIG_PATH, 'file_encoding/ASCII-encoding-config.json')
        cls.ascii_chars_file_path = os.path.join(TESTS_RESOURCES_PATH, 'encoding_test_files/ASCII-chars.brs')
        cls.non_ascii_chars_file_path = os.path.join(TESTS_RESOURCES_PATH, 'encoding_test_files/NON-ASCII-chars.brs')
        cls.utf8_encoding_config_path = os.path.join(TESTS_CONFIG_PATH, 'file_encoding/UTF8-encoding-config.json')

    def test_ascii_chars(self):
        bslint.load_config_file(user_filepath=self.ascii_encoding_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        file_path = self.ascii_chars_file_path
        result = commands.check_file_encoding(file_path)
        expected = None
        self.assertEqual(expected, result)

    def test_non_ascii_chars(self):
        bslint.load_config_file(user_filepath=self.ascii_encoding_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        file_path = self.non_ascii_chars_file_path
        result = commands.check_file_encoding(file_path)
        self.assertEqual(err_const.FILE_ENCODING, result['error_key'])

    def test_utf_8_chars(self):
        bslint.load_config_file(user_filepath=self.utf8_encoding_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        file_path = self.non_ascii_chars_file_path
        result = commands.check_file_encoding(file_path)
        expected = None
        self.assertEqual(expected, result)

    def test_file_reader(self):
        bslint.load_config_file(user_filepath=self.ascii_encoding_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        file_path = self.ascii_chars_file_path
        fo = open(file_path, "r+")
        str_to_lex = fo.read()
        result = InterfaceHandler.file_reader(file_path)
        expected = {"invalid_encoding": None, "file_content": str_to_lex}
        self.assertEqual(expected, result)

    def test_file_reader_no_encoding_check(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        file_path = self.ascii_chars_file_path
        fo = open(file_path, "r+")
        str_to_lex = fo.read()
        result = InterfaceHandler.file_reader(file_path)
        expected = {"invalid_encoding": None, "file_content": str_to_lex}
        self.assertEqual(expected, result)
