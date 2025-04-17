# Python Server-Side Rendering

This project demonstrates server-side rendering techniques using Python and Flask. It includes several tasks that progressively build up the understanding of server-side rendering, templating, and data handling.

## Tasks

### Task 0: Creating a Simple Templating Program
- Implements a function to generate personalized invitation files from a template
- Handles various edge cases and errors gracefully
- Uses string templating and file operations

### Task 1: Creating a Basic HTML Template in Flask
- Sets up a Flask application with basic routes
- Creates reusable HTML templates using Jinja
- Implements a consistent layout with header and footer components

### Task 2: Creating a Dynamic Template with Loops and Conditions
- Demonstrates dynamic content rendering using Jinja templates
- Reads and displays data from JSON files
- Implements conditional rendering and loops

### Task 3: Displaying Data from JSON or CSV Files
- Extends the application to handle multiple data sources
- Implements data filtering based on query parameters
- Handles various error cases and edge conditions

### Task 4: Extending Dynamic Data Display to Include SQLite
- Adds SQLite database support to the application
- Demonstrates reading data from multiple sources (JSON, CSV, SQLite)
- Implements proper error handling for database operations

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/holbertonschool-higher_level_programming.git
cd python-server_side_rendering
```

2. Install the required dependencies:
```bash
pip install flask
```

3. Run the individual task applications:
```bash
# Task 0
python3 task_00_intro.py

# Task 1
python3 task_01_jinja.py

# Task 2
python3 task_02_logic.py

# Task 3
python3 task_03_files.py

# Task 4
python3 task_04_db.py
```

## Usage

Each task demonstrates different aspects of server-side rendering:

- Task 0: Run the script to generate invitation files from the template
- Tasks 1-4: Access the Flask applications at http://localhost:5000

For Tasks 3 and 4, you can access the products page with different data sources:
- http://localhost:5000/products?source=json
- http://localhost:5000/products?source=csv
- http://localhost:5000/products?source=sql

You can also filter products by ID:
- http://localhost:5000/products?source=json&id=1

## Features

- Server-side rendering with Flask and Jinja
- Multiple data source support (JSON, CSV, SQLite)
- Error handling and edge cases
- Reusable templates and components
- Dynamic content rendering
- Data filtering and querying

## Requirements

- Python 3.x
- Flask
- SQLite3 (built into Python)

## Author

[Your Name]

## License

This project is licensed under the MIT License - see the LICENSE file for details.
