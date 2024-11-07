import requests

API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "DEMO_KEY"  # Replace with your own API key


def get_apod(date=None):
    """
    Retrieve the APOD (Astronomy Picture of the Day) data for a specific date.
    If no date is provided, get the APOD data for the current date.
    """
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code: {response.status_code}")
