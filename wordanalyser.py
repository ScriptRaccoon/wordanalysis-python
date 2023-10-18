"""
Module for analyzing the word counts inside of a text document
(could be a long novel, for example). It counts how many times
each word appears, sorts the results by decreasing amounts,
and saves it to a file. Too common words (the, of, to, and, ...)
are filtered out to make the result more specific to the input file.
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


def get_common_words() -> list[str]:
    """
    Gets the list of too common words from a specific file
    """
    common_words = []
    with open("data/common_words.txt", "r", encoding="utf8") as file:
        for line in file:
            word = line.replace("\n", "").lower()
            common_words.append(word)
    return common_words


def add_word(word: str, word_dict: dict[str, int], common_words: list[str]) -> None:
    """
    Adds a word to the dictionary. Changes the dictionary in place.
    Ignores too common words.

    Arguments:
        word: any string
        word_dict: a dictionary which has the updated amount of the word
    """
    if len(word) == 0 or word in common_words:
        return
    if not word in word_dict:
        word_dict[word] = 0
    word_dict[word] += 1


def process_line(line: str, word_dict: dict[str, int], common_words: list[str]) -> None:
    """
    Adds all non-common words inside of a line to a dictionary.
    Changes the dictionary in place.

    Arguments:
        word: any string
        word_dict: a dictionary which has the updated amount of the words
    """
    words_in_line = map(clean, line.split(" "))
    for word in words_in_line:
        add_word(word, word_dict, common_words)


def generate_word_dict(file_name: str) -> dict[str, int]:
    """
    Generates the word dictionary from a text file.
    Too common words are filtered out.

    Arguments:
        file_name: name of the text file to be read.

    Returns:
        A dictionary which stores the amount all words
    """
    common_words = get_common_words()
    word_dict: dict[str, int] = {}

    with open(file_name, "r", encoding="utf8") as file:
        for line in file:
            process_line(line, word_dict, common_words)

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
        file_name: the name of the file to be written to.
    """
    with open(file_name, "w", encoding="utf8") as file:
        for word, amount in word_list:
            file.write(f"{word}: {amount}\n")


def get_summary(word_list: list[tuple[str, int]], source: str, target: str) -> str:
    """
    Generates a summary of the word list.

    Arguments:
        word_list: a list of words with their amounts
        source: input file
        target: output file

    Returns:
        The summary
    """
    summary = f"{len(word_list)} non-common words have been found in {source}.\n"
    top_word, amount = word_list[0]
    summary += f'The most popular word is "{top_word}" with {amount} occurrences.\n'
    summary += f"The whole list has been written to the file {target}."
    return summary


def main() -> None:
    """
    Generates the word list from the sample file and writes it to another file
    """
    source = "data/input.txt"
    target = "data/output.txt"
    word_list = generate_word_list(source)
    save_word_list(word_list, target)
    print(get_summary(word_list, source, target))


if __name__ == "__main__":
    main()
