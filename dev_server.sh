#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Set the FLASK_APP environment variable
export FLASK_APP=run.py

# Enable Flask’s development mode
export FLASK_ENV=development

# Run the Flask application
flask run
