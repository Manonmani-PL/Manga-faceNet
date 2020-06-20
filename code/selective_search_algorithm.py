# -*- coding: utf-8 -*-

# Force matplotlib to not use any Xwindows backend.

import matplotlib
# matplotlib.use('Agg')

# import glob
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy
import os.path
from PIL import Image
import selectivesearch
import cv2
#imported all the necessary libraries
# MANO

# from selectivesearch import *


SELECTIVESEARCH_SCALE = 100  # 255.0*3  # 1 ~ 255 ?
SELECTIVESEARCH_SIGMA = 2.2  # Gaussian filter
SELECTIVESEARCH_MIN_SIZE = 10
DELETE_SIMILR_INCLUDE = True
image_path = ''
if image_path != " ":

    def main(image_path):
        # pan =0

        input_file_name = os.path.basename(image_path)
        dir_page = os.path.basename(
            os.path.dirname(image_path))
        #preprocessing the image
        image_array = pre_process(image_path)
        #selective search algo
        candidates = selective(image_path)

        # draw rectangles on the original image
        #   iamge = cv2.imread(image_path)
        #    image = cv2.rectangle(image, start_point, end_point, color, thickness)
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))

        ax.imshow(image_array)
        # print(candidates)
        fi = 0
        #result of ss algo, these are all the coordinates of the objects found
        for (x, y, w, h) in candidates:
            # mano
            fi = fi + 1
            #converting image into numpy array
            image123 = cv2.imread(image_path)
            #cropping the objects which is given by ssearch
            #cropping to feed into neural network
            crop = image123[y:y + h, x:x + w]
            file_dir = input_file_name.strip('.jpg')

            # save_crop = "data_set/result/" + dir_page + "/" + file_dir + "/" + str(fi) + ".jpg"
            # dir_sc = "data_set/result/" + dir_page
            # dir_fc = os.path.dirname(save_crop)
            # #creating folder if it is not present and saving the cropped images
            # if not os.path.exists(dir_sc):
            #     os.mkdir(dir_sc)
            # if not os.path.exists(dir_fc):
            #     os.mkdir(dir_fc)
            # cv2.imwrite(save_crop, crop)
            # # cv2.waitKey(0)

            #drawing bounding box
            rect = mpatches.Rectangle(
                (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
            #adding that region
            if x > 0 and y > 0 and y > h and x > w:
                ax.add_patch(rect)

        delete_similr = "__delete_similr" if DELETE_SIMILR_INCLUDE else ''
        #saving the cropped file
        out_file = "data_set/result/" + dir_page + "/" + input_file_name
        out_all_dir = os.path.dirname(out_file)
        #creating directory if thet is not available
        if not os.path.exists(out_all_dir):
            os.mkdir(out_all_dir)

        plt.savefig(out_file)
#preprocess
def pre_process(image_path):
    resize1 = (256, 256)
    image = cv2.imread(image_path)
    image = cv2.resize(image, resize1)
    image_array = numpy.asarray(image)

    return image_array


def selective(image_path):
    # loading lena image

    image_array = pre_process(image_path)
    #applying all the diversification strategies | basically ssearch
    img_lbl, regions = selectivesearch.selective_search(
        image_array,
        scale=SELECTIVESEARCH_SCALE,
        sigma=SELECTIVESEARCH_SIGMA,
        min_size=SELECTIVESEARCH_MIN_SIZE
    )

    candidates = set()

    pan = 0
    for r in regions:

        x, y, w, h = r['rect']

        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            # if x > 0 and y > 0 and y > h and x > w:
            # small regions
            continue
        # excluding regions smaller than 2000 pixels

        if r['size'] < 30 * 30:
            continue
        # distorted rects

        x, y, w, h = r['rect']

        if h > 0 and w > 0:
            if w / h > 3 or h / w > 3:
                # small regions folder in e drive with name  x greater 3
                continue
        candidates.add(r['rect'])

    return post_process(candidates)


def post_process(candidates):
    pan = 0
    if not DELETE_SIMILR_INCLUDE:
        return candidates

    # print(len(candidates))

    filterd_candidates = candidates.copy()

    for c in candidates:
        # print(c)

        x, y, w, h = c

        for _x, _y, _w, _h in candidates:
            if x == _x and y == _y and w == _w and h == _h:
                continue

            if abs(x - _x) < 10 and \
                    abs(y - _y) < 10 and \
                    w * h - _w * _h < 30 * 30 and \
                    w * h - _w * _h > 0:
                   # print("delete")
                filterd_candidates.discard((_x, _y, _w, _h))

    # print(len(filterd_candidates))
    #filterd candidates are the ROI
    return filterd_candidates


def delete_min_size(candidates):
    filterd_candidates = candidates.copy()

#path for the images ie dataset
if __name__ == "__main__":
    list_path = []
    for i in range(1, 55):
        if i < 10:
            image_path = "data_set/images/KimiHaBokuNoTaiyouDa/0" + str(0) + str(i) + ".jpg"
        else:
            image_path = "data_set/images/KimiHaBokuNoTaiyouDa/" + str(0) + str(i) + ".jpg"

        main(image_path)
        list_path.append(image_path)
    # image_path = "data_set/images/YasasiiAkuma/011.jpg"
    # main(image_path)
