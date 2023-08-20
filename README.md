# Project Description
Semantic descriptions to navigate around in a webot designed map.
Robotics is generalised as physical task performing machines are advanced enough to successfully perform the tasks they are coded for. The question of further research looks at abilities to improving these functionalities or diversifying them. This paper focuses on diversifying the aspect of task performed with reference to descriptors given prior the robots working. 
Task at hand includes environment traversal inside described house and fetching objects located at various locations all over the house. This all is carried out with the aim to guide the robot on taking a particular route with restrictions of travelling across certain rooms and alternatively take different paths.

# Working of the project
Robotics is generalised as physical task performing machines are advanced enough to successfully perform the tasks they are coded for. The question of further research looks at abilities to improving these functionalities or diversifying them. This paper focuses on diversifying the aspect of task performed with reference to descriptors given prior the robots working. 
Task at hand includes environment traversal inside described house and fetching objects located at various locations all over the house. This all is carried out with the aim to guide the robot on taking a particular route with restrictions of travelling across certain rooms and alternatively take different paths.

# Implementation
We run the virtual dataset used in ANNABELL as an input to the webots project that takes inputs of direction moving the robot to the inputed direction from ANNABELL. The input is analysed in a way to find the straight path to designated coordinate using compass and gps. The path algoeithm spins the the robot to get the right heading which then moves forward on finising the right heading. With achieved traversal we also use lidar imaging to avoid obstacles.

# Technology used
Webots IDE
ANNABELL
YARP: Yet Another Robot Platform
Python for controllers in webots

# Running the project
1. Follow setup guide to annabell and setup for your system with <b>yarp enabled</b>, intall yarp with all dependencies included as well and also install webots for your system.
2. The project uses virtual data set hence running annabell for virtual data set works.
3. 1st Terminal: Open yarp server with the command " yarpserver --write".
4. 2nd Terminal: run annabell on directory containing the virtual data set.
   in annabell load the trained weights form the trained file with the command " .load <file_name>.txt".
   open the yarp port with " .yo ".
5. 3rd Terminal: Navigate to desired directory and run the command "  yarp read ... /annabell/output | while read l; do echo "$l" >> AnnabelltoRobot.txt; done " to get AnnabelltoRobot.txt file having neccesary output.
6. Go back to 2nd Terminal and test a situation ".f test_bring_0.txt".
7. After the run is complete you will have confirmations of read and write in yarpserver with AnnabelltoRobot.txt.
8. Open webots.
9. Direct towards opening specific project navigate and open the diss.wbt file.
10. Select the controller to be _.py and have the AnnabelltoRobot.txt file in the directory.
11. Run the simulation in accordance to where the robot is with specified location.

# Technologies used
ANNABELL : 
C++ 70.7%
C 13.3%
Cuda 7.8%
Shell 7.3%
Makefile 0.5%
M4 0.4%

Webots :
Webots 50%
Python 50%
Python libraries used : Robot, csv , math , numpy
Understanding of Lidar, compass , motors and gps used in robot
math uses atan2 to figure out angles in calculation of compass and headers

# Future Work

# Summary of Contribution


