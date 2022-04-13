import threading, time, os, cv2
import numpy as np

import mss
import mss.tools

from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtGui import QFont, QWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from pyqt_timer_label import TimerLabel
from pyqt_transparent_centralwidget_window import TransparentCentralWidgetWindow
from pyqt_svg_icon_pushbutton import SvgIconPushButton

from pyqt_capturer.settingsDialog import SettingsDialog


class Capturer(TransparentCentralWidgetWindow):
    def __init__(self):
        main_window = QMainWindow()
        super().__init__(main_window)
        self.__initVal(main_window)
        self.__initUi(main_window)

    def __initVal(self, main_window):
        self.__top = 0
        self.__left = 0
        self.__width = 0
        self.__height = 0
        self.__t = 0
        self.__record_flag = False

        self.__settingsStruct = QSettings('capturer.ini', QSettings.IniFormat)
        self.__frameColor = self.__settingsStruct.value('frameColor', '#FFFFFF')
        self.__menuColor = self.__settingsStruct.value('menuColor', '#FFFFFF')
        self.__savePath = self.__settingsStruct.value('savePath', os.getcwd())

    def __initUi(self, main_window):
        self.setButtons()
        cornerWidget = self.getCornerWidget()
        lay = cornerWidget.layout()

        recordBtn = SvgIconPushButton(self)
        recordBtn.setShortcut('F6')
        recordBtn.setIcon('ico/video.svg')
        recordBtn.setCheckable(True)
        recordBtn.toggled.connect(self.__recordToggled)

        captureBtn = SvgIconPushButton(self)
        captureBtn.setShortcut('F5')
        captureBtn.setIcon('ico/capture.svg')
        captureBtn.clicked.connect(self.__capture)

        self.__timer_lbl = TimerLabel()
        self.__timer_lbl.setFont(QFont('Arial', 12))
        self.__timer_lbl.setTimerReverse(False)

        settingsBtn = SvgIconPushButton(self)
        settingsBtn.setIcon('ico/settings.svg')
        settingsBtn.clicked.connect(self.__settings)

        lay.insertWidget(0, settingsBtn)
        lay.insertWidget(0, self.__timer_lbl)
        lay.insertWidget(0, recordBtn)
        lay.insertWidget(0, captureBtn)
        lay.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        self.setFrameColor(self.__frameColor)

    def __initScreenGeometry(self):
        w = QWindow()
        r = int(w.devicePixelRatio())

        screen_g = self.window().geometry()

        self.__top = (screen_g.top() + self.getInnerWidget().menuBar().height() + self._margin) * r
        self.__left = (screen_g.left()+self._margin) * r
        self.__width = (screen_g.width()-self._margin*2) * r
        self.__height = (screen_g.height()-self.getInnerWidget().menuBar().height()-self._margin*2) * r

    def __initRecordThread(self):
        self.__t = threading.Thread(target=self.__recordThread,
                                    args=(self.__top, self.__left, self.__width, self.__height, ))

    def __recordThread(self, top, left, width, height):
        with mss.mss() as sct:
            # part of the screen
            monitor = {'top': top, 'left': left, 'width': width, 'height': height}
            # full screen
            name = 'sample.mp4'
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            desired_fps = 30.0
            out = cv2.VideoWriter(name, fourcc, desired_fps,
                                  (monitor['width'], monitor['height']))
            last_time = 0
            while self.__record_flag:
                img = sct.grab(monitor)
                # cv2.imshow('test', np.array(img))
                if time.time() - last_time > 1. / desired_fps:
                    last_time = time.time()
                    destRGB = cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)
                    out.write(destRGB)
                # if cv2.waitKey(25) & 0xFF == ord('q'):
                #     cv2.destroyAllWindows()
                #     break
            cv2.destroyAllWindows()

    def __recordToggled(self, f):
        self.__initScreenGeometry()
        self.__initRecordThread()
        self.__record_flag = f
        if f:
            self.__timer_lbl.start()
            self.__t.start()
        else:
            self.__timer_lbl.stop()

    def __capture(self):
        self.__initScreenGeometry()
        with mss.mss() as sct:
            output = os.path.join(self.__savePath, 'sample.png')
            monitor = {'top': self.__top, 'left': self.__left, 'width': self.__width, 'height': self.__height}
            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    def __settings(self):
        dialog = SettingsDialog()
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            color = dialog.getFrameColor()
            savePath = dialog.getSavePath()
            self.__settingsStruct.setValue('frameColor', color.name())
            self.__settingsStruct.setValue('savePath', savePath)
            self.setFrameColor(color)

    def event(self, e):
        if e.type() == 17:
            self.setFrameColor(self.__frameColor)
        return super().event(e)