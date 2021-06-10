from PIL import Image
import cv2
import numpy as np
#from keras.preprocessing import image 
from matplotlib import pyplot
test_image1 = cv2.cv2.imread("a.JPEG",0)
test_image2 = cv2.cv2.imread("b.JPEG",0)

#test_image1 = image.img_to_array(test_image1)
#test_image2 = image.img_to_array(test_image2)

#test_image1 = np.expand_dims(test_image1, axis = 0)
#test_image2 = np.expand_dims(test_image2, axis = 0)

test_image3 = np.array(test_image1) #.astype(float)
test_image4 = np.array(test_image2)  #.astype(float32)

i=480     # if array value is (756, 576)
j=640     # if array value is (756, 576)

#-----------------------------MAX----------
t_max=np.empty((i,j,3), dtype=int) 
for m in range(i):
    for k in range(j):
        if test_image3[m][k].all()> test_image4[m][k].all():
            t_max[m][k]=test_image3[m][k]
        else:
             t_max[m][k]=test_image4[m][k]
t_max=np.array(t_max)        
pyplot.imshow(t_max)
pyplot.show()
#-----------------------------MIN----------
t_min=np.empty((i,j,3), dtype=int) 
for m in range(i):
    for k in range(j):
        if test_image3[m][k].all()< test_image4[m][k].all():
            t_min[m][k]=test_image3[m][k]
        else: 
             t_min[m][k]=test_image4[m][k]
t_avg=np.array(t_min)        
pyplot.imshow(t_min)
pyplot.show()
#----------------------------AVG----------
t_avg=np.empty((i,j,3), dtype=int) 
for m in range(i):
    for k in range(j):
        t_avg[m][k]=((test_image3[m][k]+test_image4[m][k])/2)
t_min=np.array(t_avg)        
pyplot.imshow(t_avg)
pyplot.show()