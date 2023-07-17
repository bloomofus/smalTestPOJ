import cv2
import os
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
            print(f'当前已经拍摄了{i}张图片')

def prepareData(num):
    cap=capinit()
    for i in range(1,5):
        print("当前开始记录类别{}的数据集".format(i))
        catchNum(num,category=i,cap=cap)
    capEnd(cap)
    allWindowEnd()

def clearFolder(folder):
    # 文件夹路径
    folder_path = folder

    # 遍历文件夹中的所有文件和文件夹
    for filename in os.listdir(folder_path):
        # 构建完整的路径
        file_path = os.path.join(folder_path, filename)

        # 判断是否为文件
        if os.path.isfile(file_path):
            # 删除文件
            os.remove(file_path)
            print("已删除文件:", filename)
        elif os.path.isdir(file_path):
            # 删除子文件夹及其内容
            for sub_filename in os.listdir(file_path):
                sub_file_path = os.path.join(file_path, sub_filename)
                os.remove(sub_file_path)
                print("已删除文件:", sub_filename)
            # 删除空的子文件夹
            os.rmdir(file_path)
            print("已删除文件夹:", filename)
    print("清空完成")

def clearAllFolder():
    folderDic= {1: './pic_1', 2: 'pic_2', 3: 'pic_3', 4: 'pic_4'}
    for i in range(1,5):
        clearFolder(folderDic[i])
    print("清空完成")

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

def showAllFolder():
    folderDic = {1: './pic_1', 2: 'pic_2', 3: 'pic_3', 4: 'pic_4'}
    for i in range(1, 5):
        showFolder(folderDic[i])
    print("展示完成")

# clearAllFolder()
# prepareData(10)
showAllFolder()
