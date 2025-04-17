#!/usr/bin/env python3
"""
Task 1: Creating a Basic HTML Template in Flask
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 