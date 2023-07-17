import os

import cv2


def displayPic(folder, name):
    # 读取保存的图像文件
    image_path = folder + '/' + name  # 图像文件的路径
    image = cv2.imread(image_path)
    # 显示图像
    cv2.imshow("Saved Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def showAll(folder):
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


def deletePic(folder, name):
    # 图像文件夹路径
    folder_path = folder

    # 要删除的特定图片文件名
    specific_image = name

    # 构建特定图片的完整路径
    image_path = os.path.join(folder_path, specific_image)

    # 检查特定图片是否存在
    if os.path.isfile(image_path):
        # 删除特定图片
        os.remove(image_path)
        print("已删除特定图片:", specific_image)
    else:
        print("特定图片不存在:", specific_image)


folderDic = {1: './pic_1', 2: 'pic_2', 3: 'pic_3', 4: 'pic_4'}
showAll(folderDic[1])
