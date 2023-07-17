import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import load_model

# 加载保存的模型参数
loaded_model = load_model('08my_model.keras')

# 加载手写体数据集（MNIST）
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 数据预处理，将像素值归一化到0到1之间，并扩展维度以适应CNN的输入要求
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

# 将类别标签进行独热编码
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 使用加载的模型进行预测等操作
predictions = loaded_model.predict(X_test[:10])
print("pred:", predictions)
print("real:", y_test[:10])
