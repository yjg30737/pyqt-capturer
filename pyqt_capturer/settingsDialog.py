import os

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QFormLayout, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtCore import Qt, QSettings
from pyqt_color_button import ColorButton
from pyqt_color_dialog import ColorPickerDialog
from pyqt_find_path_widget import FindPathWidget


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__settingsStruct = QSettings('capturer.ini', QSettings.IniFormat)
        self.__frameColor = self.__settingsStruct.value('frameColor', '#FFFFFF')
        self.__menuColor = self.__settingsStruct.value('menuColor', '#FFFFFF')
        self.__savePath = self.__settingsStruct.value('savePath', '.')

    def __initUi(self):
        self.setWindowTitle('Settings')
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        frameColor = QColor(self.__frameColor)
        r, g, b = frameColor.red(), frameColor.green(), frameColor.blue()
        self.__frameColorBtn = ColorButton(r=r, g=g, b=b)

        menuColor = QColor(self.__menuColor)
        r, g, b = menuColor.red(), menuColor.green(), menuColor.blue()
        self.__menuColorBtn = ColorButton(r=r, g=g, b=b)

        self.__frameColorBtn.clicked.connect(self.__showFrameColorDialog)
        self.__menuColorBtn.clicked.connect(self.__showMenuColorDialog)

        colorGrpBox = QGroupBox()
        colorGrpBox.setTitle('Color')

        lay = QFormLayout()
        lay.addRow('Frame Color', self.__frameColorBtn)
        lay.addRow('Menu Color', self.__menuColorBtn)

        colorGrpBox.setLayout(lay)

        savePathGrpBox = QGroupBox()
        savePathGrpBox.setTitle('Save Path')

        self.__findPathWidget = FindPathWidget(self.__savePath)
        self.__findPathWidget.setAsDirectory(True)

        lay = QHBoxLayout()
        lay.addWidget(self.__findPathWidget)

        savePathGrpBox.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(colorGrpBox)
        lay.addWidget(savePathGrpBox)
        lay.setContentsMargins(0, 0, 0, 5)

        topWidget = QWidget()
        topWidget.setLayout(lay)

        okBtn = QPushButton('OK')
        okBtn.clicked.connect(self.accept)

        closeBtn = QPushButton('Close')
        closeBtn.clicked.connect(self.close)

        lay = QHBoxLayout()
        lay.addWidget(okBtn)
        lay.addWidget(closeBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        bottomWidget = QWidget()
        bottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(topWidget)
        lay.addWidget(bottomWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setLayout(lay)

    def __showFrameColorDialog(self):
        dialog = ColorPickerDialog(self.__frameColor)
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            self.__frameColorBtn.setColor(dialog.getColor())

    def __showMenuColorDialog(self):
        dialog = ColorPickerDialog(self.__menuColor)
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            self.__menuColorBtn.setColor(dialog.getColor())

    def getFrameColor(self):
        return self.__frameColorBtn.getColor()
    
    def getSavePath(self):
        return self.__findPathWidget.getFileName()