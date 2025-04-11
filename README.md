# Flask Server-Side Rendering Demo

This project demonstrates server-side rendering using Flask and Jinja2 templates. It showcases how to create dynamic web pages that are rendered on the server before being sent to the client.

## Features

- Server-side rendering with Flask and Jinja2
- Responsive web design
- Clean and modern UI
- Template inheritance
- Dynamic content rendering

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd python-server_side_rendering
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure you're in the project directory and your virtual environment is activated.

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
├── templates/          # Jinja2 templates
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   └── about.html     # About page
└── README.md          # Project documentation
```

## Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [MDN Web Docs on Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn/Server-side)

## License

This project is licensed under the MIT License - see the LICENSE file for details. 