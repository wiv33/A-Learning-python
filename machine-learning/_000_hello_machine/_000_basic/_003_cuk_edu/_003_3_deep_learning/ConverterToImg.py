import os
import cv2


def to_jpg(filename, root_path='C:\\Users\\wivps\\Videos'):
    vidcap = cv2.VideoCapture('%s\\%s.mp4' % (root_path, filename))
    img_dirs = '%s/%s' % (root_path, filename)
    if not os.path.exists(img_dirs):
        os.makedirs(img_dirs)

    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("%s\\frame%d.jpg" % (img_dirs, count), cv2.rotate(image, cv2.ROTATE_180))  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1


if __name__ == '__main__':
    filename = 'VID_20220701_003209'
    ROOT_PATH = 'C:\\Users\\wivps\\Videos'
    to_jpg(filename, ROOT_PATH)

# todo style gan 사용해서  images/filename 이미지 스타일 변경 후 mp4 파일로 만들기.
