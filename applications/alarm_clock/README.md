# Alarm Clock Application

A simple command-line alarm clock application that supports multiple alarms, repeating alarms, and custom sound files.

## Features

- Set multiple alarms with descriptions
- Support for repeating alarms (daily, weekly)
- Custom sound file support (WAV files)
- Command-line interface
- Background alarm checking
- Toggle alarms on/off
- List all active alarms

## Requirements

- Python 3.6 or higher
- pygame (for sound playback)
- WAV sound files (optional)

## Installation

1. Install the required dependencies:
   ```bash
   poetry add pygame
   ```

## Usage

Run the application:
```bash
python src/alarm_clock.py
```

### Available Commands

1. Add an alarm:
   ```
   add <time> <description> [repeat_days] [sound_file]
   ```
   Example: `add 07:30 "Wake up"`

2. List all alarms:
   ```
   list
   ```

3. Remove an alarm:
   ```
   remove <alarm_id>
   ```
   Example: `remove alarm_0`

4. Toggle alarm on/off:
   ```
   toggle <alarm_id>
   ```
   Example: `toggle alarm_0`

5. Start the alarm clock:
   ```
   start
   ```

6. Stop the alarm clock:
   ```
   stop
   ```

7. Quit the application:
   ```
   quit
   ```

### Time Format

- 24-hour format: `HH:MM` (e.g., `07:30`)
- 12-hour format: `HH:MM AM/PM` (e.g., `07:30 AM`)

### Sound Files

- Supports WAV files for custom alarm sounds
- If no sound file is specified, uses a simple beep sound
- Sound playback is handled by pygame for cross-platform compatibility

## Example Usage

1. Start the application:
   ```bash
   python src/alarm_clock.py
   ```

2. Add a wake-up alarm:
   ```
   add 07:30 "Wake up for work"
   ```

3. Add a repeating alarm for weekdays:
   ```
   add 09:00 "Daily meeting" 0,1,2,3,4
   ```

4. List all alarms:
   ```
   list
   ```

5. Toggle an alarm:
   ```
   toggle alarm_0
   ```

6. Remove an alarm:
   ```
   remove alarm_1
   ```

## Notes

- The application runs in the background to check for alarms
- Press Ctrl+C to stop the application
- Alarms will trigger at the specified time and play the configured sound
- For one-time alarms, if the specified time has already passed, the alarm will be set for the next day
- Custom sound files should be in WAV format for best compatibility 