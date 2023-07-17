import os

import cv2


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
            end = False
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
                elif key == ord('q'):
                    end = True
                    break
            if end:
                break
    # 关闭窗口
    cv2.destroyAllWindows()
    print("展示完成")


def showAllFolder(choose=None):
    folderDic_raw = {1: './pic_1', 2: 'pic_2', 3: 'pic_3', 4: 'pic_4'}
    folderDic_bgfilter = {1: './pic_1_processed', 2: 'pic_2_processed', 3: 'pic_3_processed', 4: 'pic_4_processed'}
    if choose == None or choose == 'all':
        for i in range(1, 5):
            showFolder(folderDic_raw[i])
        for i in range(1, 5):
            showFolder(folderDic_bgfilter[i])
    elif choose == 'raw':
        for i in range(1, 5):
            showFolder(folderDic_raw[i])
    elif choose == 'processed':
        for i in range(1, 5):
            showFolder(folderDic_bgfilter[i])
    print("展示完成")


# showAllFolder(choose='processed')

def binary_threshold(image, threshold):
    # 二值化
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化图像
    _, binary_image = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return binary_image


# 需要注意处理的图片
# 2：14，20，
# 3：7，9，10，11，
# 4：4，5，


# aDic={2:[14,20],3:[7,9,10,11],4:[4,5]}
# imgList=[]
# folderDic_bgfilter = {1: './pic_1_processed', 2: 'pic_2_processed', 3: 'pic_3_processed', 4: 'pic_4_processed'}
# for category in (2,3,4):
#     for idx in aDic[category]:
#         imgList.append(cv2.imread(folderDic_bgfilter[category]+'/'+str(idx)+'.png'))

# # 二值化，效果很不错，参数为200
# for i in range(100,256,10):
#     newImage=binary_threshold(imgList[2],i)
#     cv2.imshow('binary',newImage)
#     print(i)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


def binProcess(category, idx):
    folderDic_bgfilter = {1: './pic_1_processed', 2: 'pic_2_processed', 3: 'pic_3_processed', 4: 'pic_4_processed'}
    filePath = folderDic_bgfilter[category] + '/' + str(idx) + '.png'
    img = cv2.imread(filePath)
    newImg = binary_threshold(img, 150)
    cv2.imwrite(filePath, newImg)


def allBinProcess():
    categoryList = range(1, 5)
    idxList = range(1, 21)
    for category in categoryList:
        for idx in idxList:
            binProcess(category, idx)


# allBinProcess()
showAllFolder(choose='processed')
