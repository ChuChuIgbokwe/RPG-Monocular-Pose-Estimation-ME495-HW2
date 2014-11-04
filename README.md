RPG-Monocular-Pose-Estimation-ME495-HW2
=======================================

RPG Monocular Pose Estimation. ME495 HW2
##OBJECTIVES#
* Use the ROS [camera calibration] (http://wiki.ros.org/camera_calibration) package to calibrate the webcam you are given
* Follow the documentation for the package to try and get the package running
 - Build some sort of 3D holder for your LEDs and calculate the transforms between them
 - Build a circuit for powering the LEDs
 - Fine-tune parameters of the tracking algorithm
* Build a ROS package to run the demo


##PRELIMINARY STEPS##

Note: We are under the assumption that you have ROS set up and running on your system. The ROS version we are using is indigo.

1. Read the following publication by the developers of this package:

M. Faessler, E. Mueggler, K. Schwabe, D. Scaramuzza: **A Monocular Pose Estimation System based on Infrared LEDs.** IEEE International Conference on Robotics and Automation (ICRA), Hong Kong, 2014.

2. [Watch this video to see the Monocular Pose Estimator in action!](http://www.youtube.com/watch?v=8Ui3MoOxcPQ)

3. Obtain needed materials:

You will need:
*Note: the specific materials that we used are in parentheses below
1. At minimum 5 IR LEDs
2. Electronic prototyping materials
3. An IR filter that has a frequency below the frequency of the LEDs that you chose (We used a Digital HD Filter
4. A webcam

##NEEDED PACKAGES##

###RPG_MONOCULAR_POSE_ESTIMATOR###


###USB_CAM OR UVC_CAM###

##CONFIGURE CAMERA##

We decided to use the Microsoft LifeCam Studio webcam and we had issuses getting it to capture images

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
In a new terminal run the node with: 
```
rosrun usb_cam usb_cam_node _video_device:=/dev/video#
```
# is the number you found out that is associated with your webcam

Then, in a new terminal type: 
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

##NEEDED DATA##

###DOWNLOAD TEST BAG FILE###

###CREATING DIRECTORY###

##HARDWARE##

###BUILD HARDWARE###

###SETTING UP MARKER_POSITIONS FILE###

Figuring out how to correctly input the XYZ values of each LED into the marker_positions file was the difficult part.

-Through some experimentation and reverse engineering of the image in the publication, we found that, though they had only 4 LED positions in the marker_positions file, there were actually 5 LEDs on the object.
-From this, we realized that one of the LEDs was actually the reference point from which the other LEDs were measured. This was the lowest LED on the object's frame of reference.
-Another important detail to note is that all of the LED position values should be given in meters

##EDIT LAUNCH FILE##



###REMAPPING NODES###

#RUNNING THE PACKAGE#

##RQT_RECONFIGURE##

###Dynamic Reconfigure###

When reconfiguring monocular_pose_estimator:

-Threshold: Needs to be within the range of 80-180 (From paper and experimentation)
-Gaussian sigma: We want the range within which it will not false-detect LEDs where they are not. This value needs to be at or below 1.7
-Minimum blob area: 39 seems to be the upper limit (on a scale to 0-100)
-Maximum blob area: 55 is lower limit (on a scale of 0-1000)
-Max width height distortion: 0.5 is lower limit (on scale of 0-1.0)
-Max circular distortion: 0.5 is lower limit (on scale of 0-1.0)
-Back projection pixel tolerance: 5.0 is lower limit (on scale of 0-10)
-Nearest neighbour pixel tolerance: 7.0, but other values seem to work- not noticeable difference to us (scale of 0-10)
-Certainty threshold: 0.5 is lower limit (on scale of 0-1)
-Valid correspondance: not a noticeable difference, so go with default of 0.7
-Roi border thickness: 10 on scale of 0-200

#CONCLUSIONS#

##RELIABILITY AND SENSITIVITY TO PARAMETERS##

##OBSTACLES ENCOUNTERED##

##UTILITY##


#REFERENCES#
Matthias Faessler, Elias Mueggler, Karl Schwabe and Davide Scaramuzza, **A Monocular Pose Estimation System based on Infrared LEDs,** Proc. IEEE International Conference on Robotics and Automation (ICRA), 2014, Hong Kong. 

#USEFUL LINKS#
