from PIL import Image

image = Image.open("../dataset/images/sample/case_001/img_1.jpg")

print("Size:", image.size)
print("Mode:", image.mode)

image.show()