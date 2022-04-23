from PIL import Image
import sys

arguments = sys.argv
del arguments[0]

for file in arguments:
	image = Image.open(file)
	image.save("mod_" + file,optimize=True,quality=70)

	image.close()
