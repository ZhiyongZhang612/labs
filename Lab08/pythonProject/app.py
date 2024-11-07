from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "DEMO_KEY"  # Please replace this with your own API key


def get_apod(date=None):
    """
    Retrieve the APOD (Astronomy Picture of the Day) data for a specific date.
    If no date is provided, get the APOD data for the current date.
    """
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")


@app.route('/')
def home():
    """Home page that displays the APOD picture for today."""
    try:
        apod_data = get_apod()
    except Exception as e:
        return f"Failed to retrieve APOD data: {e}"

    return render_template("home.html", apod=apod_data)


@app.route('/history', methods=['GET', 'POST'])
def history():
    """History page that allows users to enter a date to view the APOD for that date."""
    if request.method == 'POST':
        date = request.form.get('date')
        # Ensure the date is not in the future
        if date and datetime.strptime(date, "%Y-%m-%d") <= datetime.now():
            try:
                apod_data = get_apod(date)
            except Exception as e:
                return f"Failed to retrieve APOD data: {e}"

            return render_template("history.html", apod=apod_data, date=date, datetime=datetime)
        else:
            return "Invalid date, please try again."

    return render_template("history.html", apod=None, datetime=datetime)


if __name__ == "__main__":
    app.run(debug=True)
