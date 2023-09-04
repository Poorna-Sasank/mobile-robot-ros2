# Working of the Robot
https://youtu.be/WeITjVXg2Gk

# kshoonya-bot
 This repo contains all the required file for the simulation of the kshoonya bot
### The master branch contains the src folder incase that's the only folder we want to clone or review :)

All the packages are stored inside in the src folder
#
To run the simulation just clone the repo to your workspace and use 
>> colcon build --symlink-install

After that just run the command 
>> ros2 launch my_robot_bringup my_robot_gazebo.launch.xml

The simulation runs and check if all the nodes required are running or not
>> ros2 node list # should output the following
<p> >> /collision_detector <br>
>> /diff_drive_controller <br>
>> /gazebo <br>
>> /lidar_scanner <br>
>> /robot_state_publisher <br>
>> /rviz <br>
>> /transform_listener_impl_555e7405eb80 <br> </p>


We can also go to RVIZ2 panel and add a LaserScan visualization by subscribing to "/scan" topic and visualize the LidarScan points and how it avoids them :)



# References
### For sensor plugin and usage
   https://github.com/TheNoobInventor/lidarbot/blob/main/lidarbot_description/urdf/lidar.xacro
   https://classic.gazebosim.org/tutorials?cat=guided_i&tut=guided_i1
   
### For obstacle detection approach
   https://github.com/ROBOTIS-GIT/turtlebot3/blob/ros2/turtlebot3_example/turtlebot3_example/turtlebot3_obstacle_detection/turtlebot3_obstacle_detection.py

### For URDF creation
   https://en.wikipedia.org/wiki/List_of_moments_of_inertia#List_of_3D_inertia_tensors
   https://wiki.ros.org/urdf/Tutorials/Adding%20Physical%20and%20Collision%20Properties%20to%20a%20URDF%20Model
   
### gazebo ros2 differential drive plugin
   https://github.com/ros-simulation/gazebo_ros_pkgs/blob/ros2/gazebo_plugins/include/gazebo_plugins/gazebo_ros_diff_drive.hpp
