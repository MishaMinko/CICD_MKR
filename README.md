# CICD_MKR

Modular Assessment (MA) for the **CI/CD** course. Implements a program to count words and sentences in a text file, covered by unit tests, with an automatically generated HTML report on the test results.

The project was completed as a modular assignment for the CI/CD course—a practical exercise in writing automated tests (pytest) and generating a test report, which is a fundamental element of the continuous integration (CI) process.

## Technology Stack

- **Python**
- **pytest** — unit testing framework
- **pytest-html** — generating an HTML report based on test results

## Functionality

- `count_words(text)` — counting the number of words in a text
- `count_sentences(text)` — counting the number of sentences in a text
- Read the input text from `text.txt` and write the calculation result to `result.txt`
- A set of parameterized unit tests for both functions

## Project structure

```
main.py                        # basic logic behind counting words and sentences
text.txt                       # input text file for analysis
tests/
├── test_count_words.py        # tests for the count_words function
└── test_count_sentences.py    # tests for the count_sentences function
report.html                    # pytest-html report generated
assets/style.css                # report styles
requirements.txt                # project dependencies
```

## How to start project

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start main program:
```bash
python main.py
```
The results of the word and sentence count will be saved to `result.txt`.

3. Run the tests that generate an HTML report:
```bash
pytest --html=report.html
```
