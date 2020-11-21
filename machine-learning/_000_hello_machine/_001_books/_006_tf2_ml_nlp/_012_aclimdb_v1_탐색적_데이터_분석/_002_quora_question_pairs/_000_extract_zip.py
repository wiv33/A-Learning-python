import os
from zipfile import ZipFile


def unzip(path):
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            if filename.__contains__(".zip"):
                file = ZipFile(os.path.join(dirname, filename))
                file.extractall(dirname)
                # unzip(os.path.join(dirname, filename))
                print(dirname, filename)
                file.close()


if __name__ == '__main__':
    unzip('./data_in')
