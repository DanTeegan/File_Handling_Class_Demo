from PIL import Image


# def __init__(self, file_path, text_storage=None):
#     self.file_path = file_path
#     self.text_storage = text_storage

image = Image.open("C:/Users/dante/PycharmProjects/File_Handling_Class_Demo/baby.jpg")
image.show()
image.save("Daniel.jpg")


# def image_file_read(self):
#     with open("baby.jpg", "rb") as image, open("baby2.jpg", "wb") as image2:
#         pic = image.read()
#         image2.write()
#         Image.open("baby2.jpg").show()