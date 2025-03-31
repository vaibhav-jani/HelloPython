"""
A simple alarm clock application that supports multiple alarms and sound playback.
"""

import datetime
import time
import threading
import platform
import os
import pygame
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import select
import sys


@dataclass
class Alarm:
    """Represents an alarm with its properties."""
    time: datetime
    description: str
    is_active: bool = True
    repeat_days: List[int] = None  # 0 = Monday, 6 = Sunday
    sound_file: str = None

    def __post_init__(self):
        if self.repeat_days is None:
            self.repeat_days = []

    def should_trigger(self) -> bool:
        """Check if the alarm should trigger at the current time."""
        if not self.is_active:
            return False

        current_time = datetime.now()

        if self.repeat_days:
            # For repeating alarms, check if current day is in repeat_days
            return (current_time.hour == self.time.hour and
                    current_time.minute == self.time.minute and
                    current_time.weekday() in self.repeat_days)
        else:
            # For one-time alarms, check exact time
            return (current_time.hour == self.time.hour and
                    current_time.minute == self.time.minute)


class AlarmClock:
    """Main alarm clock class that manages alarms and their triggering."""

    def __init__(self):
        self.alarms: Dict[str, Alarm] = {}
        self.running = False
        self.alarm_thread: Optional[threading.Thread] = None
        self.sound_thread: Optional[threading.Thread] = None
        # Track currently playing alarm
        self.current_alarm: Optional[str] = None
        # Track stopped alarms and when they were stopped
        self.stopped_alarms: Dict[str, datetime] = {}
        # Initialize pygame mixer only when needed
        self._init_mixer()

    def _init_mixer(self):
        """Initialize pygame mixer if not already initialized."""
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
        except Exception as e:
            print(f"Warning: Could not initialize sound system: {e}")

    def add_alarm(self,
                  time_str: str,
                  description: str,
                  repeat_days: List[int] = None,
                  sound_file: str = None
                  ) -> str:
        """Add a new alarm to the system."""
        try:
            # Parse time string (supports both 24h and 12h formats)
            # Only minutes accuracy, don;t count seconds
            alarm_time = datetime.strptime(time_str, "%H:%M")
            if alarm_time < datetime.now():
                alarm_time += timedelta(days=1)

            alarm_id = f"alarm_{len(self.alarms)}"
            self.alarms[alarm_id] = Alarm(
                time=alarm_time,
                description=description,
                repeat_days=repeat_days,
                sound_file=sound_file
            )
            return alarm_id
        except ValueError:
            raise ValueError(
                "Invalid time format ${time_str}. Use HH:MM (24h) or HH:MM AM/PM (12h)")

    def remove_alarm(self, alarm_id: str) -> bool:
        """Remove an alarm by its ID."""
        if alarm_id in self.alarms:
            del self.alarms[alarm_id]
            return True
        return False

    def toggle_alarm(self, alarm_id: str) -> bool:
        """Toggle an alarm's active state."""
        if alarm_id in self.alarms:
            self.alarms[alarm_id].is_active = not self.alarms[alarm_id].is_active
            return True
        return False

    def list_alarms(self) -> List[Dict]:
        """List all alarms with their details."""
        return [
            {
                "id": alarm_id,
                "time": alarm.time.strftime("%I:%M %p"),
                "description": alarm.description,
                "is_active": alarm.is_active,
                "repeat_days": [self._get_day_name(day) for day in alarm.repeat_days],
                "sound_file": alarm.sound_file,
                "status": self._get_alarm_status(alarm_id)
            }
            for alarm_id, alarm in self.alarms.items()
        ]

    def _get_day_name(self, day_num: int) -> str:
        """Convert day number to name."""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
        return days[day_num]

    def _play_sound(self, sound_file: str = None, alarm_id: str = None):
        """Play the alarm sound using pygame."""
        try:
            self._init_mixer()  # Ensure mixer is initialized before playing
            if sound_file and os.path.exists(sound_file):
                # Load and play the sound file
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                # Wait for the sound to finish or key press
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                    if select.select([sys.stdin], [], [], 0.0)[0]:
                        pygame.mixer.music.stop()

            else:
                # Create a simple beep sound using pygame's built-in sound
                sample_rate = 44100
                duration = 0.1  # seconds

                # Create a simple beep sound using a sine wave
                num_samples = int(sample_rate * duration)
                buffer = bytearray(num_samples * 2)  # 16-bit audio

                for i in range(num_samples):
                    # Generate a simple sine wave
                    value = int(32767 * (i / num_samples))
                    buffer[i * 2] = value & 0xFF
                    buffer[i * 2 + 1] = (value >> 8) & 0xFF

                # Create a sound buffer
                sound = pygame.mixer.Sound(buffer=bytes(buffer))
                sound.play()
                # Wait for the sound to finish or key press
                start_time = pygame.time.get_ticks()
                while pygame.time.get_ticks() - start_time < int(duration * 1000):
                    if select.select([sys.stdin], [], [], 0.0)[0]:
                        sound.stop()
                    pygame.time.Clock().tick(10)
        except Exception as e:
            print(f"Error playing sound: {e}")
            # Fallback to terminal bell
            print("\a")

    def stop_sound(self) -> bool:
        """Stop the currently playing sound."""
        try:
            self._init_mixer()  # Ensure mixer is initialized before stopping
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

                return True
            return False
        except Exception as e:
            print(f"Error stopping sound: {e}")
            return False

    def _check_alarms(self):
        """Background thread to check and trigger alarms."""
        while self.running:
            current_time = datetime.now()
            # Print current time with carriage return to update in place
            print(
                f"\rCurrent Time: {current_time.strftime('%H:%M:%S')}", end="", flush=True)

            for alarm_id, alarm in self.alarms.items():

                # Skip if alarm was recently stopped
                if alarm_id in self.stopped_alarms:
                    continue

                if alarm.should_trigger():
                    # Set current alarm
                    self.current_alarm = alarm_id
                    # Print alarm message on a new line
                    print(f"\nALARM: {alarm.description}")
                    # Play sound in the main thread to allow key press detection
                    self._play_sound(alarm.sound_file, alarm_id)
            time.sleep(1)

    def start(self):
        """Start the alarm clock system."""
        if not self.running:
            self.running = True
            self.alarm_thread = threading.Thread(target=self._check_alarms)
            self.alarm_thread.daemon = True
            self.alarm_thread.start()
            print("\nAlarm clock started. Press Ctrl+C to stop.")
            print("Current Time: ", end="", flush=True)

            # Initialize pygame mixer only when needed
            self._init_mixer()

    def stop(self):
        """Stop the alarm clock system."""
        self.running = False
        # Stop any currently playing sound
        try:
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
                if self.current_alarm:
                    self.stopped_alarms[self.current_alarm] = datetime.now()
                self.current_alarm = None
        except:
            pass

        # Wait for the alarm thread to finish
        if self.alarm_thread:
            self.alarm_thread.join()
            self.alarm_thread = None

        # Clean up pygame mixer
        try:
            if pygame.mixer.get_init():
                pygame.mixer.quit()
        except:
            pass
        print("\nAlarm clock stopped.")

    def _get_alarm_status(self, alarm_id: str) -> str:
        """Get the current status of an alarm."""
        if alarm_id == self.current_alarm:
            return "Currently Playing"
        elif alarm_id in self.stopped_alarms:
            return f"Stopped at {self.stopped_alarms[alarm_id].strftime('%H:%M:%S')}"
        elif self.alarms[alarm_id].is_active:
            return "Active"
        else:
            return "Inactive"


def print_header():
    """Print the application header with decorative lines."""
    print("\n" + "=" * 50)
    print("Welcome to the Alarm Clock Application!")
    print("=" * 50 + "\n")


def print_commands():
    """Print available commands with examples."""
    print("Available Commands:")
    print("-" * 50)

    commands = [
        ("ADD", "Add a new alarm", [
            "add 07:30 \"Wake up for work\"",
            "add 09:00 \"Daily meeting\" 0,1,2,3,4",
            "add 12:00 \"Lunch break\" 1,2,3,4,5",
            "add 18:00 \"End of day\" alarm.wav"
        ]),
        ("LIST", "List all alarms", [
            "list"
        ]),
        ("REMOVE", "Remove an alarm", [
            "remove alarm_0"
        ]),
        ("TOGGLE", "Toggle an alarm on/off", [
            "toggle alarm_0"
        ]),
        ("START", "Start the alarm clock", [
            "start"
        ]),
        ("STOP", "Stop the alarm clock", [
            "stop"
        ]),
        ("STOP SOUND", "Stop the currently playing sound", [
            "stop_sound"
        ]),
        ("HELP", "Show this help message", [
            "help"
        ]),
        ("QUIT", "Exit the application", [
            "quit"
        ])
    ]

    for cmd, desc, examples in commands:
        print(f"\n{cmd}: {desc}")
        print("-" * 30)
        for example in examples:
            print(f"  {example}")

    print("\nTime Format:")
    print("-" * 30)
    print("  24-hour: HH:MM (e.g., 07:30)")
    print("  12-hour: HH:MM AM/PM (e.g., 07:30 AM)")

    print("\nRepeat Days:")
    print("-" * 30)
    print("  0 = Monday, 1 = Tuesday, ..., 6 = Sunday")
    print("  Example: 0,1,2,3,4 for weekdays")

    print("\nAdditional Features:")
    print("-" * 30)
    print("  • Press any key to stop the alarm sound")
    print("  • Use 'help' command to show this message again")
    print("  • Live clock display updates every second")

    print("\n" + "=" * 50 + "\n")


def main():
    """Main function to run the alarm clock application."""
    alarm_clock = AlarmClock()

    print_header()
    print_commands()

    try:
        alarm_clock.start()
        while True:
            command = input("\nEnter command: ").strip().split()
            if not command:
                continue

            cmd = command[0].lower()

            if cmd == "quit":
                break
            elif cmd == "help":
                print_commands()
            elif cmd == "list":
                alarms = alarm_clock.list_alarms()
                if not alarms:
                    print("\nNo alarms set.")
                else:
                    print("\nCurrent Alarms:")
                    print("-" * 50)
                    for alarm in alarms:
                        print(f"\nID: {alarm['id']}")
                        print(f"Time: {alarm['time']}")
                        print(f"Description: {alarm['description']}")
                        print(f"Active: {alarm['is_active']}")
                        print(
                            f"Repeat Days: {', '.join(alarm['repeat_days']) or 'None'}")
                        print(
                            f"Sound File: {alarm['sound_file'] or 'Default'}")
                        print(f"Status: {alarm['status']}")
                    print("-" * 50)

            elif cmd == "add":
                if len(command) < 3:
                    print(
                        "\nUsage: add <time> <description> [repeat_days] [sound_file]")
                    print("Examples:")
                    print("  add 07:30 \"Wake up for work\"")
                    print("  add 09:00 \"Daily meeting\" 0,1,2,3,4")
                    print("  add 12:00 \"Lunch break\" 1,2,3,4,5")
                    print("  add 18:00 \"End of day\" alarm.wav")
                    continue

                time_str = command[1]
                description = " ".join(command[2:])
                repeat_days = None
                sound_file = None

                try:
                    alarm_id = alarm_clock.add_alarm(
                        time_str, description, repeat_days, sound_file)
                    print(f"\nAlarm added successfully with ID: {alarm_id}")
                except ValueError as e:
                    print(f"\nError: {e}")

            elif cmd == "remove":
                if len(command) != 2:
                    print("\nUsage: remove <alarm_id>")
                    print("Example: remove alarm_0")
                    continue

                alarm_id = command[1]
                if alarm_clock.remove_alarm(alarm_id):
                    print(f"\nAlarm {alarm_id} removed successfully.")
                else:
                    print(f"\nAlarm {alarm_id} not found.")

            elif cmd == "toggle":
                if len(command) != 2:
                    print("\nUsage: toggle <alarm_id>")
                    print("Example: toggle alarm_0")
                    continue

                alarm_id = command[1]
                if alarm_clock.toggle_alarm(alarm_id):
                    print(f"\nAlarm {alarm_id} toggled successfully.")
                else:
                    print(f"\nAlarm {alarm_id} not found.")

            elif cmd == "start":
                alarm_clock.start()

            elif cmd == "stop":
                alarm_clock.stop()
                alarm_clock.start()

            elif cmd == "stop_sound":
                if alarm_clock.stop_sound():
                    print("\nSound stopped successfully.")
                else:
                    print("\nNo sound is currently playing.")

            else:
                print("\nUnknown command. Type 'help' for available commands.")
                print("Press any key to stop the alarm sound.")

    except KeyboardInterrupt:
        print("\nStopping alarm clock...")
        alarm_clock.stop()
        print("Goodbye!")


if __name__ == "__main__":
    main()
