from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import random

from igrss2022.utils import get_visual_label_image, seg_color_str_map, get_label_arrangement


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


def plot_label_arrangement():
    src_dir_path_nice = r'E:\临时文件夹\labeled_train_with_visual\Nice\UrbanAtlas'
    src_filename_list_nice = os.listdir(src_dir_path_nice)
    label_count_nice = np.array([0 for _ in seg_color_str_map])

    for filename in src_filename_list_nice:
        if filename.endswith('.tif'):
            label_count_nice += get_label_arrangement(os.path.join(src_dir_path_nice, filename))
            # break

    plt.figure()
    plt.bar(range(len(seg_color_str_map)), label_count_nice / np.sum(label_count_nice), color=seg_color_str_map)
    for x in range(len(seg_color_str_map)):
        plt.text(x, (label_count_nice / np.sum(label_count_nice))[x], round((label_count_nice / np.sum(label_count_nice))[x], 2), ha='center')
    plt.title('nice urban atlas')
    plt.show()

    src_dir_path_saint = r'E:\临时文件夹\labeled_train_with_visual\Nantes_Saint-Nazaire\UrbanAtlas'
    src_filename_list_saint = os.listdir(src_dir_path_saint)
    label_count_saint = np.array([0 for _ in seg_color_str_map])

    for filename in src_filename_list_saint:
        if filename.endswith('.tif'):
            label_count_saint += get_label_arrangement(os.path.join(src_dir_path_saint, filename))
            # break

    plt.figure()
    plt.bar(range(len(seg_color_str_map)), label_count_saint / np.sum(label_count_saint), color=seg_color_str_map)
    for x in range(len(seg_color_str_map)):
        plt.text(x, (label_count_saint / np.sum(label_count_saint))[x], round((label_count_saint / np.sum(label_count_saint))[x], 2), ha='center')
    plt.title('saint urban atlas')
    plt.show()

    label_count_all = label_count_nice / 1e4 + label_count_saint / 1e4

    plt.figure()
    plt.bar(range(len(seg_color_str_map)), label_count_all / np.sum(label_count_all), color=seg_color_str_map)
    for x in range(len(seg_color_str_map)):
        plt.text(x, (label_count_all / np.sum(label_count_all))[x], round((label_count_all / np.sum(label_count_all))[x], 2), ha='center')
    plt.title('all urban atlas')
    plt.show()


if __name__ == '__main__':





    pass
