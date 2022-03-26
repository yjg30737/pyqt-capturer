from PyQt5.QtWidgets import QDialog, QFormLayout, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtCore import Qt, QSettings
from pyqt_color_button import ColorButton
from pyqt_color_dialog import ColorPickerDialog
from pyqt_find_path_widget import FindPathWidget


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Settings')
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.__frameColor = ColorButton()
        self.__menuColor = ColorButton()

        self.__frameColor.clicked.connect(self.__showFrameColorDialog)
        self.__menuColor.clicked.connect(self.__showMenuColorDialog)

        colorGrpBox = QGroupBox()
        colorGrpBox.setTitle('Color')

        lay = QFormLayout()
        lay.addRow('Frame Color', self.__frameColor)
        lay.addRow('Menu Color', self.__menuColor)

        colorGrpBox.setLayout(lay)

        savePathGrpBox = QGroupBox()
        savePathGrpBox.setTitle('Save Path')

        findPathWidget = FindPathWidget()

        lay = QHBoxLayout()
        lay.addWidget(findPathWidget)

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
        dialog = ColorPickerDialog()
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            self.__frameColor.setColor(dialog.getColor())

    def __showMenuColorDialog(self):
        dialog = ColorPickerDialog()
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            self.__menuColor.setColor(dialog.getColor())

    def getFrameColor(self):
        return self.__frameColor.getColor()