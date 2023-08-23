#/bin/bash

yarp read ... /annabell/output | while read l; do echo "$l" >> AnnabelltoRobot.txt; done
