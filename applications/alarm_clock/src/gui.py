from applications.alarm_clock.src.alarm_clock import AlarmClock
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QTimeEdit,
                             QLineEdit, QComboBox, QListWidget, QMessageBox,
                             QListWidgetItem)
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))


class AlarmClockGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.alarm_clock = AlarmClock()
        self.init_ui()
        self.setup_timer()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle('Alarm Clock')
        self.setGeometry(100, 100, 600, 400)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Current time display
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(QFont('Arial', 24))
        layout.addWidget(self.time_label)

        # Add alarm section
        add_alarm_layout = QHBoxLayout()

        # Time input
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        add_alarm_layout.addWidget(self.time_edit)

        # Description input
        self.description_edit = QLineEdit()
        self.description_edit.setPlaceholderText("Alarm Description")
        add_alarm_layout.addWidget(self.description_edit)

        # Repeat days dropdown
        self.repeat_combo = QComboBox()
        self.repeat_combo.addItems(
            ["No Repeat", "Weekdays", "Weekends", "Every Day"])
        add_alarm_layout.addWidget(self.repeat_combo)

        # Add button
        add_button = QPushButton("Add Alarm")
        add_button.clicked.connect(self.add_alarm)
        add_alarm_layout.addWidget(add_button)

        layout.addLayout(add_alarm_layout)

        # Alarms list
        self.alarms_list = QListWidget()
        layout.addWidget(self.alarms_list)

        # Control buttons
        control_layout = QHBoxLayout()

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_alarm_clock)
        control_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_alarm_clock)
        control_layout.addWidget(self.stop_button)

        self.remove_button = QPushButton("Remove Selected")
        self.remove_button.clicked.connect(self.remove_alarm)
        control_layout.addWidget(self.remove_button)

        layout.addLayout(control_layout)

        # Update alarms list
        self.update_alarms_list()

    def setup_timer(self):
        """Setup timer for updating current time."""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

    def update_time(self):
        """Update the current time display."""
        current_time = QTime.currentTime()
        self.time_label.setText(current_time.toString("HH:mm:ss"))

    def add_alarm(self):
        """Add a new alarm."""
        time = self.time_edit.time()
        description = self.description_edit.text()

        if not description:
            QMessageBox.warning(
                self, "Warning", "Please enter an alarm description")
            return

        # Convert repeat selection to days
        repeat_days = []
        repeat_text = self.repeat_combo.currentText()
        if repeat_text == "Weekdays":
            repeat_days = [0, 1, 2, 3, 4]
        elif repeat_text == "Weekends":
            repeat_days = [5, 6]
        elif repeat_text == "Every Day":
            repeat_days = [0, 1, 2, 3, 4, 5, 6]

        try:
            alarm_id = self.alarm_clock.add_alarm(
                time.toString("HH:mm"),
                description,
                repeat_days if repeat_days else None
            )
            self.update_alarms_list()
            self.description_edit.clear()
            QMessageBox.information(
                self, "Success", f"Alarm added with ID: {alarm_id}")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def remove_alarm(self):
        """Remove the selected alarm."""
        current_item = self.alarms_list.currentItem()
        if current_item:
            # Get alarm ID from item data
            alarm_id = current_item.data(Qt.UserRole)
            if self.alarm_clock.remove_alarm(alarm_id):
                self.update_alarms_list()
                QMessageBox.information(
                    self, "Success", "Alarm removed successfully")
            else:
                QMessageBox.warning(self, "Error", "Failed to remove alarm")

    def update_alarms_list(self):
        """Update the alarms list widget."""
        self.alarms_list.clear()
        alarms = self.alarm_clock.list_alarms()

        for alarm in alarms:
            item_text = f"{alarm['time']} - {alarm['description']}"
            if alarm['repeat_days']:
                item_text += f" (Repeat: {', '.join(alarm['repeat_days'])})"
            item_text += f" - Status: {alarm['status']}"

            # Create and add item correctly
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, alarm['id'])
            self.alarms_list.addItem(item)

    def start_alarm_clock(self):
        """Start the alarm clock."""
        self.alarm_clock.start()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        QMessageBox.information(self, "Success", "Alarm clock started")

    def stop_alarm_clock(self):
        """Stop the alarm clock."""
        self.alarm_clock.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        QMessageBox.information(self, "Success", "Alarm clock stopped")


def main():
    app = QApplication(sys.argv)
    window = AlarmClockGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
