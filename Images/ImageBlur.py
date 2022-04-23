from PIL import Image, ImageFilter
import sys

arguments = sys.argv
del arguments[0]

for file in arguments:
	im = Image.open(file)
	im_blur = im.filter(ImageFilter.GaussianBlur(radius=10) )
	im_blur.save("mod_" + file)

	im.close()
	im_blur.close()