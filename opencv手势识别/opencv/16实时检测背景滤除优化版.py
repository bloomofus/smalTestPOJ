import cv2
import numpy as np
from keras.models import load_model


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


def binary_threshold(image, threshold):
    # 二值化
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化图像
    _, binary_image = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return binary_image


def picProcess(image):
    image = smooth_filter(image, 7)  # 平滑滤波
    image = sharpen_filter(image)  # 锐化滤波
    image = binary_threshold(image, 200)  # 二值化
    return image


def predict(img):
    global loaded_model
    # 这里的img是经过预处理的256*256的01双色图
    img = np.expand_dims(img, axis=-1)
    resultList = loaded_model.predict(np.array([img, ]))[0]
    idx = 0
    for i in range(len(resultList)):
        if resultList[i] >= resultList[idx]:
            idx = i
    if resultList[idx]<=0.7:
        # 没有置信度
        return 0
    return idx + 1


# 加载保存的模型参数
loaded_model = load_model('10手势识别模型.keras')
# 创建背景减除器
bgSubtractor = cv2.createBackgroundSubtractorMOG2()
# 创建摄像头
cap = cv2.VideoCapture(0)
while True:
    # 读取摄像头帧
    ret, frame = cap.read()
    if not ret:
        break

    # 背景减除
    fgMask = bgSubtractor.apply(frame)

    # 去除噪声
    fgMask = cv2.medianBlur(fgMask, 5)

    # 展示帧
    cv2.imshow("Camera", frame)
    # 图片预处理
    ## 调整帧的尺寸为256x256
    fgMask_resized = cv2.resize(fgMask, (256, 256))
    # 将灰度图像扩展为三个通道的灰度图像
    img_processed3 = np.stack((fgMask_resized,) * 3, axis=-1)
    img_processed=binary_threshold(img_processed3,150)
    img_processed3=np.stack((img_processed,) * 3, axis=-1)
    ## 显示处理后的画面
    cv2.imshow("img_processed",img_processed3)

    print(predict(img_processed))

    # 检测按键，按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头对象和关闭窗口
cap.release()
cv2.destroyAllWindows()
