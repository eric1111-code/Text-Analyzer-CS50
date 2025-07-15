import re
import os
from collections import Counter
from tabulate import tabulate
import syllables

# Private variables for regex patterns
_word_re = r"\b[a-zA-Z']+\b"
_sentence_re = r"[.!?]+(?=\s|$)"

# Private method for text cleaning
def _clean_text(text):
    return re.sub(r"[^\w\s']", "", text).lower()

# Private method for input verification
def _verify_input(text):
    if os.path.isfile(text):
        with open(text, "r") as file:
            return file.read()
    else:
        return text

# Counts the amount of words in given text
def count_words(text):
    words = re.findall(_word_re, text)
    return len(words)

# Counts characters in given text
def count_chars(text):
    return len(text)

# Count sentences in given text
def count_sentences(text):
    sentences = re.findall(_sentence_re, text)
    return len(sentences)

# Counts syllables in a word
def count_syllables(word):
    return syllables.estimate(word)

# Returns table of the most common words and their frequency
def most_common(text, n=3):
    words = re.findall(_word_re, text)
    most_common = Counter(words).most_common(n)
    table = tabulate(most_common, headers=["Word", "Count"], tablefmt="grid")
    return table

# Basic formula for roughly calculating complexity of text
def text_complexity(text_clean, text_raw):
    words = count_words(text_clean)
    sentences = count_sentences(text_raw)
    if sentences == 0:
        return 0
    return round(words / sentences, 1)

# Formula for roughly calculating grade level of text
def flesch_kincaid(text_clean, text_raw):
    word_list = re.findall(_word_re, text_clean)
    words = len(word_list)
    sentences = count_sentences(text_raw)
    syllables = 0
    for word in word_list:
        syllables += count_syllables(word)

    if words == 0 or sentences == 0:
        return 0

    grade_level = (
        0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
    )

    return round(grade_level, 0)

# Main - printing output/saving to file
def main():
    user_input = input('Enter text or path to ".txt": ')
    text_raw = _verify_input(user_input)
    text_clean = _clean_text(text_raw)

    # Save output in one spot
    output = []
    output.append(f"{count_words(text_clean)} words")
    output.append(f"{count_chars(text_raw)} characters")
    output.append(f"{count_sentences(text_raw)} sentences")
    output.append(f"Text Complexity (Avg Words/Sentence): {text_complexity(text_clean, text_raw)}")
    output.append(f"Flesch–Kincaid Grade Level: {flesch_kincaid(text_clean, text_raw)}")
    output.append(f"Most Common Words:\n{most_common(text_clean)}")

    full_output = "\n".join(output)
    print(full_output)

    # Ask user to save text info in file
    save = input("Would you like to save the results to a file? (y/n): ").strip().lower()
    if save == "y":
        filename = input("Enter filename: ").strip()
        try:
            with open(filename, "w") as file:
                file.write(full_output)
            print(f"Results saved to {filename}")
        except Exception as e:
            print("Error writing to file: {e}")


if __name__ == "__main__":
    main()