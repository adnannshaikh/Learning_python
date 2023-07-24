from PIL import Image

img = Image.open("py_pics\liverpool_photo.jpg")

# print(img.size)
# res = img.resize((400,400))
img.thumbnail((400,400)) # keeps the aspects intact despite size change
img.save('Thumbnail2.png'