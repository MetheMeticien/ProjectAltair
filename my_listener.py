#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import random
from turtlesim.msg import Pose

def read_val(string:String):
    rospy.loginfo(string)
    


if __name__ == "__main__":
    rospy.init_node("my_listener")
    sub = rospy.Subscriber("/chatter",String, callback = read_val)
    
    
    rospy.spin()