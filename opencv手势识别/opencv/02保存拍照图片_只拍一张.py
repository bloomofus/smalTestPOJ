import cv2

cap = cv2.VideoCapture(0)
save_folder = "./pic_3"  # 指定保存照片的文件夹路径
while True:
    # 读取帧
    ret, frame = cap.read()

    # 显示帧
    cv2.imshow("Camera", frame)

    # 检测按键，按下 'p' 键保存照片
    key = cv2.waitKey(1)
    if key == ord('p'):
        # 调整帧的尺寸为256x256
        frame_resized = cv2.resize(frame, (256, 256))

        # 将帧转换为灰度图像
        gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

        # 保存灰度图像到文件夹
        filename = save_folder + "/1.png"
        cv2.imwrite(filename, gray)
        print("照片已保存。")

    # 按下 'q' 键退出循环
    elif key == ord('q'):
        break

# 释放摄像头对象和关闭窗口
cap.release()
cv2.destroyAllWindows()
