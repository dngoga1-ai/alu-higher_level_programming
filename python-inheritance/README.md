# python-inheritance

This project covers inheritance in Python: `dir()`, subclassing built-in
types, `type()`, `isinstance()` and `issubclass()`, the `super()` function,
and extending a base class (`BaseGeometry` -> `Rectangle` -> `Square`).

## Requirements

- Python 3 (Ubuntu 20.04 LTS), files end with a new line
- First line of every file: `#!/usr/bin/python3`
- Code follows the `pycodestyle` style
- Modules, classes and functions are documented
- All files are executable
- Doctests: `python3 -m doctest -v ./tests/1-my_list.txt`

## Files

| File | Description |
| ---- | ----------- |
| `0-lookup.py` | `lookup(obj)`: attributes and methods of an object |
| `1-my_list.py` | `MyList(list)` with `print_sorted()` |
| `2-is_same_class.py` | `is_same_class(obj, a_class)` |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)` |
| `4-inherits_from.py` | `inherits_from(obj, a_class)` |
| `5-base_geometry.py` | Empty class `BaseGeometry` |
| `6-base_geometry.py` | Adds `area()` that raises an exception |
| `7-base_geometry.py` | Adds `integer_validator()` |
| `8-rectangle.py` | `Rectangle` with validated private size |
| `9-rectangle.py` | Adds `area()` and `__str__` |
| `10-square.py` | `Square` inheriting from `Rectangle` |
| `11-square.py` | Adds `[Square] <width>/<height>` description |
| `tests/1-my_list.txt` | Doctests for task 1 |
| `tests/7-base_geometry.txt` | Doctests for task 7 |

## Author

dngoga1-ai
