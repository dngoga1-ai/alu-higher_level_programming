# python-object_relational_mapping

This project connects Python to MySQL: first with the `MySQLdb` module
(raw SQL, SQL injection and how to avoid it), then with the SQLAlchemy ORM
(models, sessions, queries, insert, update and delete).

## Requirements

- Python 3 (Ubuntu 20.04 LTS), files end with a new line
- First line of every file: `#!/usr/bin/python3`
- Code follows the `pycodestyle` style
- Modules and classes are documented
- All files are executable
- Scripts are not executed when imported
- Modules: `MySQLdb` (mysqlclient) and `SQLAlchemy`

## Files

| File | Description |
| ---- | ----------- |
| `0-select_states.py` | Lists all states |
| `1-filter_states.py` | Lists states starting with N |
| `2-my_filter_states.py` | Filters states by name (format query, injectable) |
| `3-my_safe_filter_states.py` | Filters states by name (injection safe) |
| `4-cities_by_state.py` | Lists all cities with their state |
| `5-filter_cities.py` | Lists the cities of a state |
| `model_state.py` | `State` model and `Base` |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Prints the first `State` |
| `9-model_state_filter_a.py` | States containing the letter a |
| `10-model_state_my_get.py` | Gets a state id by name |
| `11-model_state_insert.py` | Adds the state Louisiana |
| `12-model_state_update_id_2.py` | Renames the state with id 2 |
| `13-model_state_delete_a.py` | Deletes states containing the letter a |
| `model_city.py` | `City` model |
| `14-model_city_fetch_by_state.py` | Lists all cities with their state |

## Author

dngoga1-ai
