from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class TaskInputDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Tasks")
        self.layout = QVBoxLayout()
        
        self.task_input = QTextEdit()
        self.layout.addWidget(self.task_input)
        
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_tasks)
        self.layout.addWidget(self.submit_button)
        
        self.setLayout(self.layout)
    
    def submit_tasks(self):
        tasks = self.task_input.toPlainText().splitlines()
        tasks = [task.strip() for task in tasks if task.strip()]
        if not tasks:
            QMessageBox.warning(self, "Warning", "Please enter at least one task.")
            return
        self.tasks = tasks
        self.close()

class ScoringWizard(QWidget):
    def __init__(self, tasks):
        super().__init__()
        self.setWindowTitle("Scoring Wizard")
        self.layout = QVBoxLayout()
        
        self.task_label = QLabel()
        self.task_label.setFont(QFont("Arial", 16))
        self.layout.addWidget(self.task_label)
        
        self.importance_buttons = self.create_buttons(["BIG PROBLEM", "REAL TROUBLE", "SOME TROUBLE", "TOTALLY FINE"])
        self.urgency_buttons = self.create_buttons(["Emergency", "Someone actively waiting", "Someone passively waiting", "No one waiting"])
        self.aversiveness_buttons = self.create_buttons(["I’d actually enjoy it!", "It’s fine", "I really don’t wanna", "NOOOOOO!"])
        
        self.submit_button = QPushButton("Next")
        self.submit_button.clicked.connect(self.next_task)
        self.layout.addWidget(self.submit_button)
        
        self.setLayout(self.layout)
        self.tasks = tasks
        self.current_task_index = 0
        self.show_task()

    def create_buttons(self, labels):
        buttons = []
        for label in labels:
            button = QPushButton(label)
            button.clicked.connect(self.button_clicked)
            self.layout.addWidget(button)
            buttons.append(button)
        return buttons

    def button_clicked(self):
        sender = self.sender()
        print(f"Button clicked: {sender.text()}")

    def show_task(self):
        if self.current_task_index < len(self.tasks):
            self.task_label.setText(self.tasks[self.current_task_index])
        else:
            QMessageBox.information(self, "Info", "All tasks scored.")
            self.close()

    def next_task(self):
        self.current_task_index += 1
        self.show_task()
