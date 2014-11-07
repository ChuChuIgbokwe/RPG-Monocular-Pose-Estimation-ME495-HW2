RPG-Monocular-Pose-Estimation-ME495-HW2
=======================================
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

    3. An IR filter that has a frequency below the frequency of the LEDs that you chose ([IR 760 HD IR FILTER](http://www.amazon.com/NEEWER%C2%AE-760nm-Infrared-Infra-Filter/dp/B003TY10AS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1415146287&sr=1-1&keywords=neewer+10000314))

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

First, we can run rqt_graph in order to see an overall flow chart of the nodes and topics that are running upon launch. The screenshot below is what we obtained and we made sure that this basic structure at least was present during our debugging process. Below is a screen shot of our rqt_graph for the extension with TurtleSim (described in more detail in "Extension")

![alt text](https://raw.githubusercontent.com/raider64x/RPG-Monocular-Pose-Estimation-ME495-HW2/master/images/rqt_graph.png)

Then, we can find out what topics are being published by looking at rostopic list in the terminal- this would give us a result of:
```
/camera/camera_info
/camera/image_raw
/camera/image_raw/compressed
/camera/image_raw/compressed/parameter_descriptions
/camera/image_raw/compressed/parameter_updates
/camera/image_raw/compressedDepth
/camera/image_raw/compressedDepth/parameter_descriptions
/camera/image_raw/compressedDepth/parameter_updates
/camera/image_raw/theora
/camera/image_raw/theora/parameter_descriptions
/camera/image_raw/theora/parameter_updates
/monocular_pose_estimator/estimated_pose
/monocular_pose_estimator/image_with_detections
/monocular_pose_estimator/image_with_detections/compressed
/monocular_pose_estimator/image_with_detections/compressed/parameter_descriptions
/monocular_pose_estimator/image_with_detections/compressed/parameter_updates
/monocular_pose_estimator/image_with_detections/compressedDepth
/monocular_pose_estimator/image_with_detections/compressedDepth/parameter_descriptions
/monocular_pose_estimator/image_with_detections/compressedDepth/parameter_updates
/monocular_pose_estimator/image_with_detections/theora
/monocular_pose_estimator/image_with_detections/theora/parameter_descriptions
/monocular_pose_estimator/image_with_detections/theora/parameter_updates
/monocular_pose_estimator/monocular_pose_estimator/parameter_descriptions
/monocular_pose_estimator/monocular_pose_estimator/parameter_updates
/rosout
/rosout_agg

````
Next, we find out which nodes are active using the rosnode list command in a new terminal:
```
/camera
/monocular_pose_estimator/monocular_pose_estimator
/monocular_pose_estimator/view_visualisation_image
/rosout
````
We can also look at rqt_image_view, which would bring up a GUI from which you can select from different topics. More specifically, we can switch between the looking at the raw image and looking at the image with detections. The command you can use to bring this up is below:

```
  rosrun rqt_image_view rqt_image_view
````
##Hardware##

In order to test out the system, we wanted to build hardware that was easy to develop and quick, so more time could be spent on getting the package to function. Thus, we used a breadboard and placed the LEDs on different levels. From the paper, some important things to note when setting up your rig are:
  1. Do _not_ put the LEDs all in the same plane
  2. Do _not_ put the LEDs in a way that is symmetric about your object
  3. The LEDs should be visible from various viewing angles (this is where the breadboard idea is not the most ideal solution)
  4. As mentioned earlier, should have a minimum of 4 LEDs
  5. The LEDs should be bright in the image relative to the background so they can be easily extracted from the rest of the image- this will lead to a more accurate estimate of the position

##Software##
###Setting up Marker Positions YAML File###

Figuring out how to correctly input the XYZ values of each LED into the marker_positions file was the difficult part.

-Through some experimentation and reverse engineering of the image in the publication, we found that, though they had only 4 LED positions in the marker_positions file, there were actually 5 LEDs on the object.
-From this, we realized that one of the LEDs was actually the reference point from which the other LEDs were measured; this was the lowest (in the z-direction) LED on the object's frame of reference.
-Another important detail to note is that all of the LED position values should be given in meters relative to the aforementioned lowest LED.

The position values for our LEDs can be seen in the table below:

| LED Number    |      x        |     y       |      z      |
| ------------- |:-------------:|:-----------:|:-----------:|
|       1       |     0.044     |    0.034    |    0.005    |
|       2       |     0.022     |    0.071    |    0.002    |
|       3       |     0.000     |    0.094    |    0.026    |
|       4       |     0.029     |    0.112    |    0.005    |

###Edit Launch File###

We ran into issues running the actual software (details to be discussed in the "Obstacles Encountered" section). However, because of the issues we ran into, we decided to make two different Launch files. The general launch file on the Github for this project is below. Also, note that you will have to replace the name of the YAML file that is being called by the launch file with the name of your new YAML file that was created above.

```
 <launch> 

    <!-- Name of the YAML file containing the marker positions -->
    <arg name="YAML_file_name" default="marker_positions"/>

    <!-- File containing the the marker positions in the trackable's frame of reference -->
    <arg name="marker_positions_file" default="$(find monocular_pose_estimator)/marker_positions/$(arg YAML_file_name).yaml"/> 

    <node name="monocular_pose_estimator" pkg="monocular_pose_estimator" type="monocular_pose_estimator" respawn="false" output="screen"> 
        <rosparam command="load" file="$(arg marker_positions_file)"/>
        <param name= "threshold_value" value = "140" />
        <param name= "gaussian_sigma" value = "0.6" />
        <param name= "min_blob_area" value = "10" />
        <param name= "max_blob_area" value = "200" />
        <param name= "max_width_height_distortion" value = "0.5" />
        <param name= "max_circular_distortion" value = "0.5" />
    </node>
</launch> 
````
The first option was to have a launch file that did what was intended by the project- to make it work with a real time video stream. In order to do this, we had to add in a block of code that would launch the usb_cam_node. This block of code is seen below- be sure to tune the parameters (particularly size of the image and image type):

```
  <node name="camera" pkg="usb_cam" type="usb_cam_node" output="screen" >
	    <param name="video_device" value="/dev/video0" />
     <param name="image_width" value="320" />
    	<param name="image_height" value="240" />
	    <param name="pixel_format" value="yuyv" />
	    <param name="camera_frame_id" value="usb_cam" />
	    <param name="io_method" value="mmap"/>
	</node>
	
```

The next option is to be able to play a rosbag file that you prerecorded. This a more simple change since the demo.launch file is already written to play a Rosbag file on loop, so you only have to change the name of the Rosbag file that is called. The tricky part was getting the Rosbag file to be an appropriate one to be ran with this package, but details about this will be discussed in the "Obstacles Encountered" section.

##RUNNING THE PACKAGE##

After deciding which method you would like to run it (real-time video or pre-recorded video in rosbag file), you need to launch the appropriate launch file for the package.

###RQT_RECONFIGURE###

We have the ability to fine-tune the paramters by using rqt_reconfigure with the command below.
```
  rosrun rqt_reconfigure rqt_reconfigure
```
####Dynamic Reconfigure####

When reconfiguring monocular_pose_estimator, we were able to confirm the limits and ranges that we saw on the Github page for the package- for the most part, the values were identical or very close.

-Threshold: Needs to be within the range of 80-180

-Gaussian sigma: This value needs to be at or below 1.7. We want the range within which it will not false-detect LEDs where they are not

-Minimum blob area: 39 seems to be the upper limit (on a scale to 0-100)

-Maximum blob area: 55 is lower limit (on a scale of 0-1000)

-Max width height distortion: 0.5 is lower limit (on scale of 0-1.0)

-Max circular distortion: 0.5 is lower limit (on scale of 0-1.0)

-Back projection pixel tolerance: 5.0 is lower limit (on scale of 0-10)

-Nearest neighbour pixel tolerance: 7.0, but other values seem to work- not noticeable difference to us (scale of 0-10)

-Certainty threshold: 0.5 is lower limit (on scale of 0-1)

-Valid correspondance: not a noticeable difference, so go with default of 0.7

-ROI border thickness: 10 on scale of 0-200

##RELIABILITY AND SENSITIVITY TO PARAMETERS##

##Extension##

We were successfully able to get the TurtleSim to move by using input from the RPG Monocular Pose Estmator- it was incredibly exciting!!! However, we know that there is a lot of work to be done yet. 

###How it works###

First, we created a python node in ROS called _posetoturtle_ which subscribes to /monocular_pose_estimator/estimated_pose and publishes the x and y positions to /turtle1/cmd_vel. We learned by doing a rostopic echo on the latter topic that the pose data is outputted in the form of a [covariance vector](http://docs.ros.org/api/geometry_msgs/html/msg/PoseWithCovariance.html). Thus, we needed to extract the data that was outputted from that vector and place it into a twist vector that we then published to the /turtle1/cmd_vel node, since it is listening for data of the geometry messages, twist type. Important to note, however, is that we are not using the orientation data that is a component of the pose with covariance vector, just simply the position data. Though this is a good first step, we know that we need to do some appropriate calculations for the usage of the rotation about the x, y, and z axes to control the orientation of the turtle (or, in other applications, the direction of the object to-be-controlled).

###To use###

You can clone this repository and follow the instructions above for setting the hardware and software up. Within the repository, there is a launch file that can be used to start up our _posetoturtle_ node, as well as the monocular pose estimator and usb_cam nodes.

##Obstacles Encountered##

Unfortunately, we ran into a few different speedbumps while trying to run the package with anything other than the demo rosbag file. For that reason, we thought it would be a good idea to create our own rosbag file to rule out whether the errors we were getting were due to our use of the external camera and usb_cam package, or something else. In order to find out what topics the rosbag file was subscribed to, we went to the bags directory and used to the rosbag info command to find out more details about the file.
```
  rosbag info demo_test.bag
```
Afterward, we found out that the bag was subscribed to /camera/camera_info and /camera/image_raw. This is important to note because we now knew what data the package was expecting receive from the rosbag file (and subsequently the correct topics we needed to subscribe to while recording our own rosbag file). Our inital thought was to rosrun the usb_cam package and node but we realized that, had we recorded it from there, the names of the topics of the rosbag would have been /usb_cam/camera_info and /usb_cam/image_raw, which is not what the monocular_pose_estimator node is expecting. Thus, in the interest of not having to modify the launch file to remap the name of the node from /camera to /usb_cam, we ended up simply starting up our launch file that works with real-time video and recording with that.

 In a new terminal, type:
```
  rosbag record /camera/image_raw /camera/camera_info
  
  ctrl+c to stop the recording after about 25-30 seconds (though you could do shorter or longer)
```
We immediately noticed that our images kept freezing, and that this was not allowing us to see the detection. Our short-term fix was to look at the feed using rqt_image_view, but long term, we learned that there was actually a bug in the old version of image_view; this bug had been fixed recently, but was not yet on the ROS wiki, so you have to obtain the fix from Github.

However, after this, we noticed that we were finally getting some detections on our image, albeit incorrectly detected. Because of this, we adjusted the parameters dynamically using rqt_reconfigure and the detection did improve (screenshot below). 

![alt text](https://raw.githubusercontent.com/raider64x/RPG-Monocular-Pose-Estimation-ME495-HW2/master/images/successful_led_location_bag.png)

We noticed when we checked on the frequency with which the /monocular_pose_estimator/image_with_detections node was publishing compared to the /camera/image_raw node and found that the former was barely publishing at a rate of 2 Hz vs. 30 Hz of the latter. Running rostopic hz on those nodes with the demo rosbag file running, we see that the rate was around 30 Hz for both, indicating something was wrong from the video that we were recording. We tweaked a few different things (changed the image size, the shutter time, and the gain) and, though they improved the publishing rate of the slower node, they didn't help significantly. Our instructor brought up an important point that the fact that our camera feed was RGB color vs. monochrome may actually be impacting that rate. 

![alt text](https://raw.githubusercontent.com/raider64x/RPG-Monocular-Pose-Estimation-ME495-HW2/master/images/iamge_raw%20vs%20Image_with_detections.png)

*This photo is a screenshot of the rate at which our /monocular_pose_estimator/image_with_detections node was publishing

After looking into it further, we noticed that the package is indeed optimized for monochrome/grayscale images. There were three options that we learned could make the camera/image_raw data go from RGB to grayscale images:

1. USB_CAM

The usb_cam node has a parameter for setting pixel format, and one of the options is yuvmono10. We tried this option, but the raw images that resulted were of very low quality- the LEDs could not be distinguished, or even seen, in the raw image file.

2. [image_proc](http://wiki.ros.org/image_proc)

This is a package that essentially is built to sit between the camera driver and the image processing node. The first step in running the package is providing a NAMESPACE to make it a part of.

```
ROS_NAMESPACE=my_camera rosrun image_proc image_proc
```
Afteward, you can open a new terminal and use image_view to look at the new camera data.
```
rosrun image_view image_view image:=my_camera/image_mono
```

In our particular case, this node would sit between the usb_cam node and the monocular_pose_estimator node. We would be putting this in the namespace of the camera, so that all of the data is being published as /camera/_____ topics.

Though this resulted in a very high quality monochrome image, we were still unable to get the turtle working faster than 8 Hz (which is a significant improvement over the 1-2 Hz we were getting previously. It is important to also note that a lot of messages are still not being published so this change did not drastically improve anything, but rather increases the peak publishing rate. Also, while using grayscale, we noticed that, every time we put our IR filter over the camera, the image would freeze and the node would stop sending data; we're not sure why this is happening, but its use does become a little counter-productive. We also noticed that the node performs best in low light conditions, thought this isn't necessary.

![alt text](https://github.com/raider64x/RPG-Monocular-Pose-Estimation-ME495-HW2/blob/master/images/lifecam_mono.png)

The image above is for grayscale with low light conditions and the image below is grayscalee with the IR filter.

![alt text](https://github.com/raider64x/RPG-Monocular-Pose-Estimation-ME495-HW2/blob/master/images/detections_mono_with_box.png)

3. [open_cv node](http://opencv.org/documentation.html):

Alternatively, we could write an OpenCV node that would get the grayscale image, but we believe that the built in image_proc package would most likely do a better job. Nonetheless, we would like to explore this option in more details.

Lastly, we noticed that the laptoop's built in webcam performs better than the Microsoft Lifecam Studio camera that we used.
##Utility##

This package can be _extremely_ useful if the smaller run issues are hammered out (we hope to have the monochrome issue tested and fixed soon). As the paper states, this is a very robust and accurate way to detect changes in position. The extension that we described above would show an example of how you can use the position of one object to control another.

##Conclusions##

###Next Steps###

We would ultimately like to take this project to one step beyond this and see how different variables in the system (external as well as factors relating to software) affect the image with detections output. For example, want to test the difference in the output images with detections and publish rate of the /monocular_pose_estimator/image_with_detections node as well as whether different filters and different LEDs would impact the output we are getting positively or not. We still believe that there is a reason for the bottleneck of information that is happening between the usb_cam and monocular_pose_estimator node and would like to spend more time on figuring out why that is.

##References##
Matthias Faessler, Elias Mueggler, Karl Schwabe and Davide Scaramuzza, **A Monocular Pose Estimation System based on Infrared LEDs,** Proc. IEEE International Conference on Robotics and Automation (ICRA), 2014, Hong Kong. 
