import cv2 as cv
import numpy as np

orginal = cv.imread('image.png')
img = orginal.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
img, contours, hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for i, c in enumerate(contours):
	area = cv.contourArea(c)
	if area > 800 and area < 1500:
		print(area)
		print(len(c))
		x, y, w, h = cv.boundingRect(c)
		char = img[y : y + h, x : x + w]
		'''im = orginal.copy()
		cv.drawContours(im, contours, i, (0, 0, 255), 2)
		cv.imshow('Contours', im)'''
		cv.imshow('Char ' + str(i), char)
		cv.waitKey()