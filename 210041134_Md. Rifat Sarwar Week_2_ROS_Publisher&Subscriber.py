#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def ch_vel(string : String):
    cmd = Twist()
    cmd.linear.x = float(string.data)
    pub.publish(cmd)


if __name__ == "__main__":
    rospy.init_node("read_velocity")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size = 10)
    sub = rospy.Subscriber("/chatter",String,callback=ch_vel)
    
    rospy.spin()
