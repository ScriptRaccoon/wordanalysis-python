"""
Module for analyzing the word counts inside of a text document.
It counts how many times each word appears, sorts the
results by decreasing amounts, and saves it to a file.
"""


def clean(txt: str) -> str:
    """
    Removes non-alphanumeric characters from a string and
    makes it lowercase.
    """
    return "".join(e for e in txt if e.isalnum()).lower()


def generate_word_dict(file_name: str) -> dict[str, int]:
    """
    Generates the word dictionary from a text file.

    Arguments:
        file_name: name of the text file to be read

    Returns:
        Dictionary whose keys are all the cleaned words
        and whose values are their amounts in the file.
    """
    word_dict = {}
    with open(file_name, "r", encoding="utf8") as file:
        for line in file:
            words_in_line = map(clean, line.split(" "))
            for word in words_in_line:
                if len(word) == 0:
                    continue
                if not word in word_dict:
                    word_dict[word] = 0
                word_dict[word] += 1

    return word_dict


def generate_word_list(file_name: str) -> list[tuple[str, int]]:
    """
    Generates the word list from a text file.

    Arguments:
        file_name: name of the text file to be read

    Returns:
        List of tuples (w,a) consisting of a word w and its amount a
        in the text file, sorted decreasing by amount.
    """
    word_dict = generate_word_dict(file_name)
    word_list = list(word_dict.items())
    word_list.sort(key=lambda t: t[1], reverse=True)
    return word_list


def save_word_list(word_list: list[tuple[str, int]], file_name: str) -> None:
    """
    Saves the word list to a file.

    Arguments:
        word_list: the previously generated word list
        file_name: the name of the file to be written
    """
    with open(file_name, "w", encoding="utf8") as file:
        for word, amount in word_list:
            file.write(f"{word}: {amount}\n")


words = generate_word_list("input.txt")
save_word_list(words, "input_analysis.txt")
