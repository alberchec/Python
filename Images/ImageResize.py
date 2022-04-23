from PIL import Image
import sys

arguments = sys.argv
del arguments[0]

for file in arguments:
	size=1500,1125
	image=Image.open(file)
	image=image.resize(size)
	image.save("mod_" + file,optimize=True,quality=60)

	image.close()