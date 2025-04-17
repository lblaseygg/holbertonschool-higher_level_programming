# Flask Server-Side Rendering Project

This project demonstrates different aspects of Flask and Jinja templating through four tasks:

## Project Structure

```
python-server_side_rendering/
├── task_01_jinja.py      # Basic template inheritance
├── task_02_logic.py      # Dynamic content with loops
├── task_03_files.py      # JSON and CSV file handling
├── task_04_db.py         # SQLite database integration
├── templates/            # HTML templates
│   ├── header.html      # Base header template
│   ├── footer.html      # Base footer template
│   ├── index.html       # Home page template
│   ├── about.html       # About page template
│   ├── contact.html     # Contact page template
│   ├── task_02/         # Task 2 templates
│   └── task_03/         # Task 3 templates
├── static/              # Static files (CSS)
├── items.json           # Sample items data
├── products.json        # Sample products data (JSON)
└── products.csv         # Sample products data (CSV)
```

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install flask
```

## Running the Tasks

### Task 1: Basic Template Inheritance
```bash
python3 task_01_jinja.py
```
Access:
- http://localhost:5000/
- http://localhost:5000/about
- http://localhost:5000/contact

### Task 2: Dynamic Template with Loops
```bash
python3 task_02_logic.py
```
Access:
- http://localhost:5000/items

### Task 3: JSON and CSV File Handling
```bash
python3 task_03_files.py
```
Access:
- http://localhost:5000/products?source=json
- http://localhost:5000/products?source=csv
- http://localhost:5000/products?source=json&id=1

### Task 4: SQLite Database Integration
```bash
python3 task_04_db.py
```
Access:
- http://localhost:5000/products?source=sql
- http://localhost:5000/products?source=sql&id=1

## Features Demonstrated

1. Task 1:
   - Template inheritance
   - Template inclusion
   - Basic routing
   - Static file serving

2. Task 2:
   - Dynamic content with loops
   - Conditional rendering
   - JSON file reading

3. Task 3:
   - Multiple data sources (JSON, CSV)
   - Query parameter handling
   - Error handling
   - Table display

4. Task 4:
   - SQLite database integration
   - Database creation and population
   - Query parameter filtering
   - Error handling for all data sources
