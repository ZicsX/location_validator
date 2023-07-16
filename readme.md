Location Validator
==================

This project is designed to scrape and validate store locations from a given URL. It leverages the Google Maps API to verify the existence of a store within a specific radius.

Getting Started
---------------

### Environment Setup

1. Clone the repository to your local machine.
2. Create a new virtual environment. Run `python  -m venv env` in your terminal.
3. Activate the virtual environment. On macOS and Linux, run `source env/bin/activate`, and on Windows run `.\env\Scripts\activate`.
4. Navigate to the root directory of the project in your terminal.
5. Run `pip install -r requirements.txt` to install the required Python packages. This command installs Django, requests, etc. which are necessary for the project.

### Configuration Setup

1. Rename `dot.env` to `.env`.
2. Open `.env` and set the appropriate configurations, such as the Google Places API key.

### Database Setup

1. Make sure you have your database setup and configured in the settings.py file.
2. Run the following command to make migrations `python manage.py makemigrations`.
3. Then, apply the migrations by running `python manage.py migrate`.

Running the Project
-------------------

To start the project, run `python manage.py runserver` in your terminal. This will start a development server at `http://127.0.0.1:8000/`.

Project Structure
-----------------

* **location\_validator**: This is the main Django application that includes settings, url configurations, etc.
* **stores**: This is the app responsible for scraping store locations, validating them, and saving the results in the database. It contains the scraper, validator, and views for the application.
* **manage.py**: This is the Django's command-line utility for administrative tasks. You can use it to create apps, run the server, etc.

Dependencies
------------

* **Django**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* **Requests**: A simple HTTP library for Python, built for human beings.
* **Google Places API**: This is used to validate the existence of a store within a specific radius based on given latitude and longitude.
