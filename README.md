# Flask Weather App

Flask Weather App is a Flask-based web application that provides weather information for different locations.

## Screenshots
![Gh1iSFHWUAAUr9f](https://github.com/user-attachments/assets/f7e1724f-e22a-4585-9368-155343f385f0)

## Features

- Current weather information
- Search by city name

## Setup

### Prerequisites

- Python 3.8 or higher
- Flask

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DevMohammad-SA/flask-weather-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-weather-app
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash

     source venv/bin/activate
     ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Set the FLASK_APP environment variable:

   ```bash
   export FLASK_APP=app.py
   ```

2. Run the Flask development server:

   ```bash
   flask run
   ```

3. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Enter a city name in the search bar to get the current weather.

## License

This project is licensed under the MIT License.
