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
    # 这里的img是经过预处理的256*256的双色图
    # 归一化图像，将像素值缩放到0到1之间
    img = img / 255.0  # 这里是一个256*256的ndarray类型
    img = np.expand_dims(img, axis=-1)
    resultList = loaded_model.predict(np.array([img, ]))[0]
    idx = 0
    for i in range(len(resultList)):
        if resultList[i] >= resultList[idx]:
            idx = i
    return idx + 1


# 加载保存的模型参数
loaded_model = load_model('10手势识别模型.keras')

cap = cv2.VideoCapture(0)
while True:
    # 读取帧
    ret, frame = cap.read()

    # 展示帧
    cv2.imshow("Camera", frame)
    # 图片预处理
    ## 调整帧的尺寸为256x256
    frame_resized = cv2.resize(frame, (256, 256))
    ## 将帧转换为灰度图像
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    ## 格式变为256*256*3的灰度图像
    ### 扩展维度，将灰度图像从 (256, 256) 变为 (256, 256, 1)
    gray1 = np.expand_dims(gray, axis=-1)
    ### 将灰度图像转换为彩色图像
    gray3 = cv2.cvtColor(gray1, cv2.COLOR_GRAY2BGR)
    ## 图片预处理
    img_processed = picProcess(gray3)  # 又变成256*256了
    ## 显示处理后的画面
    img_processed3= cv2.cvtColor(np.expand_dims(img_processed, axis=-1), cv2.COLOR_GRAY2BGR)
    cv2.imshow("img_processed",img_processed3)

    print(predict(img_processed))

    # 检测按键，按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头对象和关闭窗口
cap.release()
cv2.destroyAllWindows()
