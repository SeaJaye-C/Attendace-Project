# Attendace Project
 This python project uses deep learning facial recogniton to allow users to mark attendance by logging in with their face. After registering with their name and a picture of them It stores this data into a database. 
Next time the program is used it will compare their face to previous registered users.

HOW TO INSTALL REQUIRMENTS & RUN PROPERLY
----------------------------------------------------------------------------------------------
Through making this project ive become aware of a few issues. installing dlib often is a very buggy process depending on operating systems it is reccomended you install cmake and dlib by themselves before installing requirements. 


FOR MAC 
________________________________________________________________________________________________________________
For Mac it is reccomended to install dlib on an python enviroment version less than 3.12. From my experience dlib will not properly install for a version higher than 3.11.5. Python 3.11.5 is reccomended for this project as it has shown to be compatiable with all libraries tested. 

Assuming your python version works (3.11.5 Or below most likely)

run these commands first

pip3 install cmake

pip3 install dlib==19.24.2

afterwards 

pip install -r requirements.txt
while terminal is opened to the directory of the folder.



FOR WINDOWS 
______________________________________________________________________________________________
Simiarly, you want to install cmake and dlib prior to installing requirments

# Installing CMAKE 

initially you can try "pip install cmake" but if this doesn't work follow the guide below

Download the CMake installer and install it: https://cmake.org/download/

Add CMake executable path to the Enviroment Variables:

set PATH="%PATH%;C:\Program Files\CMake\bin"

note: The path of the executable could be different from C:\Program Files\CMake\bin, just set the PATH accordingly.

note: The path will be set temporarily, to make the change permanent you have to set it in the “Advanced system settings” → “Environment Variables” tab.

Restart The Cmd or PowerShell window for changes to take effect.


# Installing DLIB FOR WINDOWS

first try 'pip install dlib' if this doesn't work follow instructions below

Install Dlib wheel for respective python version below
https://github.com/z-mahmud22/Dlib_Windows_Python3.x

add wheel to project folder. Open folder in terminal, Then run

pip install 'file name' 

for example:

for python 3.11
python -m pip install dlib-19.24.1-cp311-cp311-win_amd64.whl


Then Finally with the folder open in terminal
pip install -r requirements.txt




The code will use your first/inital webcam of your pc. Thanks for checking my project out hope you had fun!
