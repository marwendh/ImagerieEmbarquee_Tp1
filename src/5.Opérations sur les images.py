import cv2
import numpy as np


imgBin1 =np.zeros((300,500))
imgBin2 =np.zeros((300,500))

imgBin1[100:160,200:260]=1
imgBin2[140:220,220:300]=1

resultat_or = cv2.bitwise_or(imgBin1, imgBin2)
resultat_and = cv2.bitwise_and(imgBin1, imgBin2)
resultat_xor = cv2.bitwise_xor(imgBin1, imgBin2)
#cv2.imshow("resultat_or",resultat_or)
#cv2.imshow("resultat_and",resultat_and)
#cv2.imshow("resultat_xor",resultat_xor)


# image path
path1= r'..\shape2R.jpg'
path2= r'..\women2.jpg'
path3= r'..\pout.tif'
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
img3 = cv2.imread(path3)



img1=cv2.resize(img1,(630,360))
img2=cv2.resize(img2,(630,360))
img3=cv2.resize(img3,(630,360))

addd1=cv2.add(img1,img2)
addd2=img1+img2


sub1=cv2.subtract(img1,img2)
sub2=img1-img2
x=100
y=100
pixel1 = img1[x,y,:]
print(pixel1)
pixel2 = img2[x,y,:]
print(pixel2)
pixelResSub=addd2[x,y,:]
print(pixelResSub)

#sub yzid 256
#add yna9es 256




xor=cv2.bitwise_xor(img1,img2)
anda=cv2.bitwise_and(img2,img3)




cv2.imshow("add1",addd1)
cv2.imshow("add2",addd2)

cv2.imshow("sub1",sub1)
cv2.imshow("sub2",sub2)



#cv2.imshow("sub",sub)
#cv2.imshow("xor",xor)
#cv2.imshow("anda",anda)



cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

