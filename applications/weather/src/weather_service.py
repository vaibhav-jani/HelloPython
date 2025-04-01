from applications.weather.src.config import API_KEY, BASE_URL, ICON_URL
import requests
from typing import Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))


@dataclass
class WeatherData:
    """Data class to hold weather information."""
    temperature: float
    feels_like: float
    humidity: int
    description: str
    icon: str
    wind_speed: float
    city: str
    timestamp: datetime


class WeatherService:
    """Service class to handle weather API calls."""

    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.icon_url = ICON_URL

    def get_weather(self, city: str) -> Optional[WeatherData]:
        """Get weather data for a city."""
        try:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"  # Use metric units
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            return WeatherData(
                temperature=data["main"]["temp"],
                feels_like=data["main"]["feels_like"],
                humidity=data["main"]["humidity"],
                description=data["weather"][0]["description"],
                icon=data["weather"][0]["icon"],
                wind_speed=data["wind"]["speed"],
                city=data["name"],
                timestamp=datetime.fromtimestamp(data["dt"])
            )
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def get_icon_url(self, icon_code: str) -> str:
        """Get the URL for a weather icon."""
        return self.icon_url.format(icon_code)
