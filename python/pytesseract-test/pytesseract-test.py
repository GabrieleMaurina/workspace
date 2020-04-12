from skimage import io
from skimage.color import rgb2gray
from skimage.color import gray2rgb
from skimage.filters.rank import median
from skimage.filters import threshold_adaptive
from skimage.transform import resize
from skimage.measure import find_contours
from pytesseract import image_to_string
from pytesseract import image_to_data
from matplotlib import pyplot as plt
import numpy as np

def binary_to_rgb(img):
	toRtn = np.zeros(img.shape + (3,), dtype=np.uint8)
	for i in range(len(img)):
		for j in range(len(img[i])):
			toRtn[i][j] = np.array([255, 255, 255]) if img[i][j] else np.array([0, 0, 0])
	return toRtn

#plt.rcParams['toolbar'] = 'None'
f, p = plt.subplots(nrows=5, figsize=(10, 8))
for sp in p:
	sp.axis('off')

original = io.imread('photo2.jpg')
'''resized = resize(original, (360, 640))#(90, 160))
gray = rgb2gray(resized)
smoothed = median(gray, selem=np.ones((2, 2)))
threshold = binary_to_rgb(threshold_adaptive(smoothed, 101, offset=50, method='mean', mode='reflect'))'''

threshold = rgb2gray(original)

c = find_contours(threshold, 0.5)

f = c[0].T
l = c[0].T

p[0].scatter(f[0], f[1])
p[1].scatter(l[0], l[1])

#io.imsave('photo2.jpg', threshold)

'''p[0].imshow(original)
p[0].set_title('Original')

p[1].imshow(resized)
p[1].set_title('Resized')

p[2].imshow(gray2rgb(gray))
p[2].set_title('Gray')

p[3].imshow(gray2rgb(smoothed))
p[3].set_title('Smoothed')

p[4].imshow(threshold)
p[4].set_title('Threshold')'''

'''for i in range(0, 14):
	config = '-psm ' + str(i)

	try:
		print('## ' + str(i))
		print(image_to_string(original, config=config))
	except:
		pass'''

plt.show()