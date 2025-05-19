import sys
from PyQt6.QtWidgets import QApplication, QWidget

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("PrioritiZen")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
