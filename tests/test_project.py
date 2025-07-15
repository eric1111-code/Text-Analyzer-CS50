from project import (
    count_words,
    count_sentences,
    count_syllables,
    text_complexity,
    flesch_kincaid,
    count_chars,
    most_common,
    _clean_text,
)


def test_count_words():
    assert count_words("Hello world!") == 2
    assert count_words("It's a great day.") == 4
    assert count_words("") == 0


def test_count_chars():
    assert count_chars("test") == 4
    assert count_chars("Hi there!") == 9
    assert count_chars("") == 0


def test_count_sentences():
    assert count_sentences("Hello. How are you? I'm fine!") == 3
    assert count_sentences("One sentence") == 0
    assert count_sentences("") == 0


def test_count_syllables():
    assert count_syllables("banana") == 3
    assert count_syllables("apple") == 2
    assert count_syllables("make") == 1
    assert count_syllables("the") == 1


def test_most_common():
    table = most_common("apple apple banana banana banana orange")
    assert "banana" in table
    assert "3" in table


def test_text_complexity():
    text_clean = "this is a test of the system"
    text_raw = "This is a test of the system."
    assert text_complexity(text_clean, text_raw) == 7


def test_flesch_kincaid():
    text_clean = "this is a test of the system"
    text_raw = "This is a test of the system."
    score = flesch_kincaid(text_clean, text_raw)
    assert isinstance(score, float)
    assert score > 0


def test_clean_text():
    assert _clean_text("Hello, world!") == "hello world"
    assert _clean_text("It's great.") == "it's great"
    assert _clean_text("1234 is fine.") == "1234 is fine"
