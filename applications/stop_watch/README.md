# Stop Watch Application

A Python stopwatch application with millisecond accuracy and lap timing functionality.

## Features

- Millisecond accuracy
- Start, Stop, and Reset functionality
- Lap timing
- Modern GUI interface
- Real-time display updates

## Requirements

- Python 3.8 or higher
- PyQt5 for GUI

## Usage

### GUI Version

Run the GUI version:
```bash
python -m src.gui
```

Features:
- Large, easy-to-read time display
- Start, Stop, Reset, and Lap buttons
- Lap times list
- Updates every 10ms for smooth display

### Controls

- **Start**: Begin timing
- **Stop**: Pause timing
- **Reset**: Clear all times and laps
- **Lap**: Record a lap time (only available while running)

## Time Format

The stopwatch displays time in the format:
```
HH:MM:SS.mmm
```
where:
- HH = Hours (00-99)
- MM = Minutes (00-59)
- SS = Seconds (00-59)
- mmm = Milliseconds (000-999) 