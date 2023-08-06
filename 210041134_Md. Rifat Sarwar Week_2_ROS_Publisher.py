#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import random


if __name__ == '__main__':
    rospy.init_node("talker")
    rospy.loginfo("Talker Node started")

    pub = rospy.Publisher("/chatter", String, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = String()
        x = random.randint(-5,5)
        msg.data = str(x)
        pub.publish(msg)
        rate.sleep()
