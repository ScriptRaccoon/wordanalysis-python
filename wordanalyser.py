"""
Module for analyzing the word counts inside of a text document.
It counts how many times each word appears, sorts the
results by decreasing amounts, and saves it to a file.
"""


def clean(txt: str) -> str:
    """
    Removes non-alphanumeric characters from a string and
    makes it lowercase.

    Arguments:
        txt: any string.

    Returns:
        A cleaned version of the string.
    """
    return "".join(char for char in txt if char.isalnum()).lower()


def add_word(word: str, word_dict: dict[str, int]) -> None:
    """
    Adds a word to the dictionary. Changes the dictionary in place.

    Arguments:
        word: any string
        word_dict: a dictionary which has the updated amount of the word
    """
    if len(word) == 0:
        return
    if not word in word_dict:
        word_dict[word] = 0
    word_dict[word] += 1


def process_line(line: str, word_dict: dict[str, int]) -> None:
    """
    Adds all words inside of a line to a dictionary. Changes the dictionary in place.

    Arguments:
        word: any string
        word_dict: a dictionary which has the updated amount of the words
    """
    words_in_line = map(clean, line.split(" "))
    for word in words_in_line:
        add_word(word, word_dict)


def generate_word_dict(file_name: str) -> dict[str, int]:
    """
    Generates the word dictionary from a text file.

    Arguments:
        file_name: name of the text file to be read.

    Returns:
        A dictionary which stores the amount all words
    """
    word_dict: dict[str, int] = {}

    with open(file_name, "r", encoding="utf8") as file:
        for line in file:
            process_line(line, word_dict)

    return word_dict


def generate_word_list(file_name: str) -> list[tuple[str, int]]:
    """
    Generates the word list from a text file.

    Arguments:
        file_name: name of the text file to be read.

    Returns:
        List of tuples (w,a) consisting of a word w and its amount a
        in the text file. These are sorted by decreasing amount.
    """
    word_dict = generate_word_dict(file_name)
    word_list = list(word_dict.items())
    return sorted(word_list, key=lambda t: t[1], reverse=True)


def save_word_list(word_list: list[tuple[str, int]], file_name: str) -> None:
    """
    Saves the word list to a file.

    Arguments:
        word_list: a list of words with their amounts
        file_name: the name of the file to be written.
    """
    with open(file_name, "w", encoding="utf8") as file:
        for word, amount in word_list:
            file.write(f"{word}: {amount}\n")


def main():
    """
    Generates the word list from the sample file (input.txt)
    and writes it to another file (input_analysis.txt)
    """
    word_list = generate_word_list("input.txt")
    save_word_list(word_list, "input_analysis.txt")


if __name__ == "__main__":
    main()
