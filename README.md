# Text Analyzer

#### Video Demo: <https://youtu.be/yky55f8EF-g>
#### Description:

Text Analyzer is a Python-based tool that takes in raw text or '.txt' files and provides statistics such as word count, sentence count,
complexity, and readability.

This project:
- Contains a `main()` function and 3+ other custom functions.
- At least three functions are covered with `pytest` unit tests.
- Uses external libraries declared in `requirements.txt`.
- Includes a complete README and demo video.

---

### Features:

- **Word Count**
  Uses regex to count all valid words, including contractions.

- **Character Count**
  Counts every character in the original, unaltered text.

- **Sentence Count**
  Identifies sentence boundaries using punctuation.

- **Text Complexity**
  Calculates the average number of words per sentence.

- **Flesch–Kincaid Grade Level**
  Uses the standard readability formula to estimate the U.S. school reading level. Syllable estimation performed through the `syllables` library.

- **Most Common Words**
  Displays a formatted table of the top 3 most frequent words.

- **File Output Option**
  After analyzing the text, the user can optionally export the results to a file.

---

### How It Works:

- The program prompts the user to input either a string of text or a path to a `.txt` file.
- It reads the text, cleans it (removing punctuation but preserving contractions), and analyzes it through several functions.
- The main output is printed to the terminal and can also be saved to a user-defined file.

---

### Files:

- `project.py` – The main Python program containing all logic.
- `test_project.py` – Unit tests for core functions (not shown here).
- `requirements.txt` – Lists the external dependencies (e.g., `syllables`, `tabulate`).
- `README.md` – This file.

---

### Design Considerations:

- The syllable-counting logic was initially implemented manually but was replaced with the `syllables` library for simplicity.
- All core logic is broken into separate functions for readability and testability.
- The program is command-line based.

---

### Future Improvements:

- Add more advanced readability formulas (e.g., Gunning Fog, SMOG Index).
- Visualize results using `matplotlib` or similar libraries.
- Build a GUI or web version with Flask


