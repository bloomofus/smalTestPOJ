import os

import cv2
import numpy as np


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

def showAllFolder(choose=None):
    folderDic_raw = {1: './pic_1', 2: 'pic_2', 3: 'pic_3', 4: 'pic_4'}
    folderDic_bgfilter = {1: './pic_1_processed', 2: 'pic_2_processed', 3: 'pic_3_processed', 4: 'pic_4_processed'}
    if choose==None:
        for i in range(1, 5):
            showFolder(folderDic_raw[i])
        for i in range(1, 5):
            showFolder(folderDic_bgfilter[i])
    elif choose=='raw':
        for i in range(1, 5):
            showFolder(folderDic_raw[i])
    elif choose=='processed':
        for i in range(1, 5):
            showFolder(folderDic_bgfilter[i])
    print("展示完成")

def binary_threshold(image, threshold):
    # 二值化
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化图像
    _, binary_image = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

bgFilter=cv2.createBackgroundSubtractorMOG2()
cap=cv2.VideoCapture(0)

def catch(category,num):
    folderDic_raw = {1: './pic_1', 2: 'pic_2', 3: 'pic_3', 4: 'pic_4'}
    folderDic_bgfilter = {1: './pic_1_processed', 2: 'pic_2_processed', 3: 'pic_3_processed', 4: 'pic_4_processed'}
    i = 0
    while True:
        # 读取帧
        ret, frame = cap.read()
        # 显示帧
        cv2.imshow("Camera", frame)

        # 背景减除
        fgMask = bgFilter.apply(frame)
        # 去除噪声
        fgMask = cv2.medianBlur(fgMask, 5)

        ###########################这里是灰度图展示，已经包含了预处理
        ## 调整背景去噪帧的尺寸为256x256
        img_fgmask = cv2.resize(fgMask, (256, 256)) # 256*256的256灰度图
        # 将灰度图像扩展为三个通道的灰度图像
        img_processed3 = np.stack((img_fgmask,) * 3, axis=-1)   # 256*256*3的256灰度图
        img_processed = binary_threshold(img_processed3, 150)   # 256*256，这也是保存到process文件夹的图片形式
        img_processed3 = np.stack((img_processed,) * 3, axis=-1)    # 256*256*3的01灰度图，只用来绘图
        ## 显示背景去噪帧
        cv2.imshow("img_fgmask3", img_processed3)

        # 检测按键，按下 'p' 键保存照片;按下 'q' 键退出循环
        key = cv2.waitKey(1)
        if key == ord('p'):
            ####################彩色图片大小预处理，最终得到灰度图
            # 原始图片
            # 调整帧的尺寸为256x256
            frame_resized = cv2.resize(frame, (256, 256))   # 256*256*3
            # 将帧转换为灰度图像
            img_raw = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)   # 256*256
            ####################下面是文件保存
            folder_raw=folderDic_raw[category]
            folder_bgfilter=folderDic_bgfilter[category]
            file_num = len(os.listdir(folder_bgfilter))   # 不会用到文件，只是需要知道一共有多少文件
            newImgPath_raw=folder_raw+'/'+str(file_num+1)+'.png'
            newImgPath_bgfilter = folder_bgfilter + '/' + str(file_num + 1) + '.png'
            cv2.imwrite(newImgPath_raw,img_raw)
            cv2.imwrite(newImgPath_bgfilter, img_processed)
            print("照片保存成功")
            i += 1
            if i == num:
                print(f"已经拍摄完成所有类别为{category}的照片")
                break
        elif key == ord('q'):
            if i<num:
                print("尚未拍摄完成")
                continue
            break
        elif key == ord('i'):
            print(f'当前已经拍摄了{i}张图片')


catch(4,100)
cap.release()
cv2.destroyAllWindows()
