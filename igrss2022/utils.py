from PIL import Image
import numpy as np


def get_visual_label_image(label_im_path):
    seg_color_map = [
        (35, 31, 32),  # 0 No information
        (219, 95, 87),  # 1 Urban fabric
        (219, 151, 87),  # 2 Industrial, commercial, public, military, private and transport units
        (219, 208, 87),  # 3 Mine, dump and contruction sites
        (173, 219, 87),  # 4 Artificial non-agricultural vegetated areas
        (117, 219, 87),  # 5 Arable land (annual crops)
        (123, 196, 123),  # 6 Permanent crops
        (88, 177, 88),  # 7 Pastures
        (212, 246, 212),  # 8 Complex and mixed cultivation patterns
        (176, 226, 176),  # 9 Orchards at the fringe of urban classes
        (0, 128, 0),  # 10 Forests
        (88, 176, 167),  # 11 Herbaceous vegetation associations
        (153, 93, 19),  # 12 Open spaces with little or no vegetation
        (87, 155, 219),  # 13 Wetlands
        (0, 98, 255),  # 14 Water
        (35, 31, 32),  # 15 Clouds and shadows
    ]
    label_im = np.array(Image.open(label_im_path))
    uni_labels = np.unique(label_im)
    trans_label_im = np.zeros(label_im.shape + (3, ))
    for i in range(len(seg_color_map)):
        trans_label_im[label_im == i, 0] = seg_color_map[i][0]
        trans_label_im[label_im == i, 1] = seg_color_map[i][1]
        trans_label_im[label_im == i, 2] = seg_color_map[i][2]
    return Image.fromarray(trans_label_im.astype(np.uint8)), uni_labels

