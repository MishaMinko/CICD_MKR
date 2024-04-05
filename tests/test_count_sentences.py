import pytest
from main import count_sentences

@pytest.fixture
def text_example():
    return "Це речення. Це речення! Це речення?."

@pytest.mark.parametrize("text, expected_sentences", [
    ("Тестове речення. Ще одне!", 2),
    ("Це одне речення *&^%$", 1),
    ("", 0),
    ("   ", 0)
])

def test_count_sentences(text, expected_sentences):
    assert count_sentences(text) == expected_sentences

def test_count_words_using_fixture(text_example):
    assert count_sentences(text_example) == 3