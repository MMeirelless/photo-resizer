import os
from PIL import Image, ImageSequence

photos_path = r'photos'
new_size = (1024, 9999) # The height was set as 9999 because we want to preserve the image aspects and quality. So this method auto calculated which is the best Height

for root, dirs, files in os.walk(photos_path):
    for file in files:
        raw_photo_path = os.path.join(root,file)
        new_photo_path = os.path.join("resized_photos",file)
        photo_format = file.split(".")[len(file.split("."))-1]
        photo_format = "jpeg" if photo_format == "jpg" else photo_format

        if photo_format != "gif":
            image = Image.open(raw_photo_path)
            image.thumbnail(new_size, Image.ANTIALIAS) 
            image.save(new_photo_path, photo_format.upper(), quality=100)

        else:
            gif = Image.open(raw_photo_path)
            frames = ImageSequence.Iterator(gif)

            def thumbnails(frames):
                for frame in frames:
                    thumbnail = frame.copy()
                    thumbnail.thumbnail(new_size, Image.ANTIALIAS)
                    yield thumbnail

            frames = thumbnails(frames)

            new_gif = next(frames)
            new_gif.info = gif.info
            new_gif.save(new_photo_path, save_all=True, append_images=list(frames))