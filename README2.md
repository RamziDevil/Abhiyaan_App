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
>>&emsp;`rosservice call /spawn 2 2 1 turtle1`\
>>&emsp;`rosservice call /spawn 11 11 3 turtle2`\
>>&ensp;then run the python file "twobody.py"  
>11. Spawn the turtles at (0,4)(angle 1) and (1,9)(angle 2) to get concentric circles. 
>12. Spawn the turtles at (2,2)(angle 1) and (11,11)(angle 2) to get double helical shape.  
>> <img src="https://github.com/RamziDevil/Abhiyaan_App/blob/bab09e2d671fed320ab9d04ef328545ccb9be319/turtle2.jpg" width="150" height="150"> <img src="https://github.com/RamziDevil/Abhiyaan_App/blob/bab09e2d671fed320ab9d04ef328545ccb9be319/turtle1.jpg" width="150" height="150">
>11. there's a chance that the twobody file will immediately crash the turtles together and the program stops due to division by zero error. 
    if that happens please open turtle_teleop_key in another terminal and move one turtle some distance away, turn its angle and try running the python file again
    

-----
Section B:
>1. the cpp file for the first question is named "matrix.cpp"
>2. the file for the second question is "opencv.py" 
>3. the documents for the third question are "sensor.docx" and "3D LiDAR.docx"
>4.     
-----
Bonus Section:
