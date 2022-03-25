# pyqt-capturer
PyQt application which can capture/record certain area of screen

## Requirements
* PyQt5 >= 5.15.1

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-capturer.git --upgrade```

## Included Packages
* <a href="https://pypi.org/project/mss">mss</a> - For record and capture
* <a href="https://pypi.org/project/opencv-python">opencv-python</a> - For making video
* <a href="https://numpy.org">numpy</a> - Converting image into array
* <a href="https://github.com/yjg30737/pyqt-timer-label.git">pyqt-timer-label</a>
* <a href="https://github.com/yjg30737/pyqt-transparent-centralwidget-window.git">pyqt-transparent-centralwidget-window</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqt_capturer import Capturer

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Capturer(QMainWindow())
    ex.show()
    sys.exit(app.exec_())
```
