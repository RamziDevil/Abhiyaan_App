#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
int main(int argc, char **argv){
    //initialise ros
    ros::init(argc, argv, "node1");
    ros::NodeHandle n;
    //create a subscriber object to topic team_abhiyaan
    ros::Publisher pub = n.advertise<std_msgs::String>("team_abhiyaan", 1000);
    //publish 1 message per second
    ros::Rate loop_rate(1);
    while (ros::ok())
    {
        std_msgs::String msg;
        //creating message
        msg.data = "Team Abhiyaan rocks:";
        ROS_INFO("%s", msg.data.c_str());
        //publish message
        pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}
