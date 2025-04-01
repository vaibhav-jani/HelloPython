from applications.weather.src.weather_service import WeatherService, WeatherData
import requests
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QLineEdit,
                             QMessageBox)
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))


class WeatherGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.weather_service = WeatherService()
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 600, 400)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Search section
        search_layout = QHBoxLayout()
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")
        self.city_input.returnPressed.connect(
            self.search_weather)  # Add Enter key support
        search_layout.addWidget(self.city_input)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_weather)
        search_layout.addWidget(search_button)

        layout.addLayout(search_layout)

        # Weather display section
        self.city_label = QLabel("")
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setFont(QFont('Arial', 24))
        layout.addWidget(self.city_label)

        self.temperature_label = QLabel("")
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setFont(QFont('Arial', 48))
        layout.addWidget(self.temperature_label)

        self.weather_icon_label = QLabel()
        self.weather_icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.weather_icon_label)

        self.description_label = QLabel("")
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setFont(QFont('Arial', 18))
        layout.addWidget(self.description_label)

        # Additional weather info
        info_layout = QHBoxLayout()

        self.feels_like_label = QLabel("")
        self.feels_like_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(self.feels_like_label)

        self.humidity_label = QLabel("")
        self.humidity_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(self.humidity_label)

        self.wind_label = QLabel("")
        self.wind_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(self.wind_label)

        layout.addLayout(info_layout)

        # Status message
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

    def search_weather(self):
        """Search for weather in the specified city."""
        city = self.city_input.text().strip()
        if not city:
            QMessageBox.warning(self, "Warning", "Please enter a city name")
            return

        self.status_label.setText("Fetching weather data...")
        weather_data = self.weather_service.get_weather(city)

        if weather_data:
            self.update_weather_display(weather_data)
        else:
            self.status_label.setText("Failed to fetch weather data")
            QMessageBox.warning(
                self, "Error", "Could not fetch weather data. Please check your API key in config.py")

    def update_weather_display(self, data: WeatherData):
        """Update the weather display with new data."""
        self.city_label.setText(data.city)
        self.temperature_label.setText(f"{data.temperature:.1f}°C")
        self.description_label.setText(data.description.capitalize())
        self.feels_like_label.setText(f"Feels like: {data.feels_like:.1f}°C")
        self.humidity_label.setText(f"Humidity: {data.humidity}%")
        self.wind_label.setText(f"Wind: {data.wind_speed} m/s")
        self.status_label.setText(
            f"Last updated: {data.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

        # Load and display weather icon
        icon_url = self.weather_service.get_icon_url(data.icon)
        try:
            response = requests.get(icon_url)
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.weather_icon_label.setPixmap(
                pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        except Exception as e:
            print(f"Error loading weather icon: {e}")


def main():
    app = QApplication(sys.argv)
    window = WeatherGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
