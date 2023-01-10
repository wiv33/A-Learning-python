import glob
import tensorflow as tf
import CaptchaCracker as cc

weights_path = 'model/weights.h5'


def train():
    train_img_path_list = glob.glob("sample/train_numbers_only/*.png")

    img_width = 120
    img_height = 50

    # 타겟 이미지 라벨 길이
    max_length = 6
    # 타겟 이미지 라벨 구성요소
    characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    CM = cc.CreateModel(train_img_path_list, img_width, img_height)

    model = CM.train_model(epochs=100)
    model.save_weights(weights_path)


if __name__ == '__main__':
    if False:
        train()

    img_width = 120
    img_height = 50

    # 타겟 이미지 라벨 길이
    max_length = 4
    # 타겟 이미지 라벨 구성요소
    characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    AM = cc.ApplyModel(weights_path, img_width, img_height, max_length, characters)
    img_path = "kcaptcha_image.jpg"
    print(AM.predict(img_path))
