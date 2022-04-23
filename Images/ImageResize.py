from PIL import Image

size=1500,1125
image = "path.jpg"
im=Image.open(image)
im_resize=im.resize(size)
im_resize.save("newpath.jpg")