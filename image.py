from PIL import Image,ImageFilter

img = Image.open("py_pics\pikachu.jpg")
filt = img.filter(ImageFilter.BLUR)

filt.save("blurchu.png","png")
filt.show()


# print(img.format)
# print(img.size)
# print(img.mode)