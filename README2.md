Section A:
>1. The workspace is named 'catkin_ws'
>2. inside the src folder of catkin_ws i have created a package named 'pkg1'
>3. the files for all te questions in section A are in this package itself
>4. the python files are in the scripts folder inside the package and the c++ files are in the src folder
>5. for the first question in Task 2 i have created the publisher and subscriber node in both python and c++
>6. the publisher nodes are named node1.py, node1.cpp and subscribers are node2.py and node2.cpp
>7. i have done the second question in Task 2 in c++. the file is named node3.cpp 
>8. for the python files u might have to make it executable first by going to the directory or folder in which the file is placed then run the command 
>>&emsp;`chmod +x filename.py`
>10. to run any of the files in the package go to the workspace and run the commands
>>&emsp;`catkin_make`\
>>&emsp;`source devel/setup.bash`\
>>&emsp;`rosrun pkg1 filename`
>9. for the turtlesim question first run `roscore`in a new tab and then run  
>`rosrun turtlesim turtlesim_node` in another tab
>10. Then run these commands in another tab
>>&emsp;`rosservice call /reset`\
>>&emsp;`rosservice call /kill turtle1`\
>>&emsp;`rosservice call /spawn 5 8 1 turtle1`\
>>&emsp;`rosservice call /spawn 9 3 2 turtle2`\
>>&ensp;then run the python file "twobody.py"  
-----
Section B:
>1. the cpp file for the first question is named "matrix.cpp"
>2. the file for the second question is "opencv.py" 
>3. the documents for the third question are "sensor.docx" and "3D LiDAR.docx"
   
-----
Bonus Section:
>1. the python file for the first question is "road.py". it's incomplete but i spent a lot of time on this and tried a lot of different approaches. 😞
>2. the document for the section is "sponsor.docx". i have no idea what a sponsor actually does so i just went with my gut. 
>3. i didn't do the third question cause i don't know how to use any designing software but i can learn in a few days if you guys select me 🙂
