# WordFinder

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

WordFinder is a Python package designed to find words in a sentence with a given similarity threshold.

## Installation

```bash
pip install word-finder
```

## Requirements

- Python 3.x
- fuzzywuzzy

## Usage

```python
from word_finder import WordFinder

# Create an instance of WordFinder
word_finder = WordFinder("This is a sample sentence.")

# Find words in the sentence
result = word_finder.find_words(["example", "word"])
print(result)  # Output: {'example'}
```

## Documentation

### `WordFinder(sentence)`

Initializes a new instance of the WordFinder class.

- `sentence` (str): The input sentence to be processed.

### `_clean_sentence() -> str`

Cleans the input sentence by removing non-alphabetic characters and converting to lowercase.

Returns:
- `str`: Cleaned sentence.

### `find_words(target_words, similarity_threshold=80) -> set`

Finds words in the cleaned sentence that match the target words based on a similarity threshold.

Args:
- `target_words` (list): List of target words to search for.
- `similarity_threshold` (int): Minimum similarity threshold (default is 80).

Returns:
- `set`: Set of found words.

## Example

```python
word_finder = WordFinder("This is a sample sentence.")
result = word_finder.find_words(["example", "word"])
print(result)  # Output: {'example'}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
