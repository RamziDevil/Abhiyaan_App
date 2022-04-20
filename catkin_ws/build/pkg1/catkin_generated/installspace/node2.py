#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Recieved Message: %s", data.data)

def listen():
    rospy.init_node('node2',anonymous=True)
    #subscriber object to the topic team_abhiyaan
    rospy.Subscriber('team_abhiyaan',String,callback)
    #spin acts as a sort of a while loop 
    rospy.spin()
if __name__=='__main__':
    try:
        listen()
    except rospy.ROSInterruptException:
        pass

