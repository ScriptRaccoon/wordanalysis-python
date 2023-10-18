# Word analysis in Python

Module for analyzing the word counts inside of a text document (could be a long novel, for example). It counts how many times each word appears, sorts the results by decreasing amounts, and saves it to a file. Too common words (the, of, to, and, ...) are filtered out to make the result more specific to the input file.

For example, feading the script with Homer's _The Odyssey_ gives a list of over 7000 words, starting with

```
ulysses: 646
into: 286
telemachus: 271
upon: 268
suitors: 250
gods: 183
jove: 164
heaven: 160
till: 158
answered: 154
```
