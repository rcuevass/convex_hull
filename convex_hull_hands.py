import cv2
import numpy as np
import sys
import os
import math as mt
import scipy as sp

"""
This script is a very basic prototype to generate convex hull and 
convexity defects.

To run this script: python convex_hull_hands.py image_file.jpg
Images should be contained in folder /images
Resulting images are also stored in folder /images
"""


def get_hull_parameters(path,image_name):
    img = cv2.imread(path+image_name)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    ret, thresh = cv2.threshold(img_gray, 127, 255,0)

    
    contours,hierarchy = cv2.findContours(thresh,2,1)
    
    
    cnt = contours[0]
    hull = cv2.convexHull(cnt,returnPoints = False)
    

    defects = cv2.convexityDefects(cnt,hull)

    img_output = 'hull_'+image_name
    

    
    
    if defects is None:
        print 'No defects found you idiot!'
    else:
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])

            # Plot staring point of edge...
            cv2.circle(img,start,3,[0,0,255],-1)

            # Plot ending point of edge...
            cv2.circle(img,end,3,[255,0,0],-1)

            # Plot line between start and end point...
            cv2.line(img,start,end,[0,255,0],2)

            # Compute distance between vertices.
            # Possible features?
            dist_ = mt.hypot(start[0]-end[0],start[1]-end[1])
            print start,end,dist_

            
            # Plot convexity defects..
            cv2.circle(img,far,5,[255,0,255],-1)
            
            
        
        # Save final image to file named "hull+initial_image.jpg"
        cv2.imwrite(path+img_output,img)
        print "Image " + img_output + " generated"
        print 'Done!'


def main(name_):
	my_path = '/Users/rogeliocuevassaavedra/Documents/Itsme3D/hands_features/images/'
	get_hull_parameters(my_path,name_)


if __name__ == '__main__':
	print sys.argv[1]
	main(sys.argv[1])
    
