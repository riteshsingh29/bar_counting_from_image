import cv2
import numpy as np
from random import randint
from itertools import groupby




img= cv2.imread('TMT2.jpeg',0)
rows, cols = img.shape[:2]
th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,301, 41)
kernel = np.ones((4,4),np.uint8)

cv2.imshow('threshold',th)
rod_count = []
count = 100
while( count!=0 ):

    count = count-1
    random_row = randint(0, rows-1)

    arr = th[random_row:random_row+1, :]
    arr2 = np.array(arr)[0].tolist()
    temp = [a[0] for a in groupby(arr2)]
    b = sum(x == 0 for x in temp)
    rod_count.append(b)


print(np.median(rod_count)-3)
cv2.waitKey(0)
cv2.destroyAllWindows()