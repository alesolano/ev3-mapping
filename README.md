# ev3-mapping
Repository created for the sake of learning. The goal is that the EV3 could create a map of its environment.

### robot kit

The object of this project is a LEGO Mindstorms EV3, using the [EXPLOR3R chassis] (http://robotsquare.com/2015/10/06/explor3r-building-instructions/) designed by Laurens Valk.
The code will be implemented in Python, using the [ev3dev operating system] (http://www.ev3dev.org/).

### defining milestones

###### Basic Milestones

- [ ] Roaming

We need an algorithm to roam a certain room, in order to complete the map as soon as possible.

- [ ] Odometry

Next, we need to convert the information of motion from the encoders to information of the distance traveled by the robot and its localization.

- [ ] Mapping

Finally, we will asign the data readed from the ultrasonic sensor to the position of the robot at that moment. And we will export this information in an image. This image is our map.

###### Extra milestones

- [ ] Localization

Now, with a complete map of the room, if we locate the root in a random position in the room, it has to be able to recognize where he is. 

- [ ] Mapping using beacons

Odometry is prediction, a lot of errors occur when trying to localize the robot using only information from encoders. We need a little bit of perception to get rid of some uncertainty. We could use the color sensor and put some colored spots in a known location within the room, so the robot could figure out where he is if he pass through one of these colored spots.
This technique could be used to improve the mapping stage.

- [ ] Live mapping

The idea is that we could watch how the map is being created, how it evolves from blank to map while the robot roams the room.

### paradigms

There's no an unique solution to this problem. We can follow different paradigms in order to accomplish the milestones. We should list them and test them to have a better comprehension of the field of robotic mapping and to finish with the best possible solution.
We are listing the paradigms in the [wiki] (https://github.com/alesolano/ev3-mapping/wiki).

Currently, we're working on the [Grid map paradigm] (https://github.com/alesolano/ev3-mapping/wiki#grid-map).
