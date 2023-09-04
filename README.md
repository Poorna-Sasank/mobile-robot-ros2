# kshoonya-bot
# This repo contains all the required file for the simulation of the kshoonya bot
# All the packages are stored inside in the src folder
To run the simulation just clone the repo to your workspace and use 
>> colcon build --symlink-install
# After that just run the command 
>> ros2 launch my_robot_bringup my_robot_gazebo.launch.xml

#The simulation runs and check if all the nodes required are running or not
>> ros2 node list # should output the following
>> /collision_detector
/diff_drive_controller
/gazebo
/lidar_scanner
/robot_state_publisher
/rviz
/transform_listener_impl_555e7405eb80
