
# Weather App

Weather App is a Python program that fetches weather data from an online API and displays it in a user-friendly format. The app allows users to check the weather for a given city by querying an external weather service API.
## Features

- City Weather Search: Fetches weather data based on the city name.
- Real-Time Data: Displays live weather updates such as temperature, humidity, and weather description.
- Error Handling: Handles errors gracefully if the city is not found or there’s an issue with the API.
## Requirements

- Python 3.x
- Required libraries:
 ```bash
   pip install requests, PyQt5
 ```
## Installation

1. Clone the repository:

    ```bash
    git clone <repository-link>
    cd weather-app
    ```
    
2. Run the weather app:
     ```bash
        python weather_app.py
## How it works

1. The user inputs a city name.
2. The app makes an API call to fetch weather data from an online service.
3. The app displays the current weather for that city, including temperature, humidity, and weather conditions.
## Results

- Real-Time Weather: Provides live weather information for cities worldwide.
- Weather Data: Shows data such as temperature (in Celsius or Fahrenheit), weather conditions (clear, cloudy, etc.), and humidity.
## Future Enhancements 

- Multi-City Search: Allow the user to search for the weather in multiple cities at once.
- Forecast Feature: Add the ability to display weather forecasts for the next few days.
