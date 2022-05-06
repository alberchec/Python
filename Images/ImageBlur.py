from PIL import Image, ImageFilter, ImageOps
import sys

arguments = sys.argv
del arguments[0]

for file in arguments:
	im = Image.open(file)
	im=ImageOps.exif_transpose(im)
	im_blur = im.filter(ImageFilter.GaussianBlur(radius=10) )
	im_blur.save("mod_" + file,optimize=True,quality=50)

	im.close()
	im_blur.close()