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

Result (Google Chrome main page's Google logo, for example)

![image](https://user-images.githubusercontent.com/55078043/160045489-a7b016cf-0528-4a49-b085-f4e99869d5c4.png)

Captured image

![sample](https://user-images.githubusercontent.com/55078043/160045548-90708381-7870-435d-b750-051533d878a2.png)

If you click the camera icon it will capture anything inside of the frame.

Video goes the same(click the recorder icon), but video is silent. 
