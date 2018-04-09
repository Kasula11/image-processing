

Prerequisites

Python 2.7
Open cv
Numpy
Pillow


How to Install?


In order to install this Project You need to have Python 2.7 if not you can install it from https://www.python.org/


After install of Python you need configure path variables and set path to your newly installed python root folder

set the path to the below directories

C:\Python27\Scripts
C:\Python27

1.) setting up path You need to configure pip. To install pip you can either type command python get-pip.py. 

2.) Installing open cv. The Best way to install open cv is the link given below.

http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html
or 
https://sourceforge.net/projects/opencvlibrary/files/

3.) Installing Numpy. You can install numpy in your machine by entering this command pip install numpy

4.) After installation, open Python IDLE. Enter import numpy and make sure Numpy is working fine.

5.) Goto opencv/build/python/2.7 folder.

Copy cv2.pyd to C:/Python27/lib/site-packeges.

Open Python IDLE and type following codes in Python terminal.

>>> import cv2
>>> print cv2.__version__
