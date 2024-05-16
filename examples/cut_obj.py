from pymatting import cutout
import os
import numpy as np
import re

directory = '/home/developer/Development/data/sorting/images/set_03/'
image_files = [f for f in os.listdir(directory) if f.startswith("image") and f.endswith((".jpg", ".png", ".JPG", ".PNG"))]

for index in range(len(image_files)):
    image = os.path.join(directory, image_files[index])
    numbers = re.findall('\d+', image_files[index])
    mask = os.path.join(directory, "mask" + numbers[0] + ".jpg")
    trimap = os.path.join(directory, "trimap" + numbers[0] + ".jpg")

    cutout(
        # input image path
        image,
        # input trimap path
        trimap,
        # output cutout path
        directory+"cutout"+ str(numbers[0])+".png",
    )
    print("Cutout", str(numbers[0]), "done")