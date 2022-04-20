import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
"""My approach was to get the coordinates of all the points where the image had black color (after binary thresholding) 
and then draw lines from the middle of the images to all 360-degree angle until the line meets a black point. Then find 
the length of the line drawn and plot it against the angle. But I wasn’t able to draw lines in that way. Also, it would 
be difficult to find the distance if I didn’t have the coordinates of the exact point to which the line drawn to. 
I also tried to generate a parabola that approximately matches the boundaries of the road and the draw lines to the parabolas and approach as before.
But sadly i got stuck halfway:(
 """
img=cv.imread("C:/Users/Ramzi/Downloads/4Junc.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
w=img.shape[1] #width
h=img.shape[0] #height
 
# creating a scatterplot from thdata of the image array

points=np.where(img==0)
plt.scatter(points[1],points[0],s=1)



plt.xlim(0,w)
plt.ylim(0,h)
theta = np.linspace(-90,90, num=180)
#plotting each line
for i in theta:
    sl = np.tan(np.deg2rad(i))
    x = np.arange(0,w)
    y = sl*(x-(w/2)) + (h/2)
    plt.plot(x,y,color='gray', label='manual',linewidth=0.75)


plt.show()
