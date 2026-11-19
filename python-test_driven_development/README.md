# python-test_driven_development

This project is about test driven development in Python: writing
documentation, interactive tests with `doctest` (text files in `tests/`),
and unit tests with the `unittest` module.

## Requirements

- Python 3 (Ubuntu 20.04 LTS), files end with a new line
- First line of every Python file: `#!/usr/bin/python3`
- Code follows the `pycodestyle` style
- Modules and functions are documented
- All files are executable
- Doctests: `python3 -m doctest -v ./tests/<file>.txt`
- Unittests: `python3 -m unittest tests.6-max_integer_test`

## Files

| File | Description |
| ---- | ----------- |
| `0-add_integer.py` | Adds two integers (floats are cast) |
| `2-matrix_divided.py` | Divides all elements of a matrix |
| `3-say_my_name.py` | Prints `My name is <first name> <last name>` |
| `4-print_square.py` | Prints a square with `#` |
| `5-text_indentation.py` | Prints text with 2 new lines after `.`, `?` and `:` |
| `6-max_integer.py` | Function tested by the unittests (provided) |
| `tests/*.txt` | Doctests for tasks 0 to 5 |
| `tests/6-max_integer_test.py` | Unittests for `max_integer` |

## Author

dngoga1-ai
