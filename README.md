RPG-Monocular-Pose-Estimation-ME495-HW2
=======================================

RPG Monocular Pose Estimation. ME495 HW2
Group: Chukwunyere Igbokwe and Sabeen Admani

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
    1. At minimum, 4 IR LEDs

    2. Electronic prototyping materials

    3. An IR filter that has a frequency below the frequency of the LEDs that you chose ([IR 760 HD IR FILTER](http://www.amazon.com/NEEWER%C2%AE-760nm-Infrared-Infra-Filter/dp/B003TY10AS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1415146287&sr=1-1&keywords=neewer+10000314)

    4. A webcam ([Microsoft Lifecam Studio](http://www.microsoft.com/hardware/en-us/p/lifecam-studio/Q2F-00013)) 

##Package Installation##
###Dependencies###

1. Robot Operating System [(ROS)](http://wiki.ros.org/ROS/Installation): 
 
ROS Indigo is the version of ROS that we are using. You can follow the instructions to instal ROS with the following link, and then set up a Catkin Workspace using these [instructions](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

2. [OpenCV](http://opencv.org/) and [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page) are necessary for the package to run, so you need to run those as well
   -OpenCV is used by the package for image processing on the incoming image data stream
   -Eigen is used for linear algebra calculations for the IR LED locating algorithm

###RPG Monocular Pose Estimator Package Installation###

You can clone the package using the commands below:
```
cd catkin_workspace/src
git clone https://github.com/uzh-rpg/rpg_monocular_pose_estimator.git
cd ../
catkin_make
```
###USB_CAM OR UVC_CAMERA###

In order to obtain real time position tracking, you will need to allow for a way for the package to interface with the webcam you are using. To do this, you can install either the [usb_cam](http://wiki.ros.org/usb_cam) or [uvc_camera]( http://wiki.ros.org/uvc_camera) packages. This can be done by typing in the following commands:

```
sudo apt-get install ros-indigo-usb-cam

OR

sudo apt-get install ros-indigo-uvc-camera
```
Check whether they installed properly with:
```
dpkg -l | grep usb_cam

dpkg -l | grep uvc_camera
```

##Configure Camera##

Because we are using our camera for precision position detection, we need to ensure that the camera is appropriately calibrated. You can follow the appropriate steps to calibrate your camera using the following [link](http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration)

In our case, it was a bit difficult to connect to our camera at times. Also, it is important to note tha the camera you are using may change names when you plug/unplug it or restart your computer. The following steps will help you find out what the name of your device is and testing it from the command lines.

In order to find out what devices are plugged into your computer, type in:

```
lsusb
dmesg | tailh
```

Next, (if you don't already have it), install gnome-media. From gnome-media, Gstreamer will allow you to view which video and audio devices are connected, and test each of them. Note: this is really handy when you cannot tell when you cannot tell which device is your built-in camera and which is externally plugged in.
```
sudo apt-get install gnome-media
gstreamer-properties
```
  1. Select video tab
  2. Select webcam device "test"
  3. Select video4linux (1) not (2) & "test"

From this, we were also able to set our webcam as the default, and were able to test that with Cheese. You can confirm that the name by removing the webcam and checking the devices again with:
```
cd /dev
ls
```
If you search for "video" in that list, take note of the number after it; it will most likely be 0 or 1. Plug in your webcam and then type:
```
ls
```
There will be another video term with a number after it- that is your webcam’s ID.

##Test Camera and USB_CAM Package##

Launch ROS by typing the following into the commandline:
```
roscore 
```
In a new terminal run the usb_cam_node with: 
```
rosrun usb_cam usb_cam_node _video_device:=/dev/video#
```
*Note: # is the number you found out that is associated with your webcam

Then, in a new terminal type to view the image:
```
rosrun image_view image_view image:=usb_cam/image_raw
```
A window should pop up now displaying real-time video from your webcam.
To check what topics are being published type "rostopic list" into the terminal:
```
rostopic list
````
The result should be:
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
##Testing the Software##

Within the RPG Monocular Pose Estimator package, there is a demo launch file. This launch file has been developed to open and play a video that was pre-recorded as a bagfile, rather than having a live video feed. Follow the steps below to test your package with the demo file! 

*Note: the steps on testing the software are taken directly from the [RPG Monocular Pose Estimator Github page](https://github.com/uzh-rpg/rpg_monocular_pose_estimator)


###Create Directory to Save Rosbag File###

```
  roscd monocular_pose_estimator
  mkdir bags
  cd bags
````
###Download Test Rosbag File###
```
  wget http://rpg.ifi.uzh.ch/data/monocular-pose-estimator-data.tar.gz
  tar -zxvf monocular-pose-estimator-data.tar.gz
  rm monocular-pose-estimator-data.tar.gz
````
###Launch the Rosbag File###
```
  roslaunch monocular_pose_estimator demo.launch
````
###Examine the Result###

By launching the demo launch file, we can get a lot of information just through visual inspection. First, we see that the LEDs are circled in red and successfully being tracked as the object is moving. The region of interest has a blue square around it and a coodrdinate frame is attached to the object's origin.

We can find a little more out by running a few different commands.

First, we can find out what topics are being published by looking at rostopic list in the terminl- this would give us a result of:
```
  BLAHHHH
````
Next, we find out which nodes are active using the rosnode list command in a new terminal:
```
  BLAHHHH
````
We can also look at rqt_image_view, which would bring up a GUI from which you can select from different topics. More specifically, we can switch between the looking at the raw image and looking at the image with detections. The command you can use to bring this up is below, as well as a screenshot of the GUI:

```
  BLAHHHH
````

##HARDWARE##

In order to test out the system, we wanted to build hardware that was easy to develop and quick, so more time could be spent on getting the package to function. Thus, we used a breadboard and placed the LEDs on different levels. From the paper, some important things to note when setting up your rig are:
  1. Do _not_ put the LEDs all in the same plane
  2. Do _not_ put the LEDs in a way that is symmetric about your object
  3. The LEDs should be visible from various viewing angles (this is where the breadboard idea is not the most ideal solution)
  4. As mentioned earlier, should have a minimum of 4 LEDs
  5. The LEDs should be bright in the image relative to the background so they can be easily extracted from the rest of the image- this will lead to a more accurate estimate of the position

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
