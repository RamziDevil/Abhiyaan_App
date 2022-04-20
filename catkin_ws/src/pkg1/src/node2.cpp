#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
//defining callback function for subscriber
void WriteToLog(const std_msgs::String::ConstPtr& msg){
    ROS_INFO("Recieved Message : [%s]", msg->data.c_str());
}
int main(int argc, char **argv){
    //initialise ros
    ros::init(argc, argv, "node2");
    ros::NodeHandle n;
    //subscriber object
    ros::Subscriber sub = n.subscribe("team_abhiyaan", 1000, WriteToLog);
    ros::spin();
    return 0;
}