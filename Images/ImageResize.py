from PIL import Image

size=1500,1125
image=Image.open("obra1foto1.jpg")
image=image.resize(size)
image.save("newpath.jpg",optimize=True,quality=60)