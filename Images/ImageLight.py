from PIL import Image

image = Image.open("path.jpg")
image.save("newpath.jpg",optimize=True,quality=70)
