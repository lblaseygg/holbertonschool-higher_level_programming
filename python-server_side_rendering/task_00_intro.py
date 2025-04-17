#!/usr/bin/env python3
"""
Task 0: Creating a Simple Templating Program
"""

import logging
import os

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee information
    
    Returns:
        None
    """
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Check input types
    if not isinstance(template, str):
        logging.error("Template must be a string")
        return
    if not isinstance(attendees, list):
        logging.error("Attendees must be a list")
        return
    
    # Check for empty template
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    
    # Check for empty attendees list
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        if not isinstance(attendee, dict):
            logging.error(f"Attendee at index {i-1} is not a dictionary")
            continue
            
        # Create output content by replacing placeholders
        output_content = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A')
            if value is None:
                value = 'N/A'
            output_content = output_content.replace(f'{{{key}}}', str(value))
        
        # Write to output file
        output_file = f'output_{i}.txt'
        try:
            with open(output_file, 'w') as f:
                f.write(output_content)
            logging.info(f"Generated {output_file}")
        except Exception as e:
            logging.error(f"Error writing to {output_file}: {str(e)}")

if __name__ == "__main__":
    # Example usage
    with open('template.txt', 'r') as file:
        template_content = file.read()

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees) 