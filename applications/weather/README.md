# Weather Application

A Python weather application that displays current weather information with icons using the OpenWeatherMap API.

## Features

- Real-time weather data
- Temperature in Celsius
- Weather description with icons
- Feels like temperature
- Humidity percentage
- Wind speed
- City search functionality
- Modern GUI interface

## Requirements

- Python 3.8 or higher
- PyQt5 for GUI
- OpenWeatherMap API key
- requests library

## Setup

1. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Edit `src/config.py` and replace `YOUR_API_KEY` with your actual API key
3. Install dependencies:
   ```bash
   pip install PyQt5 requests
   ```

## Usage

Run the application:
```bash
python -m src.gui
```

### Features

1. **Search Weather**
   - Enter a city name in the search box
   - Click "Search" or press Enter
   - View current weather information

2. **Display Information**
   - City name
   - Current temperature
   - Weather description with icon
   - Feels like temperature
   - Humidity
   - Wind speed
   - Last update timestamp

3. **Weather Icons**
   - Dynamic weather icons based on current conditions
   - Icons for different weather types (sunny, cloudy, rainy, etc.)

## Error Handling

- Input validation for city names
- API error handling
- Network error handling
- Icon loading error handling
- API key validation

## Configuration

The application uses `src/config.py` for configuration:
- API key
- API endpoints
- Other settings

## Note

The OpenWeatherMap API has rate limits for free accounts. Please check their documentation for more details. 