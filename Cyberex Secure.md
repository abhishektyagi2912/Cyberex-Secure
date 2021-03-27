
`   `**Cyberex Secure**

Cyberex Secure is planned to be a security solution with a wide range of features such as phishing detection, advanced  AI- face recognition while accessing payment gateways, computer generated passwords and automatic sign-in. The software will automatically block and report phishing emails/websites to the government portal so that they can be taken down. The assistant will ask for a prompt to send the report before sending it to the portal. 

Project Status: The majority of the python files required to run the backend have been prepared. Integrating them into a GUI is the further task ahead.

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.001.png)

Password Generation Module 

File:  password\_generator.py

1. This uses “Tkinter” , which is a GUI Package in Python.
1. To run this software, a module called pip install pyperclip needs to be used when code is run in Pycharm or VSCode.
1. The generated code can be of desired length and can be copied to the user’s clipboard.

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.002.png)

`          `Automatic Mail Deletion Module

` `File: autodelete.py

1. This uses : pip install oauth2client
1. Enable the Gmail API (due to Google Security)
1. Download the file and save it to the folder same as the code.

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.003.png)

1. Set the subject of the emails which are not required. (For example : Bank OTPs 
1. In the spot of “<abc@gmail.com>”, put in the website, from which the mails are 

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.004.png)

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.005.png)


Website Blocking Module 

File : phishing.py

Blocking  :

The websites which are coveted by the user needs to be put in the Website List.

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.006.png)

Unblocking :

Navigate to the host file.

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.007.png)

Open the host file and remove the blocked domains as shown in below image.

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.008.png)

Due to the Windows Security, the module needs to be operated by the administrator.Then the module will automatically block the website. 

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.009.png)






Face Recognition 

1. Prerequisites: Install Visual C++ Redistributable Packages  (required to run C++ applications that are built by using Visual Studio)
1. Python modules required:
- pip install opencv-python
- pip install cv2
- pip install face-recognition
1. In the initial setup, the user will be required to give webcam access for the first time. The user will have to register their face through it.
1. ` `It will recognize the face of the person with the webcam and compare it with the registered face and evaluate whether they are the same person. It can also evaluate multiple faces at once. 
1. It uses haarcascades, which are machine learning object detection algorithms to detect faces.

![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.010.png)



![](Aspose.Words.15f817e4-d9c8-4a1e-bb38-b3ab56365d4a.011.png)





