"""
Unit tests for wordanalyser.py
"""

# pylint: disable=missing-function-docstring

import wordanalyser


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
