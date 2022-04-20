#include "ros/ros.h"
#include "std_msgs/String.h"
#include <bits/stdc++.h>
#include <string.h>
//creating a class containing the publisher and subscriber
//using template so that we can publish any type of message (here we r using string)
template<typename PublishT, typename SubscribeT>
class PubSub{
    public:
        PubSub(){}
        PubSub(std::string publishTopicName, std::string subscribeTopicName, int queueSize)
        {
            publisherObject  = n.advertise<PublishT>(publishTopicName,queueSize);
            subscriberObject = n.subscribe<SubscribeT>(subscribeTopicName,queueSize,&PubSub::subscriberCallback,this);
        }
        void subscriberCallback(const typename SubscribeT::ConstPtr& recievedMsg);
    protected:
    ros::Subscriber subscriberObject;
    ros::Publisher publisherObject;
    ros::NodeHandle n;
};
//function to reverse string
std::string revWords(std::string str){ 
    std::string s;
    std::string s1;
    
    for(int i = 0; i < str.length(); ++i){ 
        if(str[i] != ' '){ 
            s = str[i]+s;
        }
        else { 
            s1+=s;
            s1+=" ";
            s = "";
        } 
    } 
    s1+=s;
    return s1;
} 
//defining the subscriber callback function
template<>
void PubSub<std_msgs::String, std_msgs::String>::subscriberCallback(const std_msgs::String::ConstPtr& recievedMsg)
{
    ROS_INFO("Recieved Message: %s",recievedMsg->data.c_str());
    std::string reverse=revWords(recievedMsg->data);
    ROS_INFO("Publishing Message: %s",reverse.c_str());
    std_msgs::String revMsg;
    revMsg.data=reverse;
    //publishing reversed message
    publisherObject.publish(revMsg);
}
int main(int argc, char **argv){
    ros::init(argc, argv, "node3");
    PubSub<std_msgs::String, std_msgs::String> node3("naayihba_maet","team_abhiyaan",100);
    ros::spin();
    return 0;
}