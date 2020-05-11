import os
import cv2  

DOWNLOADED = 'assets/downloaded_images'
RESHAPED = 'assets/reshaped'

if not os.path.exists(RESHAPED):
	os.mkdir(RESHAPED)

for file in os.listdir(DOWNLOADED):

	_,ext = os.path.splitext(file)
	if ext == '.png': # make sure it is an image
		image_path = os.path.join(DOWNLOADED,file)
		image = cv2.imread(image_path) 

		scale_percent = 70
		width = int(image.shape[1] * scale_percent / 100)
		height = int(image.shape[0] * scale_percent / 100)
		dim = (width, height)

		# resize image
		image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
		image = cv2.copyMakeBorder(image, 100, 100, 125, 100, cv2.BORDER_CONSTANT) 
		cv2.imwrite(os.path.join(RESHAPED,file),image)
		print(file,'done')
	else:
		print('ignored',file)