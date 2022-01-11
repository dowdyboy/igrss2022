from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import random

from igrss2022.utils import get_visual_label_image


def visual_seg_map():
    rgb_im_path = r'E:\临时文件夹\labeled_train\Nice\BDORTHO\06-2014-0994-6311-LA93-0M50-E080.tif'
    label_im_path = r'E:\临时文件夹\labeled_train\Nice\UrbanAtlas\06-2014-0994-6311-LA93-0M50-E080_UA2012.tif'
    dem_im_path = r'E:\临时文件夹\labeled_train\Nice\RGEALTI\06-2014-0994-6311-LA93-0M50-E080_RGEALTI.tif'

    rgb_im = np.array(Image.open(rgb_im_path))
    label_im = np.array(Image.open(label_im_path))
    dem_im = np.array(Image.open(dem_im_path))
    print(rgb_im.shape)
    print(label_im.shape)
    print(dem_im.shape)

    trans_label_im, _ = get_visual_label_image(label_im_path)

    plt.figure()
    plt.imshow(trans_label_im)
    plt.show()

    plt.figure()
    plt.imshow(rgb_im)
    plt.show()
    # plt.figure()
    # plt.imshow(label_im, cmap='gray')
    # plt.show()
    # plt.figure()
    # plt.imshow(dem_im)
    # plt.show()


def generate_visual_data():
    src_dir_path = r'E:\临时文件夹\labeled_train\Nice\UrbanAtlas'
    dst_dir_path = r'E:\临时文件夹\labeled_train\Nice\UrbanAtlas-visual'
    if not os.path.isdir(dst_dir_path):
        os.makedirs(dst_dir_path)
    src_filename_list = os.listdir(src_dir_path)
    random.shuffle(src_filename_list)
    for filename in src_filename_list:
        if filename.endswith('.tif'):
            print(os.path.join(src_dir_path, filename))
            im, uni_label = get_visual_label_image(os.path.join(src_dir_path, filename))
            im.save(os.path.join(dst_dir_path, filename))
            with open(os.path.join(dst_dir_path, filename.split('.')[0] + '.txt'), 'w+') as f:
                f.write(','.join(map(lambda x: str(x), list(uni_label))))
            # break


if __name__ == '__main__':


    pass
