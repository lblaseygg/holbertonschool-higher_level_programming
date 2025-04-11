# SQL More Queries

This project contains SQL queries for working with a TV shows database.

## Setup

1. Create the database:
```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
```

2. Import the SQL dump:
```bash
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

3. Verify the import:
```bash
echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
```

## Requirements

- All files should end with a new line
- All SQL queries should have a comment just before
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.)
- Files will be tested using `wc` command 