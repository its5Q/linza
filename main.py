from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMessageBox, QApplication
from widgets.settings import SettingsWindow
import sys

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("icon.png"))
    app.setApplicationName("Linza")

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Error", "No system tray found, we won't work without it, exiting.")
        sys.exit(1)

    QApplication.setQuitOnLastWindowClosed(False)

    settings_window = SettingsWindow()
    settings_window.resize(400, 300)
    settings_window.show()

    sys.exit(app.exec())