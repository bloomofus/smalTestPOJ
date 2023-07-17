import os

import cv2
import numpy as np


def adjust_brightness(image, brightness_factor):
    # 亮度调整
    # 将图像转换为浮点类型
    image = image.astype(np.float32)
    # 根据亮度调整因子调整图像亮度
    adjusted_image = image * brightness_factor
    # 将图像像素值限制在0到255之间
    adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)
    return adjusted_image


def adjust_contrast(image, contrast_factor):
    # 对比度调整
    # 将图像转换为浮点类型
    image = image.astype(np.float32)
    # 根据对比度调整因子调整图像对比度
    adjusted_image = image * contrast_factor
    # 将图像像素值限制在0到255之间
    adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)
    return adjusted_image


def smooth_filter(image, kernel_size):
    # 平滑滤波
    # 使用均值滤波器平滑图像
    smoothed_image = cv2.blur(image, (kernel_size, kernel_size))
    return smoothed_image


def sharpen_filter(image):
    # 锐化滤波
    # 创建拉普拉斯滤波器核
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]], dtype=np.float32)
    # 使用拉普拉斯滤波器对图像进行锐化
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image


def edge_detection(image, threshold1, threshold2):
    # 使用Canny边缘检测算法检测边缘
    edges = cv2.Canny(image, threshold1, threshold2)
    return edges


def binary_threshold(image, threshold):
    # 二值化
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化图像
    _, binary_image = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return binary_image


# # 读取图像
# image = cv2.imread('./pic_4/1.png')


# # 调用边缘检测函数，效果还不错
# edges = edge_detection(image, 80, 450)
# # 显示边缘图像
# cv2.imshow("Edges", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 二值化，效果很不错，参数为200
# for i in range(100,256,10):
#     newImage=binary_threshold(image,i)
#     cv2.imshow('binary',newImage)
#     print(i)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # 锐化滤波，效果还行，我觉得可以放在最开头开始处理的时候
# newImage=sharpen_filter(image)
# cv2.imshow('sharp',newImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 平滑滤波，效果很一般，参数为7顶天了
# for i in range(1,30,1):
#     newImage=smooth_filter(image,i)
#     cv2.imshow('smooth',newImage)
#     print(i)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # 对比度，效果还行，参数0全黑，3全白，1普通，2还行
# for i in np.arange(0,3,0.1):
#     newImage=adjust_brightness(image,i)
#     cv2.imshow('adjust',newImage)
#     print(i)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# 就不调整亮度了

def picProcess(folder, name):
    image = cv2.imread(folder + '/' + name)
    image = smooth_filter(image, 7)  # 平滑滤波
    # cv2.imshow('img_processed', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    image = sharpen_filter(image)  # 锐化滤波
    # cv2.imshow('img_processed', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    image = binary_threshold(image, 200)  # 二值化
    # cv2.imshow('img_processed', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # image=adjust_brightness(image,2)    # 对比度
    # cv2.imshow('img_processed', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # image=binary_threshold(image,200)   # 二值化
    # cv2.imshow('img_processed', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # image=edge_detection(image,80,450)    # 边缘检测
    # cv2.imshow('img_processed', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 将处理后的图片保存为新的文件
    processed_image_path = folder + '_processed/' + name
    cv2.imwrite(processed_image_path, image)


def picAllProcess():
    folderDic = {1: './pic_1', 2: 'pic_2', 3: 'pic_3', 4: 'pic_4'}
    for i in range(1, 5):
        folder = folderDic[i]
        file_list = os.listdir(folder)
        for idx in range(len(file_list)):
            filename = file_list[idx]
            # 检查文件扩展名，只处理图像文件
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                picProcess(folder, filename)


# folderDic= {1: './pic_1', 2: 'pic_2', 3: 'pic_3', 4: 'pic_4'}
# picProcess(folderDic[1],'1.png')
# picAllProcess()

def showFolder(folder):
    # 遍历文件夹中的所有文件
    file_list = os.listdir(folder)
    file_num = len(file_list)
    for idx in range(file_num):
        filename = file_list[idx]
        # 检查文件扩展名，只处理图像文件
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # 构建完整的图像文件路径
            image_path = os.path.join(folder, filename)
            # 读取并显示图像
            image = cv2.imread(image_path)
            cv2.imshow("Image", image)

            while True:
                key = cv2.waitKey(0)
                if key == ord('i'):
                    print(f"当前是第{idx + 1}/{file_num}个文件")
                    continue
                elif key == ord('n'):
                    break
                elif key == ord('d'):
                    # 提示是否删除图像
                    delete = False
                    while True:
                        response = input("是否删除该图像？(y/n): ")
                        if response.lower() == 'y':
                            # 删除图像文件
                            os.remove(image_path)
                            print("图像已删除。")
                            delete = True
                            cv2.destroyAllWindows()
                            break
                        elif response.lower() == 'n':
                            print("图像未删除。")
                            break
                        else:
                            print("无效的输入。")
                            continue
                    if delete:
                        break  # 直接展示下一张图片，否则继续展示当前图片
    # 关闭窗口
    cv2.destroyAllWindows()
    print("展示完成")


showFolder('./pic_2_processed')
