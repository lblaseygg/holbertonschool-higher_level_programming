# Python Object Relational Mapping

This project focuses on implementing Object Relational Mapping (ORM) in Python using MySQL and SQLAlchemy. The project demonstrates how to interact with a MySQL database using both raw SQL queries and SQLAlchemy ORM.

## Requirements

- Python 3.8.5
- MySQL 8.0
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- pycodestyle 2.7.*

## Setup

1. Install MySQL 8.0:
```bash
sudo apt update
sudo apt install mysql-server
```

2. Install MySQLdb dependencies:
```bash
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
```

3. Install SQLAlchemy:
```bash
sudo pip3 install SQLAlchemy
```

## Project Structure

- `models/` - Contains SQLAlchemy model definitions
- `tests/` - Contains test files
- `*.py` - Main project files

## Style Guide

All code follows PEP 8 style guidelines and is checked using pycodestyle (version 2.7.*).

## Documentation

All modules, classes, and functions include comprehensive documentation that can be accessed using:
```bash
python3 -c 'print(__import__("module_name").__doc__)'
python3 -c 'print(__import__("module_name").ClassName.__doc__)'
python3 -c 'print(__import__("module_name").function_name.__doc__)'
```

## Usage

[Usage instructions will be added as the project develops] 