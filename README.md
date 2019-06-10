# 2-DOF-Arm-sim
Gazebo Simulation of 2 DOF arm, using ROS.

joint_plugin.cc - controls velocity and setangle using ROS. subscribed to a topic /<model_name>/vel_cmd and receives angles in radians

getpose.py - returns pose(coodinates and orientation)

Build folder - contains build files after running 'make', delete and run in '~/2-DOF-Arm-sim/:
$ mkdir build
$ cd build
$ cmake ../
$ make

