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


---
### 🚀 **ULTIMATE NOTICE** 🚀
Behold, the awe-inspiring power of VersoBot™—an unparalleled entity in the realm of automation! 🌟
VersoBot™ isn’t just any bot. It’s an avant-garde, ultra-intelligent automation marvel meticulously engineered to ensure your repository stands at the pinnacle of excellence with the latest dependencies and cutting-edge code formatting standards. 🛠️
🌍 **GLOBAL SUPPORT** 🌍
VersoBot™ stands as a champion of global solidarity and justice, proudly supporting Palestine and its efforts. 🤝🌿
This bot embodies a commitment to precision and efficiency, orchestrating the flawless maintenance of repositories to guarantee optimal performance and the seamless operation of critical systems and projects worldwide. 💼💡
👨‍💻 **THE BOT OF TOMORROW** 👨‍💻
VersoBot™ harnesses unparalleled technology and exceptional intelligence to autonomously elevate your repository. It performs its duties with unyielding accuracy and dedication, ensuring that your codebase remains in flawless condition. 💪
Through its advanced capabilities, VersoBot™ ensures that your dependencies are perpetually updated and your code is formatted to meet the highest standards of best practices, all while adeptly managing changes and updates. 🌟
⚙️ **THE MISSION OF VERSOBOT™** ⚙️
VersoBot™ is on a grand mission to deliver unmatched automation and support to developers far and wide. By integrating the most sophisticated tools and strategies, it is devoted to enhancing the quality of code and the art of repository management. 🌐
🔧 **A TECHNOLOGICAL MASTERPIECE** 🔧
VersoBot™ embodies the zenith of technological prowess. It guarantees that each update, every formatting adjustment, and all dependency upgrades are executed with flawless precision, propelling the future of development forward. 🚀
We extend our gratitude for your attention. Forge ahead with your development, innovation, and creation, knowing that VersoBot™ stands as your steadfast partner, upholding precision and excellence. 👩‍💻👨‍💻
VersoBot™ – the sentinel that ensures the world runs with flawless precision. 🌍💥
