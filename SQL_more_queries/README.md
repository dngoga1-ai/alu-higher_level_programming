# SQL_more_queries

This project goes further with MySQL: users and privileges, constraints
(`NOT NULL`, `DEFAULT`, `UNIQUE`, `PRIMARY KEY`, `AUTO_INCREMENT`,
`FOREIGN KEY`), subqueries, and joins (`INNER JOIN`, `LEFT JOIN`) with
`GROUP BY` and `COUNT()`.

## Requirements

- MySQL 8.0 (Ubuntu 20.04 LTS)
- All files end with a new line and start with a comment describing the script
- SQL keywords are uppercase
- Usage: `cat <file>.sql | mysql -hlocalhost -uroot -p [database]`
- Tasks 10 to 16 use the `hbtn_0d_tvshows` database dump

## Files

| File | Description |
| ---- | ----------- |
| `0-privileges.sql` | Lists the grants of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and `user_0d_2` with SELECT only |
| `3-force_name.sql` | Table `force_name`, `name` cannot be null |
| `4-never_empty.sql` | Table `id_not_null`, `id` defaults to 1 |
| `5-unique_id.sql` | Table `unique_id`, `id` defaults to 1 and is unique |
| `6-states.sql` | Database `hbtn_0d_usa` and table `states` |
| `7-cities.sql` | Table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Cities of California, using a subquery |
| `9-cities_by_state_join.sql` | All cities with their state, using a join |
| `10-genre_id_by_show.sql` | Shows with at least one genre |
| `11-genre_id_all_shows.sql` | All shows with their genre ids (NULL if none) |
| `12-no_genre.sql` | Shows without a genre |
| `13-count_shows_by_genre.sql` | Number of shows per genre |
| `14-my_genres.sql` | Genres of the show Dexter |
| `15-comedy_only.sql` | Comedy shows |
| `16-shows_by_genre.sql` | All shows with their genre names |

## Author

dngoga1-ai
