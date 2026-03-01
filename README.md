# Flask Weather App

A Flask-based web app that displays current weather information for a given city.

## Screenshot

![Gh1iSFHWUAAUr9f](https://github.com/user-attachments/assets/f7e1724f-e22a-4585-9368-155343f385f0)

## Features

- Current weather information
- Search by city name

## Setup

### Prerequisites

- Python 3.12+
- (Optional but recommended) **uv** package manager: <https://docs.astral.sh/uv/>

---

## Environment variables (.env)

This project uses **python-dotenv** to load environment variables from a `.env` file.

1. Create your local `.env` file from the example:

   ```bash
   cp example.env .env
   ```

2. Update the values inside `.env`:
   - `ACCESS_KEY`: Weatherstack API key (required for weather requests)
   - `SECRET_KEY`: Flask secret key (required for sessions/flash messages)

---

## Installation (recommended: uv)

1. Clone the repository:

   ```bash
   git clone https://github.com/DevMohammad-SA/flask-weather-app.git
   cd flask-weather-app
   ```

2. Create and activate a virtual environment with uv:

   ```bash
   uv venv
   # macOS/Linux
   source .venv/bin/activate
   # Windows (PowerShell)
   # .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   uv pip install -r requirements.txt
   ```

---

## Installation (pip + venv)

1. Clone the repository:

   ```bash
   git clone https://github.com/DevMohammad-SA/flask-weather-app.git
   cd flask-weather-app
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows
   # venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the application

### Option A: Flask CLI

```bash
export FLASK_APP=run.py   # macOS/Linux
# set FLASK_APP=run.py    # Windows (cmd)
# $env:FLASK_APP="run.py" # Windows (PowerShell)

flask run
```

### Option B: Run directly

```bash
python run.py
```

Open your browser at: <http://127.0.0.1:5000>

## Usage

- Enter a city name in the search bar to get the current weather.

## License

MIT
