import pytest
from main import count_words

@pytest.fixture
def text_example():
    return "Це тестовий текст"

@pytest.mark.parametrize("text, expected_words", [
    ("Це тестовий текст", 3),
    ("Це ще один тестовий текст з більшою кількістю слів", 8),
    ("Текст з *&^%$", 1),
    ("", 0),
    ("   ", 0)
])
def test_count_words(text, expected_words):
    assert count_words(text) == expected_words

def test_count_words_using_fixture(text_example):
    assert count_words(text_example) == 3