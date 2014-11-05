#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped

pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size=10)
rospy.init_node('posetoturtle', anonymous=True)

def callback(data):
	p = Twist()	
	p.linear.x = data.pose.pose.position.x
	p.linear.y = data.pose.pose.position.y
	#p.angular.z = data.pose.orientation.w
	pub.publish(p)


def listener():	
	rospy.Subscriber('/monocular_pose_estimator/estimated_pose',PoseWithCovarianceStamped,callback)
	rospy.spin()

if __name__ == '__main__':
	listener()	
