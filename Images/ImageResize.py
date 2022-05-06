from PIL import Image, ImageFilter, ImageOps
import sys

arguments = sys.argv
del arguments[0]

for file in arguments:
	size=1500,1125
	#size=800,600
	#size=200,150

	image=Image.open(file)
	image=ImageOps.exif_transpose(image)
	pixels = image.size

	if(pixels[0] < pixels[1]):
		size = size[1],size[0]

	image=image.resize(size)
	image = image.filter(ImageFilter.GaussianBlur(radius=0.5) )
	image.save("mod_" + file,optimize=True,quality=80)

	image.close()