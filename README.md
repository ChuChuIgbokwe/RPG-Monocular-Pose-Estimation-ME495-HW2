RPG-Monocular-Pose-Estimation-ME495-HW2
=======================================

RPG Monocular Pose Estimation. ME495 HW2
##OBJECTIVES#
* Use the ROS [camera calibration] (http://wiki.ros.org/camera_calibration) package to calibrate the webcam you are given
* Follow the documentation for the package to try and get the package running. You will need to do things like
 - Build some sort of 3D holder for your LEDs and calculate the transforms between them
 - Build a circuit for powering the LEDs
 - Fine-tune parameters of the tracking algorithm
* Build a ROS package to run the demo


##PRELIMINARY STEPS#
We decided to use the Microsoft LifeCam Studio wecam and we had issuses getting it to capture images

```lsusb
dmesg | tail
```

and run
```
sudo apt-get install gnome-media
gstreamer-properties
```
select video tab
select webcam device "test"
select video4linux (1) not (2) & "test"

this got our webcam to publish images as the default camera.
Remove the webcam and check see to your computers default webcam with 
```
cd /dev
ls
```

search for video and take note of the number after it. It will most likely be 0 or 1. Plug in your webcam and run 
```
ls
```

there will be another video term with a number after it. That is your webcam’s ID.
install the [usb_cam ROS package] (http://wiki.ros.org/usb_cam) with
```
sudo apt-get install ros-indigo-usb-cam
```
Check it installed properly with
```
dpkg -l | grep usb_cam
```
launch ROS with
```
roscore 
```
In a new terminal run the node with 
```
rosrun usb_cam usb_cam_node _video_device:=/dev/video#
```
# is the number you found out that is associated with your webcam.
in a new terminal 
```
rosrun image_view image_view image:=usb_cam/image_raw
```
A window should pop up now displaying images from your webcam.
To check what topics you are publishing 

```
rostopic list
````
which should give you 
```
/rosout
/rosout_agg
/usb_cam/camera_info
/usb_cam/image_raw
/usb_cam/image_raw/compressed
/usb_cam/image_raw/compressed/parameter_descriptions
/usb_cam/image_raw/compressed/parameter_updates
/usb_cam/image_raw/compressedDepth
/usb_cam/image_raw/compressedDepth/parameter_descriptions
/usb_cam/image_raw/compressedDepth/parameter_updates
/usb_cam/image_raw/theora
/usb_cam/image_raw/theora/parameter_descriptions
/usb_cam/image_raw/theora/parameter_updates
```



Note: We are under the assumption that you have ROS set up and running on your system. The ROS version we are using is indigo.

##NEEDED PACKAGES##

###RPG_MONOCULAR_POSE_ESTIMATOR###

###USB_CAM OR UVC_CAM###

##CONFIGURE CAMERA##

##NEEDED DATA##

###DOWNLOAD TEST BAG FILE###

###CREATING DIRECTORY###

##HARDWARE##

###BUILD HARDWARE###

###SETTING UP MARKER_POSITIONS FILE###

##EDIT LAUNCH FILE##

###REMAPPING NODES###

#RUNNING THE PACKAGE#


#CONCLUSIONS#

##RELIABILITY AND SENSITIVITY TO PARAMETERS##

##OBSTACLES ENCOUNTERED##

##UTILITY##


#REFERENCES#
Matthias Faessler, Elias Mueggler, Karl Schwabe and Davide Scaramuzza, **A Monocular Pose Estimation System based on Infrared LEDs,** Proc. IEEE International Conference on Robotics and Automation (ICRA), 2014, Hong Kong. 

#USEFUL LINKS#
