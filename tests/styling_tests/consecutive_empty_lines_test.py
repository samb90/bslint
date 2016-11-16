import unittest
import os

import bslint
import bslint.messages.handler as error
import bslint.messages.error_constants as err_const
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from filepaths import EMPTY_LINES_TEST_FILES_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestConsecutiveEmptyLines(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.single_empty_lines_config_path = os.path.join(TESTS_CONFIG_PATH,
                                                          'empty_lines/single-empty-lines-config.json')
        cls.double_empty_lines_config_path = os.path.join(TESTS_CONFIG_PATH,
                                                          'empty_lines/double-empty-lines-config.json')
        cls.common = Common()

    def test_no_empty_lines(self):
        bslint.load_config_file(user_filepath=self.single_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        no_empty_lines_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH, 'no-empty-lines.brs')
        file_name = no_empty_lines_file_path
        self.common.lex_file([], file_name)

    def test_one_consecutive_empty_line(self):
        bslint.load_config_file(user_filepath=self.single_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        one_consecutive_empty_line_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH,
                                                            'one-consecutive-empty-line.brs')
        file_name = one_consecutive_empty_line_file_path
        self.common.lex_file([], file_name)

    def test_only_empty_lines(self):
        bslint.load_config_file(user_filepath=self.single_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        only_empty_lines_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH, 'only-empty-lines.brs')
        file_name = only_empty_lines_file_path
        expected = [
            error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [1, 2]),
            error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3]),
            error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [1, 4])]
        self.common.lex_file(expected, file_name)

    def test_empty_lines_at_end(self):
        bslint.load_config_file(user_filepath=self.single_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        empty_lines_at_end_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH, 'empty-lines-at-end.brs')
        file_name = empty_lines_at_end_file_path
        expected = [error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3]),
                    error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [1, 4])]
        self.common.lex_file(expected, file_name)

    def test_empty_lines_at_start(self):
        bslint.load_config_file(user_filepath=self.single_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        empty_lines_at_start_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH, 'empty-lines-at-start.brs')
        file_name = empty_lines_at_start_file_path
        expected = [error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [1, 2]),
                    error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3])]
        self.common.lex_file(expected, file_name)

    def test_empty_lines_in_middle(self):
        bslint.load_config_file(user_filepath=self.single_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        empty_lines_in_middle_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH, 'empty-lines-in-middle.brs')
        file_name = empty_lines_in_middle_file_path
        expected = [error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [1, 4])]
        self.common.lex_file(expected, file_name)

    def test_comment_not_empty_lines(self):
        bslint.load_config_file(user_filepath=self.single_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        comment_not_empty_lines_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH, 'comment-not-empty-lines.brs')
        file_name = comment_not_empty_lines_file_path
        self.common.lex_file([], file_name)

    def test_multiple_tokens_and_empty_lines(self):
        bslint.load_config_file(user_filepath=self.single_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        multiple_tokens_and_empty_lines_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH,
                                                                 'multiple-tokens-and-empty-lines.brs')
        file_name = multiple_tokens_and_empty_lines_file_path
        expected = [error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3])]
        self.common.lex_file(expected, file_name)

    def test_empty_lines_in_middle_custom_config(self):
        bslint.load_config_file(user_filepath=self.double_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        empty_lines_in_middle_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH, 'empty-lines-in-middle.brs')
        file_name = empty_lines_in_middle_file_path
        self.common.lex_file([], file_name)

    def test_only_empty_lines_custom_config(self):
        bslint.load_config_file(user_filepath=self.double_empty_lines_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        only_empty_lines_file_path = os.path.join(EMPTY_LINES_TEST_FILES_PATH, 'only-empty-lines.brs')
        file_name = only_empty_lines_file_path
        expected = [error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [2, 3]),
                    error.get_error_msg(err_const.CONSECUTIVE_EMPTY_LINES, [2, 4])]
        self.common.lex_file(expected, file_name)
