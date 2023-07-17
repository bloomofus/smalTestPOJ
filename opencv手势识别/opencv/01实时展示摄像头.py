import cv2
cap = cv2.VideoCapture(0)
while True:
    # 读取帧
    ret, frame = cap.read()

    # 展示帧
    cv2.imshow("Camera", frame)

    # 检测按键，按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头对象和关闭窗口
cap.release()
cv2.destroyAllWindows()
