import pandas as pd
import zipfile


def unzip(source_file, dest_path):
    with zipfile.ZipFile(source_file, 'r') as zf:
        zf.extractall(path=dest_path)
        zf.close()


unzip(
    'C:\develop\projects\python\PycharmProjects\A-Learning-python\machine-learning\_000_hello_machine\_000_basic\_003_tensorflow_cuk_edu\_002_2_ml\data/20201024194536.zip',
    'C:\develop\projects\python\PycharmProjects\A-Learning-python\machine-learning\_000_hello_machine\_000_basic\_003_tensorflow_cuk_edu\_002_2_ml\data')
