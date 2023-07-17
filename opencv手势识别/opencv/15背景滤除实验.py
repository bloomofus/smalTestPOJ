import cv2

# 创建背景减除器
bgSubtractor = cv2.createBackgroundSubtractorMOG2()

# 打开摄像头
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

    # 显示结果
    cv2.imshow('Original', frame)
    cv2.imshow('Foreground Mask', fgMask)

    # 检测按键，按下ESC键退出
    key = cv2.waitKey(1)
    if key == 27:
        break

# 释放摄像头和关闭窗口
cap.release()
cv2.destroyAllWindows()
