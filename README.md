# My Web App
## Description
This is a web app that serves an index.html file and a data API from a Python web server, and reads data from a SQLite database. The index.html file uses Vue.js to call the data API and display the results in a table. The web app includes error handling and a loading state.

## Installation
1. Install Python 3 and SQLite.
2. Clone this repository.
3. Install the required packages using `pip install -r requirements.txt`.
4. Seed the database with example data using `python seed.py`.
5. Start the web server using `python server.py`.
6. Open a web browser and go to http://localhost.

## Usage
The web app has two endpoints:

1. `/` serves the `index.html` file, which displays a table of data from the database.
2. `/api/data` returns an array of JSON objects containing data from the database.
If the data cannot be loaded due to an error, an error message will be displayed instead of the table.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
