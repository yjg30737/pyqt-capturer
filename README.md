# pyqt-capturer
PyQt application which can capture/record certain area of screen

## Requirements
* PyQt5 >= 5.15.1

## Setup
`pip3 install git+https://github.com/yjg30737/pyqt-capturer.git --upgrade`

## Included Packages
* <a href="https://pypi.org/project/mss">mss</a> - For record and capture
* <a href="https://pypi.org/project/opencv-python">opencv-python</a> - For making video
* <a href="https://numpy.org">numpy</a> - Converting image into array
* <a href="https://github.com/yjg30737/pyqt-timer-label.git">pyqt-timer-label</a> - For recording timer
* <a href="https://github.com/yjg30737/pyqt-transparent-centralwidget-window.git">pyqt-transparent-centralwidget-window</a> - Main frame
* <a href="https://github.com/yjg30737/pyqt-svg-button.git">pyqt-svg-button</a> - For supporting SVG
* <a href="https://github.com/yjg30737/pyqt-color-button.git">pyqt-color-button</a> - Used by Settings Dialog
* <a href="https://github.com/yjg30737/pyqt-color-picker.git">pyqt-color-picker</a> - Used by Settings Dialog
* <a href="https://github.com/yjg30737/pyqt-find-path-widget.git">pyqt-find-path-widget</a> - Used by Settings Dialog

## Detailed Description

![image](https://user-images.githubusercontent.com/55078043/160047499-be3de7f6-663c-4d47-8309-69bdf1565314.png)

This is camera app.

If you click the camera icon it will capture anything inside of the frame and save it as "sample.png" at script folder.

If you click the recorder icon, it will record anything inside of the frame and save it as "sample.mp4" at script folder. But result video is silent currently.

You can see the label next to recorder icon. That is elapsed time from starting record.

You can move/resize the frame.

You can change the frame color and save path in "Settings". (pressing gear icon)

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_capturer import Capturer

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Capturer()
    ex.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/174037790-d08161cd-839e-407c-ac94-f1ecd1338ceb.png)

Captured image

![image](https://user-images.githubusercontent.com/55078043/174037898-e8b4b05e-7183-4de1-8043-e13bd53d0ef8.png)
