# SQL Introduction

This project contains SQL scripts and exercises for learning SQL basics.

## Requirements
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- Files will be tested using wc for length

## SQL File Format
Example:
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Setup
To set up MySQL on Ubuntu 20.04:
```bash
sudo apt update
sudo apt install mysql-server
mysql --version
```

## Connection
To connect to MySQL:
```bash
sudo mysql
``` 