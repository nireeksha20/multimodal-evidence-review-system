from PIL import Image

paths = [
    "../dataset/images/test/case_001/img_1.jpg",
    "../dataset/images/test/case_017/img_1.jpg",
    "../dataset/images/test/case_029/img_1.jpg"
]

for p in paths:
    img = Image.open(p)
    print(p, img.size)
    img.show()