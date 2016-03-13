# ev3-mapping
Repository created for the sake of learning. The goal is that the EV3 could create a map of its environment.

### robot kit

The object of this project is a LEGO Mindstorms EV3, using the [EXPLOR3R chassis](http://robotsquare.com/2015/10/06/explor3r-building-instructions/) designed by Laurens Valk.
The code will be implemented in Python, using the [ev3dev operating system](http://www.ev3dev.org/).

But hey, don't get scared! **You don't need to have an EV3 at home to contribute to the project**. The idea is to develop robotics projects where an EV3 is the tester. So, in order to ease the transition between ideas and implementation, we're developing a [quick guide](https://docs.google.com/document/d/1BQL6n_TtwxtuzLo3r-wGgEYh9efFLvU81lJhyMmS0ns/edit?usp=sharing) to program an EV3 with Python.

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
We are listing the paradigms in the [wiki](https://github.com/alesolano/ev3-mapping/wiki).

Currently, we're working on the [Grid map paradigm](https://github.com/alesolano/ev3-mapping/wiki#grid-map).

### code design

We need some classes and functions to attain the milestones. This will be moved to this wiki page: [Grid map API](https://github.com/alesolano/ev3-mapping/wiki/Grid-Map-API)

Classes:

1. DiffRobot.  This class defines a basic differential robot. It needs the port addresses of its two motors, the radius of the wheels and distance between the wheels. It has methods like go_forwards(distance), turn_right(angle) and turn_left(angle).
2. EXPLOR3R. This class inherits DiffRobot, setting port addresses and distances by its default values, along with the inclusion of ultrasonic sensor, with possibility of having touch and color sensors.
3. GridRobot. This class is specific for our project. It inherits EXPLOR3R and has methods like go_forward_cell(), go_backward_cell(), go_right_cell(), go_left_cell(), go_cell(x, y), get_current_cell().
4. GridMap. *Currently pondering*

Functions:

1. roam().

