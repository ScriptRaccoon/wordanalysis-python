"""
Unit tests for wordanalyser.py
Requires pytest and pytest-mock
"""

# pylint: disable=missing-function-docstring

import wordanalyser
from unittest.mock import patch, mock_open


def test_clean():
    assert wordanalyser.clean(" U V W  ") == "uvw"
    assert wordanalyser.clean("a b cd e ") == "abcde"


def test_add_word():
    common_words = ["i", "am", "ok"]
    word_dict = {"hello": 10, "there": 2}
    wordanalyser.add_word("", word_dict, common_words)
    assert word_dict == {"hello": 10, "there": 2}
    wordanalyser.add_word("hello", word_dict, common_words)
    assert word_dict == {"hello": 11, "there": 2}
    wordanalyser.add_word("ok", word_dict, common_words)
    assert word_dict == {"hello": 11, "there": 2}
    wordanalyser.add_word("band", word_dict, common_words)
    assert word_dict == {"hello": 11, "there": 2, "band": 1}


def test_add_line():
    common_words = ["i", "am", "ok"]
    word_dict = {}
    wordanalyser.process_line("This works", word_dict, common_words)
    assert word_dict == {"this": 1, "works": 1}
    wordanalyser.process_line("and works and I am ok", word_dict, common_words)
    assert word_dict == {"this": 1, "works": 2, "and": 2}


def test_add_summary():
    word_list = [("hello", 400), ("there", 100), ("ok", 50)]
    summary = (
        "3 non-common words have been found in input.txt.\n"
        + 'The most popular word is "hello" with 400 occurrences.\n'
        + "The whole list has been written to the file output.txt."
    )
    assert wordanalyser.get_summary(word_list, "input.txt", "output.txt") == summary


def test_get_common_words():
    mock_words = "i\nam\nOK"
    with patch("builtins.open", mock_open(read_data=mock_words)):
        assert wordanalyser.get_common_words() == ["i", "am", "ok"]


def test_get_word_dict():
    mock_text = "This is a - sample - text.\nI hope this will work.\nok."
    common_words = ["i", "am", "ok", "a", "is", "will"]
    expected_dict = {"this": 2, "sample": 1, "text": 1, "hope": 1, "work": 1}
    with patch("builtins.open", mock_open(read_data=mock_text)):
        assert (
            wordanalyser.generate_word_dict("sample.txt", common_words) == expected_dict
        )


def test_generate_word_list(mocker):
    gen_dict_mock = mocker.patch("wordanalyser.generate_word_dict")
    gen_dict_mock.return_value = {"word1": 60, "word2": 10, "word3": 30, "word4": 50}
    expected_list = [("word1", 60), ("word4", 50), ("word3", 30), ("word2", 10)]
    assert wordanalyser.generate_word_list("does-not-matter.txt") == expected_list
