from setuptools import setup, find_packages

setup(
    name='pyqt-capturer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_capturer.ico': ['capture.svg', 'settings.svg', 'video.svg']},
    description='PyQt application which can capture/record certain area of screen',
    url='https://github.com/yjg30737/pyqt-capturer.git',
    install_requires=[
        'PyQt5>=5.15.1',
        'mss',
        'opencv-python',
        'numpy',
        'pyqt-timer-label @ git+https://git@github.com/yjg30737/pyqt-timer-label.git@main',
        'pyqt-transparent-centralwidget-window @ git+https://git@github.com/yjg30737/pyqt-transparent-centralwidget-window.git@main',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main'
    ]
)