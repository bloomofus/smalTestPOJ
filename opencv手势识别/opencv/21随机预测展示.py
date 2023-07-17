import random
import os

import cv2
import numpy as np
from keras.models import load_model
from sklearn.model_selection import train_test_split

# 加载保存的模型参数
loaded_model = load_model('10手势识别模型.keras')
folderDic_bgfilter = {1: './pic_1_processed', 2: 'pic_2_processed', 3: 'pic_3_processed', 4: 'pic_4_processed'}


def predict(img):
    global loaded_model
    # 目前img是256*256*3的双色图
    img=img[:,:,0]  # 256*256
    # 这里的img是经过预处理的256*256的01双色图
    img = np.expand_dims(img, axis=-1)
    resultList = loaded_model.predict(np.array([img, ]))[0]
    idx = 0
    for i in range(len(resultList)):
        if resultList[i] >= resultList[idx]:
            idx = i
    if resultList[idx]<=0.7:
        # 没有置信度
        return 0
    return idx + 1

while True:

    # 获取1、2、3或4中的随机一个数
    rand_category = random.randint(1, 4)
    rand_idx= random.randint(1, len(os.listdir(folderDic_bgfilter[rand_category])))
    img=cv2.imread(folderDic_bgfilter[rand_category]+'/'+str(rand_idx)+'.png')
    pred=predict(img)
    print("now category:",rand_category)
    print("pred:",pred)
    # cv2.imshow(str(pred),img)
    a=input("")
    cv2.destroyAllWindows()
    if a=='q':
        break
cv2.destroyAllWindows()
