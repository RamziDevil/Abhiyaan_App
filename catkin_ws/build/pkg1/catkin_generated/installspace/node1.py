#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def talk():
    #creating a publisher object
    pub=rospy.Publisher('team_abhiyaan',String,queue_size=10)
    rospy.init_node('node1',anonymous=True)
    #to publish twice every second
    rate=rospy.Rate(2)
    rospy.loginfo('Publisher Node Started')
    while not rospy.is_shutdown():
        #creating string message
        msg="Team Abhiyaan rocks:"
        pub.publish(msg)
        rate.sleep()
if __name__=='__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass

