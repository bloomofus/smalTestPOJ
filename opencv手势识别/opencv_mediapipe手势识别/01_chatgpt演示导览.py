import cv2
import mediapipe as mp

# 初始化Mediapipe的手势模型
mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头帧
    ret, frame = cap.read()
    if not ret:
        break

    # 将图像从BGR转换为RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 使用Mediapipe进行手势检测
    results = mp_hands.process(rgb_frame)

    # 绘制手势识别结果
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                # 获取手部关键点坐标
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])

                # 在图像上绘制关键点
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # 显示图像
    cv2.imshow('Hand Gesture Recognition', frame)

    # 检测按键，按下ESC键退出
    key = cv2.waitKey(1)
    if key == 27:
        break

# 释放摄像头和关闭窗口
cap.release()
cv2.destroyAllWindows()
