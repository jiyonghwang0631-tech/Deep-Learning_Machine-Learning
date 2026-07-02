import os
import tensorflow as tf
import matplotlib.pyplot as plt

IMG_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 20

MODEL_PATH = "ai_detector.keras"

AI_DIR = "Ai"
REAL_DIR = "Real"


def main():
    print("데이터셋 불러오는 중...")

    # 현재 폴더 구조:
    # AI_Image_Classifier/
    # ├── Ai
    # ├── Real
    # ├── Test
    # ├── train.py
    # └── predict.py

    train_ds = tf.keras.utils.image_dataset_from_directory(
        ".",
        labels="inferred",
        label_mode="binary",
        class_names=["Real", "Ai"],  # Real = 0, AI = 1 로 고정
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        ".",
        labels="inferred",
        label_mode="binary",
        class_names=["Real", "Ai"],  # Real = 0, Ai = 1 로 고정
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE
    )

    print("클래스 순서:", train_ds.class_names)
    print("Real = 0, Ai = 1")

    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

    # 데이터 증강
    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.1),
        tf.keras.layers.RandomZoom(0.1),
    ])

    # MobileNetV2 전처리 함수
    preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input

    # 사전 학습된 MobileNetV2 불러오기
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(IMG_SIZE, IMG_SIZE, 3),
        include_top=False,
        weights="imagenet"
    )

    # 기존 MobileNetV2 부분은 학습하지 않음
    base_model.trainable = False

    # 모델 구성
    inputs = tf.keras.Input(shape=(IMG_SIZE, IMG_SIZE, 3))

    x = data_augmentation(inputs)
    x = preprocess_input(x)

    x = base_model(x, training=False)

    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(0.4)(x)

    outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)

    model = tf.keras.Model(inputs, outputs)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    print("MobileNetV2 전이학습 시작...")

    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS
    )

    model.save(MODEL_PATH)

    print("=" * 40)
    print("학습 완료")
    print(f"모델 저장 완료: {MODEL_PATH}")
    print("=" * 40)

    plt.plot(history.history["accuracy"], label="Train Accuracy")
    plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("MobileNetV2 Ai Image Detector Accuracy")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()