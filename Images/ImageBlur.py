from PIL import Image, ImageFilter

image = "path.jpg"
im = Image.open(image)
im_blur = im.filter(ImageFilter.GaussianBlur(radius=10) )
im_blur.save("newpath.jpg")