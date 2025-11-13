"""
File: writer_bot_ht.py
Author: Saketh Katta
Course: CSC 120, Fall 2024
Purpose: This program generates text using a Markov chain model implemented
with a custom hashtable. It processes a source text to build prefixes
and suffixes and generates random text based on user input.
"""

import sys
import random

SEED = 8
NONWORD = '@'

class Hashtable:
    """Custom hashtable implementation for storing prefix-suffix pairs."""

    def __init__(self, size):
        """Initializes the hashtable with a given size.

        Parameters:
            size: The size of the underlying storage array.
        """
        self._size = size
        self._pairs = [None] * size

    def _hash(self, key):
        """Computes a hash value for the given key.

        Parameters:
            key: The string key to hash.

        Returns:
            An integer representing the hash value within the bounds of the
            hashtable size.
        """
        p = 0
        for c in key:
            p = 31 * p + ord(c)
        return p % self._size

    def put(self, key, value):
        """Adds a key-value pair to the hashtable.

        Parameters:
            key: The key to store.
            value: The value to associate with the key.
        """
        index = self._hash(key)
        while self._pairs[index] is not None:
            if self._pairs[index][0] == key:
                # Appends to the value list if key already exists.
                self._pairs[index][1].append(value)
                return
            index = (index - 1) % self._size
        # Stores the new key value pair.
        self._pairs[index] = [key, [value]]

    def get(self, key):
        """Retrieves the value associated with a given key.

        Parameters:
            key: The key to look up.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        index = self._hash(key)
        while self._pairs[index] is not None:
            if self._pairs[index][0] == key:
                return self._pairs[index][1]
            index = (index - 1) % self._size
        return None

    def __contains__(self, key):
        """Checks if a key is in the hashtable.

        Parameters:
            key: The key to check.

        Returns:
            True if the key exists, False otherwise.
        """
        index = self._hash(key)
        while self._pairs[index] is not None:
            if self._pairs[index][0] == key:
                return True
            index = (index - 1) % self._size
        return False


def build_table(source_text, n, table_size):
    """Builds a Markov chain table from the source text.

    Parameters:
        source_text: The input text to process.
        n: The prefix size (number of words in the prefix).
        table_size: The size of the hashtable.

    Returns:
        A hashtable containing prefixes as keys and
        lists of suffixes as values.
    """
    table = Hashtable(table_size)
    words = [NONWORD] * n + source_text.split() + [NONWORD]
    for i in range(len(words) - n):
        prefix = ' '.join(words[i:i + n])
        suffix = words[i + n]
        table.put(prefix, suffix)
    return table


def generate_text(table, n, num_words):
    """Generates random text using the Markov chain table.

    Parameters:
        table: The Markov chain table (hashtable of prefixes and suffixes).
        n: The prefix size (number of words in the prefix).
        num_words: The number of words to generate.

    Returns:
        A list of generated words forming the random text.
    """
    result = []
    prefix = ' '.join([NONWORD] * n)

    while len(result) < num_words:
        suffixes = table.get(prefix)
        if suffixes is None:
            break

        # Randomly selects a suffix if multiple exist.
        if len(suffixes) > 1:
            index = random.randint(0, len(suffixes) - 1)
            suffix = suffixes[index]
        else:
            suffix = suffixes[0]

        # Stops if the suffix is NONWORD.
        if suffix == NONWORD:
            break

        result.append(suffix)
        # Updates the prefix with the next suffix.
        prefix_words = prefix.split()[1:] + [suffix]
        prefix = ' '.join(prefix_words)

    return result


def main():
    """Main function to build the Markov chain table and generate random text.

    Reads user inputs for the source file, table size, prefix size, and the
    number of words to generate. Outputs the generated text in chunks.
    """
    random.seed(SEED)
    sfile = input().strip()
    table_size = int(input().strip())
    n = int(input().strip())
    num_words = int(input().strip())

    if n < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)

    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    # Reads the source text file.
    file = open(sfile, 'r')
    source_text = file.read().strip()
    file.close()

    # Builds the table and generate the text.
    table = build_table(source_text, n, table_size)
    generated_text = generate_text(table, n, num_words)

    # Prints the generated text in lines of up to 10 words.
    for i in range(0, len(generated_text), 10):
        print(' '.join(generated_text[i:i + 10]))


if __name__ == "__main__":
    main()
