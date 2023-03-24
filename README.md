# vehicle-and-pedestrian-recognition-software

1. To run the program you'll need to install the following software:
*Install python your computer /machine.
To install Python: You can download the latest version of Python from the official website (https://www.python.org/downloads/). Make sure to install the version that matches your operating system.

*Get pip python manager.
 -On Mac or Ubuntu run the following command on your terminal(AFTER FIRST INSTALLING PYTHON):
    sudo apt-get install python-pip

 -On Windows run the following command on your terminal(AFTER FIRST INSTALLING PYTHON):
    python get-pip.py


*Install OpenCV: You can install OpenCV using pip, the Python package manager. Open a command prompt or terminal window and run the following command:
RUN:
pip install opencv-python
This will install the latest version of OpenCV and all its dependencies.

Once you have installed these dependencies, you should be able to run the Python program that identifies cars and pedestrians using OpenCV.

Though I programmed the software  in python3, it should work on any other python version. If it doesn't work your python version, install python 3 and run it using the python3.


2. RUNNING THE PROGRAMS AND EXPECTED OUTPUT:    *NB: The dollar sign($)[where written] is not part of the commands to be written in the command prompt line/terminal in order to run any of the programs.


First configure git/github on your machine.
Clone this github repository to your machine by running the following command on your terminal:
        git clone git@github.com:Bethwel-Kipruto/vehicle-and-pedestrian-recognition-software.git



Once successfully cloned, change your directory into the location where you have cloned the git folder/repository containing the programs.
YOU MAY NOW RUN THE ANY OF THESE PROGRAMS ON YOUR TERMINAL THROUGH THE FOLLOWING COMMANDS:


                    RUNNING THE FIRST PRORAM PRESENT IN OUR FOLDER.
    1. To run the PROGRAM THAT USES YOUR DEVICE'S CAMERA TO IDENTIFY VEHICLES AND PEDESTRIANS IN REAL TIME, run :$python carrecognitionbycamera.py or
    $python3 carrecognitionbycamera.py on your terminal   -->once you run this , your camera will switch on and once a vehicle or pedestrian is located in your camera's view,you will see a red rectangle around the vehicle and a green rectangle around the pedestrians



                    RUNNING THE SECOND PROGRAM PRESENT IN OUR FOLDER.
    2.To run the PROGRAM THAT TAKES IN AN IMAGE AND IDENTIFIES VEHICLES AND PEDESTRIANS IN THE IMAGE, open your cloned repository in an IDE like VScode then open the carecognitionbyimage.py file. On line 5 of the file you should add the literal path of an image already present on your computer in between the quotation marks. eg.'/Users/bethwel/Desktop/cars.jpg'
    *save this change made(adding the path of your preffered image on line 5) by pressing [ctrl+s] on Windows or [command+s] on Mac.
    *Open your terminal and write this command $python carecognitionbyimage.py or $python3 carecognitionbyimage.py
    -->Once you run this on your terminal you should see your image pop up. If a vehicle is present in the image, a red rectangle will be present around it and if a pedestrian is present in the image, a green rectangle will be present around the pedestrian.



                    RUNNING THE THIRD PROGRAM PRESENT IN OUR FOLDER.

    3.To run the PROGRAM THAT TAKES IN A VIDEO AND IDENTIFIES VEHICLES AND PEDESTRIANS IN THE VIDEO, open your cloned repository in an IDE like VScode then open the carecbyvideo.py file. On line 3 of the file you should add the literal path of a video already present on your computer in between the quotation marks(line 3). eg.'/Users/bethwel/Desktop/pedestandcars.mp4'
    *save this change made(adding the path of your preffered video on line 3) by pressing [ctrl+s] on Windows or [command+s] on Mac.
    *Open your terminal and write this command $python carecbyvideo.py or $python3 carecbyvideo.py
    -->Once you run this on your terminal you should see your video pop up. If a vehicle is present in your video, a red rectangle will be present around it and if a pedestrian is present in the video, a green rectangle will be present around the pedestrian.
                

***3.ACTUAL APPLICATION/CAPABILITY OF THE PROGRAM.
The program is quite accurate in vehicle and pedestrian detection, and once merged with relevant hardware such as a full sized vehicle or any mechanically moving object, it can be used to program an autonomously driven vehicle for collision/accident prevention or during autonomous driving of the vehicle by identifying other vehicles,pedestrians and obstacles within the vicinty of the vehicle. On detecting any object within the car's vicinity through my peogram, the car(or hardware in use) may then be programmed to make any necessary action during the self driving process, such as stopping the vehicle or changing its direction and also increasing the speed of the vehicle where necesseary.***



4.IF THERE ARE ANY QUERRIES, SUGGESTIONS OR COMMENTS ON ANY OF THE PROGRAMS IN THIS REPOSITORY,
    contact the author of the program via email through (bethwelk85@gmail.com)

#************************************************************************************************
ABOUT ME:

My name is Bethwel Kipruto Kangogo, and I am an 18-year-old fresh from high school with a passion for programming, AI, and machine learning. I am constantly exploring new technologies and experimenting with different programming languages to expand my skill set.

I believe that AI and machine learning have the potential to revolutionize the way we go about various different tasks, especially in transport,medicine,agriculture and other vital areas. My goal is to contribute to this revolution by developing innovative AI solutions that can make life easier and better for people around the world.

As someone who is just a month fresh from high school(at the time of publishing this program), I am excited to challenge myself and take on more projects in AI and machine learning. I am always looking for new opportunities to learn and grow, and I am committed to making a positive impact on the world through my work.

Thank you for taking the time to check out my program, and I hope you find it useful.

#************************************************************************************************


LICENSE:

MIT License

Copyright [©2023] [BETHWEL KIPRUTO KANGOGO]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files of my vehicle and pedestrian detection software, to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

