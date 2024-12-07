import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel('Enter city name: ', self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton('Get Weather', self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.get_weather_button.setObjectName('get_weather_button')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')

        self.setStyleSheet('''
                    /* Main window background */
                    QWidget {
                        background-color: #87CEEB; /* Sky blue for weather theme */
                    }

                    /* Title label styling */
                    QLabel#title {
                        font-size: 30px;
                        font-weight: bold;
                        font-family: "Arial";
                        color: #FFFFFF;
                        background-color: transparent;
                        padding: 10px;
                        text-align: center;
                    }

                    /* Weather information labels */
                    QLabel {
                        font-size: 20px;
                        font-family: "Calibri";
                        color: #333333;
                        padding: 5px;
                        background-color: rgba(255, 255, 255, 0.7); /* Slightly transparent white */
                        border: 1px solid #FFFFFF;
                        border-radius: 10px;
                        margin: 5px;
                    }

                    /* Buttons */
                    QPushButton {
                        background-color: #FFD700; /* Golden yellow for buttons */
                        color: #333333;
                        font-size: 18px;
                        font-family: "Verdana";
                        font-weight: bold;
                        border-radius: 15px;
                        border: 2px solid #FFFFFF;
                        padding: 10px;
                    }

                    QPushButton:hover {
                        background-color: #FFC107; /* Slightly darker yellow on hover */
                    }

                    QPushButton:pressed {
                        background-color: #FFA000; /* Even darker yellow when pressed */
                        border: 2px solid #FFA000;
                    }

                    /* Input fields */
                    QLineEdit {
                        font-size: 18px;
                        font-family: "Tahoma";
                        padding: 8px;
                        border: 2px solid #FFFFFF;
                        border-radius: 8px;
                        color: #333333;
                        background-color: rgba(255, 255, 255, 0.8); /* Transparent white */
                    }

                    QLineEdit:focus {
                        border: 2px solid #FFA000; /* Highlight border when focused */
                    }

                    /* Weather icon container */
                    QLabel#icon {
                        background-color: transparent; /* Transparent background for weather icons */
                        border: none;
                        padding: 10px;
                    }

                    /* Footer or additional text */
                    QLabel#footer {
                        font-size: 12px;
                        font-family: "Courier New";
                        color: #FFFFFF;
                        background-color: transparent;
                        text-align: center;
                        margin-top: 20px;
                    }
                ''')

        self.get_weather_button.clicked.connect(self.get_weather)


        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = 'af7e592be80911ea99bb678ac2575a61'
        city = self.city_input.text()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data['cod'] == 200:
                self.display_weather(data)
            else:
                self.display_error(data.get('message', 'Error retrieving weather data'))

        except requests.exceptions.HTTPError as http_error:
            self.display_error(f'HTTP error occurred: {http_error}')
        except requests.exceptions.ConnectionError:
            self.display_error('Connection Error: Check your Internet Connection')
        except requests.exceptions.Timeout:
            self.display_error('Timeout Error: The request timed out')
        except requests.exceptions.RequestException as req_error:
            self.display_error(f'Request Error: {req_error}')
        except KeyError:
            self.display_error('Unexpected response format. Please try again.')

    def display_error(self, message):
        self.temperature_label.setStyleSheet('font-size: 20px; color: red;')
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet('font-size: 75px;')
        temperature_k = data['main']['temp']
        temperature_c = temperature_k - 273.15
        weather_id = data['weather'][0]['id']
        weather_description = data['weather'][0]['description']

        self.temperature_label.setText(f'{temperature_c:.0f}°C')
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return '⛈️'
        elif 300 <= weather_id <= 321:
            return '🌦️'
        elif 500 <= weather_id <= 531:
            return '🌧️'
        elif 600 <= weather_id <= 622:
            return '❄️'
        elif 701 <= weather_id <= 741:
            return '🌫️'
        elif weather_id == 762:
            return '🌋'
        elif weather_id == 771:
            return '💨'
        elif weather_id == 781:
            return '🌪️'
        elif weather_id == 800:
            return '☀️'
        elif 801 <= weather_id <= 804:
            return '☁️'
        else:
            return ''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
