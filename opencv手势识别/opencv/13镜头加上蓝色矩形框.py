import cv2

# 设置矩形框的位置和大小
rect_x = 400
rect_y = 0
rect_width = 300
rect_height = 300

# 摄像头捕获函数
def capture_frame():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 在帧上绘制蓝色矩形框
        cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (255, 0, 0), 2)

        cv2.imshow('Camera', frame)

        # 检测按键
        key = cv2.waitKey(1)
        if key == ord('p'):  # 按下'p'键保存框内图像
            img_roi = frame[rect_y:rect_y+rect_height, rect_x:rect_x+rect_width]
            cv2.imwrite('captured_image.jpg', img_roi)
            print('Image saved!')

        if key == 27:  # 按下ESC键退出
            break

    cap.release()
    cv2.destroyAllWindows()

# 调用摄像头捕获函数
capture_frame()
