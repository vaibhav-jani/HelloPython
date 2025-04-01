from stop_watch import StopWatch
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QListWidget,
                             QListWidgetItem)
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))


class StopWatchGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stop_watch = StopWatch()
        self.init_ui()
        self.setup_timer()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle('Stop Watch')
        self.setGeometry(100, 100, 400, 500)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Time display
        self.time_label = QLabel("00:00:00.000")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(QFont('Arial', 48))
        layout.addWidget(self.time_label)

        # Control buttons
        control_layout = QHBoxLayout()

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_stop_watch)
        control_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_stop_watch)
        self.stop_button.setEnabled(False)
        control_layout.addWidget(self.stop_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_stop_watch)
        control_layout.addWidget(self.reset_button)

        self.lap_button = QPushButton("Lap")
        self.lap_button.clicked.connect(self.record_lap)
        self.lap_button.setEnabled(False)
        control_layout.addWidget(self.lap_button)

        layout.addLayout(control_layout)

        # Laps list
        self.laps_list = QListWidget()
        layout.addWidget(self.laps_list)

    def setup_timer(self):
        """Setup timer for updating display."""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(10)  # Update every 10ms for smooth display

    def update_time(self):
        """Update the time display."""
        self.time_label.setText(self.stop_watch.get_time())

    def start_stop_watch(self):
        """Start the stopwatch."""
        self.stop_watch.start()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.lap_button.setEnabled(True)

    def stop_stop_watch(self):
        """Stop the stopwatch."""
        self.stop_watch.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.lap_button.setEnabled(False)

    def reset_stop_watch(self):
        """Reset the stopwatch."""
        self.stop_watch.reset()
        self.laps_list.clear()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.lap_button.setEnabled(False)

    def record_lap(self):
        """Record a lap time."""
        self.stop_watch.lap()
        self.update_laps_list()

    def update_laps_list(self):
        """Update the laps list widget."""
        self.laps_list.clear()
        for i, lap_time in enumerate(self.stop_watch.get_laps(), 1):
            item = QListWidgetItem(f"Lap {i}: {lap_time}")
            self.laps_list.addItem(item)


def main():
    app = QApplication(sys.argv)
    window = StopWatchGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
