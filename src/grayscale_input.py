#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
cap = cv2.VideoCapture(1)
pub = rospy.Publisher('/monocular_pose_estimator/image_with_detections',Image, queue_size=10)
rospy.init_node('grayscale_camera_output', anonymous=True)


def gray(cv_image):
	while not rospy.is_shutdown():
	    # Capture frame-by-frame
	    ret, frame = cap.read()

	    # Our operations on the frame come here
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

	    # Display the resulting frame
	    gray_image = cv2.imshow('frame',gray)
	    
	#     if cv2.waitKey(1) & 0xFF == ord('q'):
	#         break

	# # When everything done, release the capture
	# cap.release()
	# cv2.destroyAllWindows()
	
def callback(data):
	print data
	cv_image = bridge.imgmsg_to_cv2(image_message, desired_encoding ="passthrough")
	gx,gy,gz = gray(cv_image)
    if cx is not None:
        i = Image()
        i.x = gx
        i.y = gy
        i.z = gz
        image_message = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pub.publish(i)
def listener():	
	rospy.Subscriber('/camera/image_raw',Image,callback)
	rospy.Subscriber('/camera/camera_info',CameraInfo,callback)
	rospy.spin()

if __name__ == '__main__':
	listener()	
