![2024-01-31_13-35](https://github.com/ThickBunBun/Qt5YtDL/assets/81237388/ae3f9c8f-0e3d-4510-b93c-96f34c0f3219)

![Static Badge](https://img.shields.io/badge/Qt5-black?logo=Qt)![Static Badge](https://img.shields.io/badge/Python-black?logo=Python)![Static Badge](https://img.shields.io/badge/YouTube-black?logo=Youtube&logoColor=red)

## About
This is a front end for Pytube python library, written using Qt5 GUI library. 

As of now application has the current functionality:
- User may see the preview of the link they entered
- User may pick between different video quality
- User may enable audio only download
 
## Installation
As of now, producing the executable will require rewriting few of essential code blocks because project wasn't planned for that purpose.
If you plan to test out the app you'll have to clone the repository first. 
```console
git clone "https://github.com/ThickBunBun/Qt5YtDL.git"
```
When it's done, cd to the repository directory, initiate python's virtual environment and install the dependencies.
```console
cd Qt5YtDL
```
```console
python -m venv venv
```
```console
source venv/bin/activate
```
```console
pip install -r requirements.txt 
```
After that you may cd into gui folder and launch the app.
```console
cd ptdlgui
```
```console
python main.py
```
After launching and entering the video link for the first time it will prompt you to connect it to your YouTube account in the console.
"Please open https://www.google.com/device and input code XXX-XXX-XXXX
Press enter when you have completed this step.QCoreApplication::exec: The event loop is already running"
It has to be done only once.

##
![photo_2024-04-17_15-58-02](https://github.com/ThickBunBun/Qt5YtDL/assets/81237388/eaabbb8e-8e36-4759-a292-b01583a54707)
![photo_2024-04-15_21-05-23](https://github.com/ThickBunBun/Qt5YtDL/assets/81237388/a11d83ca-9ee2-47c1-a69d-b181977614c5)

