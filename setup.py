from setuptools import setup, find_packages

setup(
    name='pyqt-capturer',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_capturer.ico': ['cam.svg', 'capture.svg', 'settings.svg', 'video.svg']},
    description='PyQt application which can capture/record certain area of screen',
    url='https://github.com/yjg30737/pyqt-capturer.git',
    install_requires=[
        'PyQt5>=5.15.1',
        'mss',
        'opencv-python',
        'numpy',
        'pyqt-timer-label>=0.0.1',
        'pyqt-transparent-centralwidget-window>=0.0.1',
        'pyqt-svg-button>=0.0.1',
        'pyqt-color-button @ git+https://git@github.com/yjg30737/pyqt-color-button.git@main',
        'pyqt-color-picker>=0.0.1',
        'pyqt-find-path-widget>=0.0.1'
    ]
)