import os
from PIL import Image

photos_path = r'photos'

for root, dirs, files in os.walk(photos_path):
    for file in files:
        raw_photo_path = os.path.join(root,file)
        new_photo_path = os.path.join("resized_photos",file)
        photo_format = file.split(".")[len(file.split("."))-1]
        photo_format = "jpeg" if photo_format == "jpg" else photo_format

        image = Image.open(raw_photo_path)
        image.thumbnail((1024, 9999), Image.ANTIALIAS) # The height was set as 9999 because we want to preserve the image aspects and quality. So this method auto calculated which is the best Height
        image.save(new_photo_path, photo_format.upper(), quality=100)
        image.show()