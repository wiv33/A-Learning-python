import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split

DATA_IN_PATH = './data_in/'

TRAIN_Q1_DATA_FILE = 'train_q1.npy'
TRAIN_Q2_DATA_FILE = 'train_q2.npy'
TRAIN_LABEL_DATA_FILE = 'train_label.npy'

# tag::get 훈련 데이터[]
train_q1_data = np.load(open(DATA_IN_PATH + TRAIN_Q1_DATA_FILE, 'rb'))
train_q2_data = np.load(open(DATA_IN_PATH + TRAIN_Q2_DATA_FILE, 'rb'))
train_labels = np.load(open(DATA_IN_PATH + TRAIN_LABEL_DATA_FILE, 'rb'))
# end::get 훈련 데이터[]

# [a], [b] => [[a], [b]]
train_input = np.stack((train_q1_data, train_q2_data), axis=1)

print(train_input.shape)

train_input, eval_input, train_label, eval_label = train_test_split(train_input, train_labels, test_size=.2,
                                                                    random_state=4242)

train_data = xgb.DMatrix(train_input.sum(axis=1), label=train_label)  # 학습 데이터 읽어오기
eval_data = xgb.DMatrix(eval_input.sum(axis=1), label=eval_label)  # 평가 데이터 읽어오기
# MAX_LENGTH = 31
# eval.data.feature_name
# ['f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13',
# 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25', 'f26', 'f27', 'f28', 'f29', 'f30']


data_list = [(train_data, 'train'), (eval_data, 'valid')]

# 모델에게 전달할 param
params = {
    'objective': 'binary:logistic',  # 이진 로지스틱 예측
    'eval_metric': 'rmse'  # root mean square error 를 사용
}

# tag::학습 == fit[]
bst = xgb.train(params, train_data, num_boost_round=1000, evals=data_list, early_stopping_rounds=10)
# end::학습 == fit[]


# tag::테스트 데이터 가져오기[]
TEST_Q1_DATA_FILE = 'test_q1.npy'
TEST_Q2_DATA_FILE = 'test_q2.npy'
TEST_ID_DATA_FILE = 'test_id.npy'

test_q1_data = np.load(open(DATA_IN_PATH + TEST_Q1_DATA_FILE, 'rb'))
test_q2_data = np.load(open(DATA_IN_PATH + TEST_Q2_DATA_FILE, 'rb'))
test_id_data = np.load(open(DATA_IN_PATH + TEST_ID_DATA_FILE, 'rb'), allow_pickle=True)
# end::테스트 데이터 가져오기[]


# tag::예측하기[]
test_input = np.stack((test_q1_data, test_q2_data), axis=1)
test_data = xgb.DMatrix(test_input.sum(axis=1))
test_predict = bst.predict(test_data)
# end::예측하기[]

DATA_OUT_PATH = "./data_out/"
import os
import pandas as pd
if not os.path.exists(DATA_OUT_PATH):
    os.makedirs(DATA_OUT_PATH)

output = pd.DataFrame({'test_id': test_id_data, 'is_duplicate': test_predict})
output.to_csv(DATA_OUT_PATH + 'sample_xgb.csv', index=False)

# kaggle competitions submit -c quora-question-pairs -f sample_xgb.csv -m "submit predict by xgb"