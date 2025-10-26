from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMessageBox, QStyle
import random

class SettingsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self._button = QtWidgets.QPushButton("Click me!")
        self._text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self._tray_icon = QSystemTrayIcon(self)

        self._quit_action = QtGui.QAction("Quit", self)
        self._tray_icon_menu = QtWidgets.QMenu(self)
        self._tray_icon_menu.addAction(self._quit_action)
        self._quit_action.triggered.connect(qApp.quit) # noqa: F821

        self._tray_icon.setToolTip("Linza")
        self._tray_icon.setIcon(QIcon("icon.png"))
        self._tray_icon.setContextMenu(self._tray_icon_menu)
        self._tray_icon.show()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self._text)
        self.layout.addWidget(self._button)

        self._button.clicked.connect(self.magic)



    def closeEvent(self, event):
        if not event.spontaneous() or not self.isVisible():
            return
        if self._tray_icon.isVisible():
            QMessageBox.information(self, "Information",
                                    "Linza will keep running in the background. To fully exit, right-click it in the system tray and press <b>Quit</b>.")
            self.hide()
            event.ignore()

    @QtCore.Slot()
    def magic(self):
        self._text.setText(random.choice(self.hello))