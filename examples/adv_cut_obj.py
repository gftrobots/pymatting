from pymatting import *
import os
import numpy as np
import re

directory = '/home/developer/Development/data/sorting/images/set_03/'
image_files = [f for f in os.listdir(directory) if f.startswith("image") and f.endswith((".jpg", ".png", ".JPG", ".PNG"))]

scale = 1.0

for index in range(len(image_files)):
    image_path = os.path.join(directory, image_files[index])
    numbers = re.findall('\d+', image_files[index])
    trimap_path = os.path.join(directory, "trimap" + numbers[0] + ".jpg")

    image = load_image(image_path, "RGB", scale, "box")
    trimap = load_image(trimap_path, "GRAY", scale, "nearest")

    # estimate alpha from image and trimap
    alpha = estimate_alpha_cf(image, trimap)

    # make gray background
    new_background = np.zeros(image.shape)
    new_background[:, :] = [0.5, 0.5, 0.5]

    # estimate foreground from image and alpha
    foreground, background = estimate_foreground_ml(image, alpha, return_background=True)

    # blend foreground with background and alpha, less color bleeding
    new_image = blend(foreground, new_background, alpha)

    # save results in a grid
    images = [image, trimap, alpha, new_image]
    grid = make_grid(images)
    save_image(directory+"grid_"+ str(numbers[0])+".png", grid)
    save_image(directory+"alpha_"+ str(numbers[0])+".png", alpha)
    save_image(directory+"foreground_"+ str(numbers[0])+".png", foreground)
    save_image(directory+"background_"+ str(numbers[0])+".png", background)
    print("Processed image: ", numbers[0])
