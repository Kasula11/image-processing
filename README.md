# image-processing
Gui based image processing system. which can detect images faces and recognize it.Gui is made with Python using Tkinter and Image Processing is done using Open cv and Numpy.

Prerequisite
Python 2.7
Open cv
Pillow
Numpy


If you don't have the above Softwares you can download it from below websites.

To get Python 2.7 kindly refer this link https://www.python.org/. We need only python 2.7. The version which are above python 2.7 will not work for our project.


To install pip browse through your's python root directory it would like this C:\Python27 and look for Scripts folder. If your python root folder doesn't contain Script sub folder you can browse to the path C:\Python27\Lib\site-packages and enter the following command in your command prompt

python get-pip.py

After installation of pip:

after you have installed it download the opencv and extract it, go to “opencv/Build/python/2.7/x86” folder and copy “cv2.pyd” file to “c:/python27/Lib/site-packages/” folder.
And now we are ready to use opencv in python. just one single problem is there, Opencv uses numpy library for its images so we have to install numpy library too, Lets do that
Go to start and type “cmd” you will see the command prompt icon right click on it and select “run as administrator” this will bring us to the cmd window,
Now type
“cd c:/python27/scripts/”
hit enter then type
“pip install numpy”
This will install the numpy library in your python packages
Now We Are Ready To Do Some Coding
Go to Start and search “IDLE” and open it
To use opencv we need to import the opencv library first,
import cv2
After that we need to import the numpy library
import numpy as np
so now we can use opencv and numpy in our code
Lets Do Face detection
Now that everything is setup and running lets write a code to detect faces from the webcam.
This is kind of hello world program for opencv
The method that we are going to use in this program is a cascade classifier, which can be loaded with a pretrained xml file, these xml files are hard to train but luckily we dont have to worry opencv already has many of these pretrained classifier ready for face detection.
To use the face detection classifier we need to copy the classifier xml file from the “[opencv extracted folder]/sources/data/haarcascades/”, and then copy the file haarcascade_frontalface_default.xml to your project folder (same location where you will save the python program)
Now thats done we can proceed further
we can load the classifier now
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
let add the video capture object now
cap=cv2.VideoCapture(0)
In the above line VideoCapture has one argument which is device id, for inbuilt webcam its usually ‘0’, and if you have some other webcam you can change that number so see that is your webcam’s Id
so lets test the camera now
ret,img=cap.read()
cv2.imshow('windowname',img)
cv2.waitKey(0)
Image of a persion captured by opencv
looks like its working fine
in the above code we read the image from the video capture object using cap.read() method, it returns one status variable which is just True/False and the captured frame then we used imshow() method to display the image, here first argument is the window name and second argument is the image that we want to display, the third line we used waitKey(10) is used for a delay of 10 milisecond it is important for the imshow() method to work properly
Before using the face detector we need comvert the captured image to Gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Now lets apply the face detector to detect faces in our captured image
faces = detector.detectMultiScale(gray, 1.3, 5)
the above line will get the x,y and height,width of all the faces present in the captured image in a list, So now we have to loop through all the faces and draw rectangle there
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
I think its clear what this code is doing, let me explain the rectangle() the first argument is the input image in which we are going to draw the rectangles, second is the x,y coordinate of the face, then the height and weight, after that we are specifying the color of the line which is in the form of (blue,green,red) and you can adjust the value of each color, the range is 0-255, in this case its a green line, and the last argument is the line thickness
Now that we have marked the faces with green rectangles we can display them
cv2.imshow('frame',img)
cv2.waitKey(0)
image of face detection of a persion
Almost Done!!
now to detect face from the webcam live, we need to create a loop which will get the images form the webcam frame by frame and detect the faces and show them in a window. so if we arrange the above code in a loop it will look like this
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
You can see that I changed the “waitKey” , because it aslo returns the value of the key pressed in the keyboard so we are comparing it with the key ‘q’ if its true the we are breaking the loop
after the program ends we need to release the video capture object and distroy all the windows
cap.release()
cv2.destroyAllWindows()

 
The Complete Face Detection Code In One Piece
import numpy as np
import cv2

detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()


