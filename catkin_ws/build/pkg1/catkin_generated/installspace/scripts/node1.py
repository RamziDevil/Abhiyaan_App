import queue
import rospy
from std_msgs import String



def talk():
    pub=rospy.Publisher('team_abhiyaan',String,queue_size=10)
    rospy.init_node('node1',anonymous=True)
    rate=rospy.Rate(1)
    rospy.loginfo('Publisher Node Started')
    while not rospy.is_shutdown():
        msg="Team Abhiyaan rocks:"
        pub.publish(msg)
        rate.sleep()
if __name__=='__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass

