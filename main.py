
import cv2
import numpy as np

#Получить изображение из файла
img = cv2.imread('1.jpg',0)
#Фильтрация изображения
img = cv2.GaussianBlur(img,(0, 0),sigmaX=1.5, sigmaY= 1.5) #Блюр
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img = cv2.Canny(image = img, threshold1= 50, threshold2= 150, apertureSize = 3) #Поиск границ
img = cv2.GaussianBlur(img,(0, 0),sigmaX=1.2, sigmaY= 1.2)#ДопБлюр
#maxR = int(min(img.shape[0], img.shape[1])/3)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1.05,6000,param1=100,param2=70,minRadius=0,maxRadius=0)#Поиск окружностей

#Вывод окружностей
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('Circles',cimg) #Обнаруженный круг
cv2.imshow('img',img) #То что, видит комп.
cv2.waitKey(0)

cv2.destroyAllWindows()