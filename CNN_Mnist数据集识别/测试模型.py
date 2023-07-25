import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import mnist
from keras.models import load_model
from keras.utils import to_categorical

# 导入模型
model = load_model('mnist_model.keras')
# 加载MNIST数据集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 数据预处理
train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 评估模型在测试集上的性能
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)


# 展示当前测试的图片
def show_test_image(index):
    plt.imshow(test_images[index].reshape(28, 28), cmap='gray')
    plt.title(f'True label: {test_labels[index].argmax()}')
    plt.show()


while True:
    # 选择要展示的测试图片的索引
    test_index = np.random.randint(0,10000)
    show_test_image(test_index)
