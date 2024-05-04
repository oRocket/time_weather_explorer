#!/usr/bin/python3

from app import app, db

# Create an application context to work within the Flask app
with app.app_context():
    # Create all database tables
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
