# python-almost_a_circle

This project is about object-oriented programming in Python: a `Base`
class that manages ids and JSON serialization, a `Rectangle` class that
inherits from it, and a `Square` class that inherits from `Rectangle`.
It also covers `*args` and `**kwargs`, static and class methods, JSON
files, and unit tests.

## Requirements

- Python 3 (Ubuntu 20.04 LTS), files end with a new line
- First line of every file: `#!/usr/bin/python3`
- Code follows the `pycodestyle` style
- Modules, classes and methods are documented
- All files are executable
- Run all the tests: `python3 -m unittest discover tests`

## Files

| File | Description |
| ---- | ----------- |
| `models/__init__.py` | Makes `models` a package |
| `models/base.py` | `Base`: id management, `to_json_string`, `from_json_string`, `save_to_file`, `create`, `load_from_file` |
| `models/rectangle.py` | `Rectangle`: validated attributes, `area`, `display`, `__str__`, `update`, `to_dictionary` |
| `models/square.py` | `Square`: `size`, `__str__`, `update`, `to_dictionary` |
| `tests/test_models/test_base.py` | Unit tests for `Base` |
| `tests/test_models/test_rectangle.py` | Unit tests for `Rectangle` |
| `tests/test_models/test_square.py` | Unit tests for `Square` |

## Author

dngoga1-ai
