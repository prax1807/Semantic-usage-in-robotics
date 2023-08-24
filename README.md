# Project Description
Semantic descriptions to navigate around in a webot designed map.
Robotics is generalised as physical task performing machines are advanced enough to successfully perform the tasks they are coded for. The question of further research looks at abilities to improving these functionalities or diversifying them. This paper focuses on diversifying the aspect of task performed with reference to descriptors given prior the robots working. 
Task at hand includes environment traversal inside described house and fetching objects located at various locations all over the house. This all is carried out with the aim to guide the robot on taking a particular route with restrictions of travelling across certain rooms and alternatively take different paths.

# Working of the project
A pre trained AI model namely ANNABELL is used with ROS webots to achieve the goal of the dissertation. ANNABELL trained for multiple situations, one of them being a virtual dataset that fed with information provides guidance as per cardinl directions and picking up objects or giving them to people. On the other hand Webot being an IDE making robotic usage on virtual timestep. We run the virtual dataset used in ANNABELL as an input to the webots project that takes inputs of direction moving the robot to the inputted direction from ANNABELL. The input is analysed in webots to act accordingly.

# Implementation
ANNABELL is trained on the virtual dataset contained with the corpus, this trains ANNABELL to navigate in a virtual maze using linguistic input. Achieveing the semantic part of the project we take the output produced by the model for test set(also included with the corpus) to use as input. To connect this output to webots we use YARP(yet another robot platform)

# Running the project
1. Follow setup guide to ANNABELL with yarp enabled. Install yarp with all dependencies included. Install webots for your system.
2. The project uses virtual data set hence use trains ANNABELL to navigate in a virtual maze using linguistic input.
3. 1st Terminal: Open yarp server with the command " yarpserver --write".
4. 2nd Terminal: run annabell on directory containing the virtual data set.
   in annabell load the trained weights form the trained file with the command " .load <file_name>.txt".
   open the yarp port with " .yo ".
5. 3rd Terminal: Navigate to desired directory and run the command "  yarp read ... /annabell/output | while read l; do echo "$l" >> AnnabelltoRobot.txt; done " to get AnnabelltoRobot.txt file having neccesary output.
6. Go back to 2nd Terminal and test a situation ".f test_bring_0.txt".
7. After the run is complete should have confirmations of read and write in yarpserver with AnnabelltoRobot.txt.
8. Open webots.
9. Direct towards opening specific project navigate and open the diss.wbt file.
10. Select the controller to be _.py and have the AnnabelltoRobot.txt file in the directory.
11. Run the simulation in accordance to where the robot is with specified location.

# Technologies used
<a href= "https://github.com/golosio/annabell">ANNABELL </a>: <br>
C++ 70.7%
C 13.3%
Cuda 7.8%
Shell 7.3%
Makefile 0.5%
M4 0.4% 
<br>

<a href= "https://github.com/cyberbotics/webots/tree/master">Webots</a> :<br>
Webots 50%
Python 50%
Python libraries used : Robot, csv , math , numpy
Understanding of Lidar, compass , motors and gps used in robot
math uses atan2 to figure out angles in calculation of compass and headers
<br>

<a href= "https://yarp.it/latest/index.html">YARP: Yet Another Robot Platform</a>
# Future Work

The project supports working of bot in one developed environment. Hence is constricted with the environment and situation that is put forward by ANNABELL. Although the program follows basic structure of following the room in accordance to the coordinates, it can be automated to know when the room changes. The project also discards commands like "pick the object " and "give to butler " hence the improvement on improving on these cases can be a step towards a better robotic model.<br>
Virtual time automation could be possible as YARP supports links with other ROS systems and can be utilised with steps to recognised environment, scan for object, and even take virtual time instruction from ANNABELL and feed instruction to it as well.<br>
Annabell uses multiple maps as in test set has differnet mazes hence the algorithm works on described maze on the ROS which can be improved upon by designing different mazes or refining the algorithm to wokr universally.

# Summary of Contribution

1. Reading ANNABELL output via YARP to use as input in Webots. 
2. Devising a algorithm for shortest distance traversal
3. Understanding of lidar as obstacle detector,Compass and GPS in navigation.
4. Understanding usage of Webots IDE as an ROS.
5. Understanding of ANNABELL as an AI model.

