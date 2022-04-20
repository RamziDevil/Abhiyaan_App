import cv2 as cv
import numpy as np
cap = cv.VideoCapture("bolt_test_pothole.mp4")  #opening the video
#cap = cv.VideoCapture("virat_test_pothole.mp4")
while cap.isOpened():
    #reading each frame individually
    ret, frame = cap.read()  
    # if frame is read correctly ret is True
    if not ret:
        #breaking when the stream ends
        print("Can't receive frame (stream end!). Exiting ...")  
        break
    #convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #run a binary thresholding process to detect only white pixels above the threshold
    ret, thresh = cv.threshold(gray, 220, 255, cv.THRESH_BINARY)
    kernel1 = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
    kernel2 = np.ones((5,5),np.uint8)
    #erosion and dilation
    erosion = cv.erode(thresh,kernel2,iterations = 1)
    dilate = cv.dilate(erosion, kernel1, iterations=4)
    #detecting contours
    contours, _ = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    color = (0,255,0)
    for c in contours:
        poly=[None]*1
        perim = cv.arcLength(c, True)
        boundRect=cv.boundingRect(c)
        epsilon = 0.02 * cv.arcLength(c, True)
        poly[0] = cv.approxPolyDP(c, epsilon, True)
        #filtering the contours and draw their apprroximated polygons and bouding boxes
        if perim <600 and perim>30 and boundRect[2]<250 and boundRect[3]<100  and boundRect[2]>30 and len(poly[0])>3 :
            cv.drawContours(frame, poly, -1, color)
            cv.rectangle(frame, (int(boundRect[0]), int(boundRect[1])), 
            (int(boundRect[0]+boundRect[2]), int(boundRect[1]+boundRect[3])), color, 2)
            #draw everything on the original frame itself
    cv.imshow('frame', frame)
    # wait after each frame to adjust speed
    if cv.waitKey(2) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()







