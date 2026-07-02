import os
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

IMG_SIZE = 224
MODEL_PATH = "ai_detector.keras"
TEST_IMAGE_PATH = "Test/test.jpg"


def preprocess_image(image_path):
    img_bgr = cv2.imread(image_path)

    if img_bgr is None:
        raise ValueError(f"이미지를 불러올 수 없습니다: {image_path}")

    # 화면 출력용 원본 이미지
    display_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # 모델 입력용 이미지
    img_resized = cv2.resize(img_bgr, (IMG_SIZE, IMG_SIZE))
    img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

    # MobileNetV2 train.py에서 preprocess_input을 모델 안에 넣었으므로
    # 여기서는 /255.0 하지 않습니다.
    input_img = np.array(img_rgb, dtype=np.float32)
    input_img = np.expand_dims(input_img, axis=0)

    return display_img, input_img


def main():
    if not os.path.exists(MODEL_PATH):
        print("모델 파일이 없습니다.")
        print("먼저 train.py를 실행해서 ai_detector.keras를 생성하세요.")
        return

    if not os.path.exists(TEST_IMAGE_PATH):
        print("Test 폴더 안에 test.jpg 파일을 넣어주세요.")
        return

    model = tf.keras.models.load_model(MODEL_PATH)

    display_img, input_img = preprocess_image(TEST_IMAGE_PATH)

    print("입력 이미지 shape:", input_img.shape)

    prediction = model.predict(input_img)[0][0]

    ai_probability = prediction * 100
    real_probability = (1 - prediction) * 100

    if prediction >= 0.5:
        result = "AI Generated Image"
        confidence = ai_probability
    else:
        result = "Real Image"
        confidence = real_probability

    print("=" * 40)
    print("AI IMAGE DETECTOR")
    print("=" * 40)
    print(f"파일명: {TEST_IMAGE_PATH}")
    print(f"판별 결과: {result}")
    print(f"신뢰도: {confidence:.2f}%")
    print("-" * 40)
    print(f"AI 확률: {ai_probability:.2f}%")
    print(f"Real 확률: {real_probability:.2f}%")
    print("=" * 40)

    plt.figure(figsize=(8, 6))
    plt.imshow(display_img)
    plt.title(f"{result} ({confidence:.2f}%)")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()