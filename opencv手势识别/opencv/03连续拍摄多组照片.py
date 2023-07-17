import cv2

def capinit():
    # 创建摄像头对象
    return cv2.VideoCapture(0)
def capEnd(cap):
    # 释放摄像头对象
    cap.release()
def allWindowEnd():
    # 释放全部窗口对象
    cv2.destroyAllWindows()


def catchNum(num, category,cap):
    folderDic = {1: './pic_1', 2: 'pic_2', 3: 'pic_3', 4: 'pic_4'}
    i = 0
    while True:
        # 读取帧
        ret, frame = cap.read()

        # 显示帧
        cv2.imshow("Camera", frame)

        # 检测按键，按下 'p' 键保存照片;按下 'q' 键退出循环
        key = cv2.waitKey(1)
        if key == ord('p'):
            # 调整帧的尺寸为256x256
            frame_resized = cv2.resize(frame, (256, 256))
            # 将帧转换为灰度图像
            gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
            # 保存灰度图像到文件夹
            filename = folderDic[category] + "/" + str(i + 1) + ".png"
            cv2.imwrite(filename, gray)
            print("照片已保存。")
            i += 1
            if i == num:
                print(f"已经拍摄完成所有类别为{category}的照片")
                break
        elif key == ord('q'):
            break
        elif key == ord('i'):
            print(f'当前已经拍摄了{num}张图片')

def catchEnd(folder,cap):
    num=0
    while True:
        # 读取帧
        ret, frame = cap.read()
        # 显示帧
        cv2.imshow("Camera", frame)
        # 检测按键，按下 'p' 键保存照片;按下 'q' 键退出循环
        key = cv2.waitKey(1)
        if key == ord('p'):
            # 调整帧的尺寸为256x256
            frame_resized = cv2.resize(frame, (256, 256))
            # 将帧转换为灰度图像
            gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
            # 保存灰度图像到文件夹
            filename = folder + "/" + str(num + 1) + ".png"
            cv2.imwrite(filename, gray)
            print("照片已保存。")
            num += 1

        elif key == ord('q'):
            break
        elif key == ord('i'):
            print(f'当前已经拍摄了{num}张图片')

cap=capinit()
# catchNum(20, 1,cap)
# catchNum(20, 2,cap)
# catchNum(20, 3,cap)
# catchNum(20, 4,cap)
catchEnd('./pic_1',cap)
capEnd(cap)
allWindowEnd()



