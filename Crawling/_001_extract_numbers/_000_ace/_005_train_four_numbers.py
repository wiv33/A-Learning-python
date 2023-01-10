import glob
import CaptchaCracker as cc
import os

import numpy as np


class CaptchaModel:
    def __init__(self):
        self.img_width = 120
        self.img_height = 60
        self.max_len = 4
        self.label_characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        self.weights_path = 'model/four_numbers_weights.h5'
        self.train_img_path = glob.glob("sample/train_extract_four_numbers/*.png")

    def train(self, epochs=300):
        model = cc.CreateModel(train_img_path=self.train_img_path, img_width=self.img_width, img_height=self.img_height)
        train_model = model.train_model(epochs, earlystopping=False)
        print('train model', train_model.input_shape, train_model.output_shape)
        train_model.save_weights(self.weights_path)

    def predict(self, predict_img_path):
        am = cc.ApplyModel(weights_path=self.weights_path,
                           img_width=self.img_width,
                           img_height=self.img_height,
                           max_length=self.max_len,
                           characters=self.label_characters)
        print('am model', am.prediction_model.input_shape, am.prediction_model.output_shape)
        return am.predict(predict_img_path)


if __name__ == '__main__':
    captcha_model = CaptchaModel()
    captcha_model.train()
    if not os.path.exists(captcha_model.weights_path):
        captcha_model.train(120)

    if True:
        quit()

    jpeg = '/Users/auto/PycharmProjects/A-Learning-python/Crawling/_000_basic/_003_extract_number/sample/train_extract_four_numbers/0051.png'
    print(captcha_model.predict(jpeg))

    for x in glob.glob("sample/train_four_numbers/*"):
        absolute_path_name = x
        if x.endswith("jpeg"):
            absolute_path_name = x.replace("jpeg", "png")
            os.system(f'mv {x} {absolute_path_name}')

        filename = captcha_model.predict(absolute_path_name)
        save_path = f'sample/valid_four_numbers/{filename}.png'
        print(f'prev: {absolute_path_name}, to: {filename}')
        os.system(f'mv {absolute_path_name} {save_path}')
