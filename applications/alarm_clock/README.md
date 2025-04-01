# Alarm Clock Application

A Python alarm clock application that allows you to set multiple alarms with custom sounds and repeat options.

## Features

- Set multiple alarms with custom descriptions
- Support for repeating alarms (weekdays, weekends, or custom days)
- Custom sound file support (WAV format)
- Live clock display
- Key press to stop alarm sound
- Command-line interface
- Graphical User Interface (GUI)

## Requirements

- Python 3.8 or higher
- Poetry for dependency management
- PyQt5 for GUI (optional)

## Installation

1. Clone the repository
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

### Command Line Interface

Run the CLI version:
```bash
python -m src.alarm_clock
```

Available commands:
- `add <time> <description> [repeat_days] [sound_file]`: Add a new alarm
- `list`: List all alarms
- `remove <alarm_id>`: Remove an alarm
- `toggle <alarm_id>`: Toggle an alarm on/off
- `start`: Start the alarm clock
- `stop`: Stop the alarm clock
- `stop_sound`: Stop the currently playing sound
- `help`: Show help message
- `quit`: Exit the application

### Graphical User Interface

Run the GUI version:
```bash
python -m src.gui
```

GUI Features:
- Live clock display
- Easy alarm addition with time picker
- Dropdown for repeat options
- List view of all alarms with status
- Start/Stop controls
- Remove selected alarm
- Status messages for all actions

## Time Format

- 24-hour: HH:MM (e.g., 07:30)
- 12-hour: HH:MM AM/PM (e.g., 07:30 AM)

## Repeat Days

- 0 = Monday
- 1 = Tuesday
- 2 = Wednesday
- 3 = Thursday
- 4 = Friday
- 5 = Saturday
- 6 = Sunday

Example: 0,1,2,3,4 for weekdays

## Additional Features

- Press any key to stop the alarm sound
- Use 'help' command to show available commands
- Live clock display updates every second
- Status tracking for all alarms
- Cross-platform compatibility 