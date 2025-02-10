# Basic Weather Application with API

import sys
import requests
import APIkey
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):       
        super().__init__()      
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter) 
        self.city_input.setAlignment(Qt.AlignCenter)
        # get_weather_button expands the width of the window
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # set styles based on the QLabel and QPushButton classes:
        self.setStyleSheet("""QLabel, QPushButton{font-family: calibri;}
                           QLabel#city_label{font-size: 40px; font-style: italic;}
                           QLineEdit#city_input{font-size:40px;}
                           QPushButton#get_weather_button{font-size: 30px; font-weight: bold; border: 3px solid; border-radius: 15px;}
                           QLabel#temp_label{font-size: 75px;}
                           QLabel#emoji_label{font-size: 100px; font-family: Segoe UI emoji;} 
                           QLabel#description_label{font-size: 50px;}""")
        
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        
        city = self.city_input.text()      
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey.api_key}"      

        try:
            response = requests.get(url)
            
            response.raise_for_status()

            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        
        # **types of exceptions: 
        #   1. http error (an exception raised by the request module when an HTTP request returns a 400/500 status code) 
        #   2. connection error; internet disconnected, etc.
        #   3. timeout error; the request has timed out (both ConnectTimeout and ReadTimeout errors)
        #   4. redirect error; too many redirects
        #   5. request exception; anything else (can be due to network problems, invalid URLs, etc.)
        
        # ***HTTPError:
        except requests.exceptions.HTTPError as http_error:
            match response.status_code: 
                case 400:        
                    self.display_error("Bad request\nPlease check your input")
                case 401:             
                    self.display_error("Unauthorized\nInvalid API key")
                case 403:         
                    self.display_error("Forbidden\nAccess is denied")
                case 404:            
                    self.display_error("Not found\nCity not found")
                case 500:                 
                    self.display_error("Internal server error\nPlease try again later")
                case 502:                    
                    self.display_error("Bad gateway\nInvalid response from the server")
                case 503:                     
                    self.display_error("Service unavailable\nServer is down")
                case 504:                  
                    self.display_error("Gateway timeout\nNo response from the server")
                case _:                  
                    self.display_error(f"HTTP error occured\n{http_error}")

        # ***ConnectionError:
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")

        # ***Timeout:
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")

        # ***TooManyRedirects:
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL") 

        # ***RequestException:
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
        
    # display the error in the app instead of on terminal print line:
    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 30px;")
        self.temp_label.setText(message)        # set the text for the temperature label to be the message passed in
        self.emoji_label.clear()                # clear the emoji when displaying an error with the clear method
        self.description_label.clear()          # clear the description when displaying an error 

    # display weather method; receive an object to represent the data
    def display_weather(self, data):
        self.temp_label.setStyleSheet("font-size: 85px;")

        # retrieve the weather data:
        temp_data = data["main"]["temp"]
        temp_c = temp_data - 273.15            # convert default temp from kelvin to celsius
        temp_f = (temp_data * 9/5) - 459.67    # convert defailt temp from kelvin to fahrenheit

        # retrieve weather id:
        weather_id = data["weather"][0]["id"]

        # retrieve weather description:
        weather_description = data["weather"][0]["description"]

        # change temp, emoji, and description label and set the text to output the return of each variable
        self.temp_label.setText(f"{temp_f:.0f}°F") 
        self.emoji_label.setText(self.get_weather_emoji(weather_id)) 
        self.description_label.setText(weather_description)

    # display emoji according to weather;
    @staticmethod                      
    def get_weather_emoji(weather_id):    # pass in a weather ID and return an emoji
        if 200 <= weather_id <= 232:
            return "⛈️"                   # 200 - 232 = Thunderstorm
        elif 300 <= weather_id <= 321:
            return "☂️"                   # 300 - 321 = Rain drizzle
        elif 500 <= weather_id <= 531:
            return "☔"                   # 500 - 531 = Rain
        elif 600 <= weather_id <= 622:
            return "❄️"                   # 600 - 622 = Snow
        elif 700 <= weather_id <= 780:
            return "🌬️"                   # 700 - 781 = Atmosphere (701=Mist;711=Smoke;721=Haze;741=Fog; etc.)
        elif weather_id == 781:
            return "🌪️"                   # 781 = Tornado
        elif weather_id == 800:
            return "☀️"                   # 800 = Clear
        elif 801 <= weather_id <= 804:
            return "☁️"                   # 801 - 804 = Clouds
        else:
            return ""                      # else ^^ empty string


if __name__ == "__main__":          
    app = QApplication(sys.argv)    
    weather_app = WeatherApp()     
    weather_app.show()             
    sys.exit(app.exec_())          