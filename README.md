# Attendace Project
 This python project uses deep learning facial recogniton to allow users to mark attendance by logging in with their face. After registering with their name and a picture of them It stores this data into a database. 
Next time the program is used it will compare their face to previous registered users.

HOW TO INSTALL REQUIRMENTS

Through making this project ive become aware of a few issues. installing dlib often is a very buggy process depending on operating systems it is reccomended you install cmake and dlib by themselves before installing requirements. 


#FOR MAC 

For Mac it is reccomended to install dlib on an python enviroment version less than 3.12. From my experience 
dlib will not properly install for a version higher than 3.11.5. Python 3.11.5 is reccomended for this project as it has shown to be compatiable with all libraries tested. 

Assuming your python version works 

run these commands first

pip3 install cmake

pip3 install dlib==19.24.2

after run 


#FOR WINDOWS 


If needed please remove dlib line from requirements.txt then install.

install respective requirments by either typing

pip install -r requirements.txt

or

pip install -r requirements_windows.txt

into the terminal directed to the respected folder of this project
It is reccomeded to use 3.11.5 or below at the time of this project due to bugs with python 3.12

The code will use your first/inital webcam of your pc. Thanks for checking my project out
