import glob
import time

import CaptchaCracker as cc
import os

import numpy as np
from PIL import Image


class CaptchaModelSix:
    def __init__(self):
        self.required_check_dir_path = "model/required_check_eight_numbers"
        self.predict_new_img_path = "model/train_six_extract_numbers/*"
        self.img_width = 70
        self.img_height = 30
        self.max_len = 6
        self.label_characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        self.weights_path = 'model/six_numbers_weights.h5'
        self.train_imgs = glob.glob("model/train_six_numbers/*.png")
        self.actual_train_imgs = glob.glob("model/resize_test/result/*.png")

        self.resize_dir_path = "model/resize_test"
        self.resized_imgs = glob.glob("model/resize_test/result/*.png")

        if not os.path.exists(self.weights_path):
            # for x in self.train_imgs:
            #     self.resize(x)
            self.train()

    def train(self, epochs=300):
        model = cc.CreateModel(train_img_path=self.train_imgs, img_width=self.img_width, img_height=self.img_height)
        train_model = model.train_model(epochs, earlystopping=False)
        print('train model', train_model.input_shape, train_model.output_shape)
        train_model.save_weights(self.weights_path)

    def predict(self, _predict_img_path):
        predict_img_path = self.resize(_predict_img_path)
        am = cc.ApplyModel(weights_path=self.weights_path,
                           img_width=self.img_width,
                           img_height=self.img_height,
                           max_length=self.max_len,
                           characters=self.label_characters)
        print('am model', am.prediction_model.input_shape, am.prediction_model.output_shape)
        return am.predict(predict_img_path)

    def predict_new_imgs(self):
        for f_n in glob.glob(self.predict_new_img_path):
            absolute_path_name = f_n
            if f_n.endswith("jpeg"):
                absolute_path_name = f_n.replace("jpeg", "png")
                os.system(f'mv {f_n} {absolute_path_name}')

            filename = captcha_model.predict(absolute_path_name)
            save_path = f'{self.required_check_dir}/{filename}.png'
            print(f'prev: {absolute_path_name}, to: {filename}')
            os.system(f'mv {absolute_path_name} {save_path}')

    def resize(self, file):
        img = Image.open(file)
        img_resize_lanczos = img.resize((self.img_width, self.img_height))
        # return img_resize_lanczos
        img_resize_lanczos.save(f'{self.resize_dir_path}/result/{file.split("/")[-1]}')
        return f'{self.resize_dir_path}/result/{file.split("/")[-1]}'


if __name__ == '__main__':
    captcha_model = CaptchaModelSix()
    captcha_model.train()
    # if not os.path.exists(captcha_model.weights_path):
    #     captcha_model.train()

    print(captcha_model.predict(
        '/Users/auto/PycharmProjects/A-Learning-python/Crawling/_001_extract_numbers/_001_sm3/model/train_six_numbers/927117.png'))

    # for x in captcha_model.train_img_path:
    #     captcha_model.resize(x)

    # captcha_model.resize("/Users/auto/PycharmProjects/A-Learning-python/Crawling/_001_extract_numbers/_001_sm3/model/train_six_numbers/314431.png")
    # captcha_model.resize("/Users/auto/PycharmProjects/A-Learning-python/Crawling/_001_extract_numbers/_001_sm3/model/train_numbers_only/020853.png")
