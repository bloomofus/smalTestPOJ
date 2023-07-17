import os

import cv2
import numpy as np
from keras.models import load_model
from sklearn.model_selection import train_test_split

# 加载保存的模型参数
loaded_model = load_model('10手势识别模型.keras')

img = cv2.imread('./pic_3_processed/1.png')


def predict(img):
    global loaded_model
    # 这里的img是经过预处理的256*256*3的双色图
    img = img[:, :, 0]
    # 归一化图像，将像素值缩放到0到1之间
    img = img / 255.0  # 这里是一个256*256的ndarray类型
    img = np.expand_dims(img, axis=-1)
    resultList = loaded_model.predict(np.array([img, ]))[0]
    idx = 0
    for i in range(len(resultList)):
        if resultList[i] >= resultList[idx]:
            idx = i
    return idx + 1


print(predict(img))  # 预测正确


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
    return X, y


# 加载数据
X, y = dataLoad()

# 打乱数据集
np.random.seed(42)
dataset_size = len(X)

## 生成一个随机排列的索引数组
shuffle_indices = np.random.permutation(dataset_size)

## 使用随机索引对X和y进行打乱
X_shuffled = X[shuffle_indices]
y_shuffled = y[shuffle_indices]
X = X_shuffled
y = y_shuffled

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

print("pred:", loaded_model.predict(X_test))
print("real:", y_test)
