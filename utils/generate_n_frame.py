from __future__ import print_function, division
import os
import sys


def generate_n_frame(dir_path, class_name):  # 记录帧数
    class_path = os.path.join(dir_path, class_name)
    if not os.path.isdir(class_path):
        return

    for file_name in os.listdir(class_path):
        video_dir_path = os.path.join(class_path, file_name)
        image_index = []
        for image_file_name in os.listdir(video_dir_path):
            if 'image' not in image_file_name:
                continue
            image_index.append(int(image_file_name[6:11]))

            if len(image_index) == 0:
                print('no image files', video_dir_path)
                n_frames = 0
            else:
                image_index.sort(reverse=True)
                n_frames = image_index[0]
                print(video_dir_path, n_frames)
            with open(os.path.join(video_dir_path, 'n_frames'), 'w') as dst_file:
                dst_file.write(str(n_frames))


if __name__ == "__main__":
    dir_path = sys.argv[1]  # jpg directory
    for class_name in os.listdir(dir_path):
        generate_n_frame(dir_path, class_name)