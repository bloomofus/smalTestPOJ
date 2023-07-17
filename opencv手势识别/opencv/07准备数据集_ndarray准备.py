import os

import cv2
import numpy as np
from keras.utils import to_categorical

def dataLoad():
    folderDic = {1: './pic_1_processed', 2: './pic_2_processed', 3: './pic_3_processed', 4: './pic_4_processed'}
    X = []
    y = []
    for category in range(1, 5):
        folder = folderDic[category]
        file_list = os.listdir(folder)
        for idx in range(len(file_list)):
            filename = file_list[idx]
            # 检查文件扩展名，只处理图像文件
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                # 构建完整的图像文件路径
                image_path = os.path.join(folder, filename)
                # 读取图像文件
                image = cv2.imread(image_path)
                image = image[:, :, 0]
                # 归一化图像，将像素值缩放到0到1之间
                image = image / 255.0  # 这里是一个256*256的ndarray类型
                X.append(image)
                y.append(category)
    # 将列表转换为NumPy数组
    X = np.array(X)
    y = np.array(y)
    # 进行独热编码
    y = to_categorical(y)
    return X, y


X,y=dataLoad()
