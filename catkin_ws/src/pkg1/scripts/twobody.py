#!/usr/bin/env 
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time

#callback functions for each subscriber to update their positions
def callback1(data):
    global pos1
    pos1=data
    
def callback2(data):
    global pos2
    pos2=data
    

def twobody():
    #we are assuming that there exists two turtles "turtle1" and "turtle2" in the turtlesim node
    #and that they are at (5,8) and (9,3) just so that their orbits are centered  at the centre
    #we are also assuming values for G and thier masses
    rospy.init_node('turtlesim', anonymous=True)
    global pos1
    global pos2
    G=7
    m1=2
    m2=1.5
    vel1 = Twist()
    vel2 = Twist() 
    pos1 = Pose()
    pos2 = Pose()
    #publishers
    pub1 = rospy.Publisher('/turtle1/cmd_vel',
                          Twist, queue_size=10)
    pub2 = rospy.Publisher('/turtle2/cmd_vel',
                          Twist, queue_size=10)
    #subscribers
    rospy.Subscriber('/turtle1/pose',Pose,callback1)
    rospy.Subscriber('/turtle2/pose',Pose,callback2)
    #giving the subscribers enough time to give initial position values
    #or else both the pos will be zero and will show divion by zero error
    time.sleep(1)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        #finding the relative position vector and its magnitude
        rx=pos1.x-pos2.x
        ry=pos1.y-pos2.y
        r2=rx**2 +ry**2
        rospy.loginfo(" %s","Simulation Active :")

        #updating velocity variables of both  turtles according to gravitational force
        vel1.linear.x = G*m2*rx/r2
        vel1.linear.y = G*m2*ry/r2
        vel1.linear.z = 0
        vel1.angular.x = 0
        vel1.angular.y = 0
        vel1.angular.z = 0
        vel2.linear.x = -G*m1*rx/r2
        vel2.linear.y = -G*m1*ry/r2
        vel2.linear.z = 0
        vel2.angular.x = 0
        vel2.angular.y = 0
        vel2.angular.z = 0
        #publishing the velocities
        pub1.publish(vel1)
        pub2.publish(vel2)
        rate.sleep()
 
 
if __name__ == '__main__':
    try:
        twobody()
    except rospy.ROSInterruptException:
        pass