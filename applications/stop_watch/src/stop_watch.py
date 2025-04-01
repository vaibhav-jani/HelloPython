import time
from datetime import datetime
from typing import Optional


class StopWatch:
    """A stopwatch class with millisecond accuracy."""

    def __init__(self):
        self.start_time: Optional[float] = None
        self.elapsed_time: float = 0
        self.is_running: bool = False
        self.laps: list[float] = []

    def start(self) -> None:
        """Start the stopwatch."""
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True

    def stop(self) -> None:
        """Stop the stopwatch."""
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.is_running = False

    def reset(self) -> None:
        """Reset the stopwatch to zero."""
        self.start_time = None
        self.elapsed_time = 0
        self.is_running = False
        self.laps = []

    def lap(self) -> float:
        """Record a lap time."""
        if self.is_running:
            current_time = time.time() - self.start_time
            lap_time = current_time - self.elapsed_time
            self.laps.append(lap_time)
            self.elapsed_time = current_time
            return lap_time
        return 0.0

    def get_time(self) -> str:
        """Get the current time in HH:MM:SS.mmm format."""
        if self.is_running:
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time

        hours = int(current_time // 3600)
        minutes = int((current_time % 3600) // 60)
        seconds = int(current_time % 60)
        milliseconds = int((current_time * 1000) % 1000)

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

    def get_laps(self) -> list[str]:
        """Get all lap times in HH:MM:SS.mmm format."""
        return [f"{int(lap // 3600):02d}:{int((lap % 3600) // 60):02d}:{int(lap % 60):02d}.{int((lap * 1000) % 1000):03d}"
                for lap in self.laps]
