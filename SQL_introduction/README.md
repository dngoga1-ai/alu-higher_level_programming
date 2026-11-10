# SQL_introduction

This project is an introduction to SQL with MySQL: creating and removing
databases and tables, inserting, selecting, updating and deleting rows,
and using `ORDER BY`, `WHERE`, `AVG()`, `COUNT()` and `GROUP BY`.

## Requirements

- MySQL 8.0 (Ubuntu 20.04 LTS)
- All files end with a new line and start with a comment describing the script
- SQL keywords are uppercase
- Usage: `cat <file>.sql | mysql -hlocalhost -uroot -p [database]`

## Files

| File | Description |
| ---- | ----------- |
| `0-list_databases.sql` | Lists all databases |
| `1-create_database_if_missing.sql` | Creates `hbtn_0c_0` if missing |
| `2-remove_database.sql` | Deletes `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables of a database |
| `4-first_table.sql` | Creates `first_table` |
| `5-full_table.sql` | Prints the full definition of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts a row in `first_table` |
| `8-count_89.sql` | Counts the records with `id = 89` |
| `9-full_creation.sql` | Creates `second_table` and adds rows |
| `10-top_score.sql` | Lists records by score, top first |
| `11-best_score.sql` | Lists records with a score >= 10 |
| `12-no_cheating.sql` | Updates Bob's score to 10 |
| `13-change_class.sql` | Removes records with a score <= 5 |
| `14-average.sql` | Computes the score average |
| `15-groups.sql` | Counts the records per score |
| `16-no_link.sql` | Lists records with a name, by descending score |

## Author

dngoga1-ai
