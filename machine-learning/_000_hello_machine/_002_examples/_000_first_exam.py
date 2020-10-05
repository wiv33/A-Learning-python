import pandas as pd
import tensorflow as tf
from sklearn.decomposition import PCA
from tensorflow import keras


def find_column_seq(col):
    for i, x in enumerate(df_independent.columns):
        if col == x:
            return i, x


def update_col_in_df(update_df: pd.DataFrame, id: str, tags: []):
    for i in range(len(update_df[id])):
        if len(tags[update_df[id][i]]) > 0:
            for j in tags[update_df[id][i]]:
                j_idx = find_column_seq(j)[0]
                update_df.iloc[i: i + 1, j_idx:j_idx + 1] += 1


def grouping_tags(df: pd.DataFrame, id: str) -> {}:
    result = {}
    for u, t in df.groupby(id):
        result[u] = df[df[id] == u]['tagID'].values

    return result


train = pd.read_csv('./data/machine-learning/train.csv')
df_tag_map = pd.read_csv('./data/machine-learning/tags.csv')
job_companies = pd.read_csv('./data/machine-learning/job_companies.csv')
user_tag = pd.read_csv('./data/machine-learning/user_tags.csv')
job_tag = pd.read_csv('./data/machine-learning/job_tags.csv')

독립 = train[:][['userID', 'jobID']]
tt = df_tag_map.transpose()
tt.columns = tt.values[0]
df_merge = pd.merge(독립, job_companies[['jobID', 'companyID']])
df_concat = pd.concat([df_merge, tt], ignore_index=True)
df_concat.drop(df_concat.index[[6000, 6001]], inplace=True)
df_independent = df_concat.fillna(0)

# Try using .loc[row_indexer,col_indexer] = value instead

update_col_in_df(df_independent, 'userID', grouping_tags(user_tag.drop_duplicates(), 'userID'))
# df_independent
update_col_in_df(df_independent, 'jobID', grouping_tags(job_tag.drop_duplicates(), 'jobID'))

df_train = df_independent
pca = PCA(n_components=3)
df_train = pca.fit_transform(df_train)
print(df_train.shape)
df_y = train['applied']

X = tf.keras.layers.Input(shape=(6000,))
H = tf.keras.layers.Flatten()(X)
H = tf.keras.layers.Dropout(rate=0.3)(H)

H = tf.keras.layers.Activation(activation='swish')(H)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Dense(units=40000)(H)

H = tf.keras.layers.Activation(activation='swish')(H)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Dense(units=3600)(H)

Y = tf.keras.layers.Dense(units=1, activation='sigmoid')(H)

model = tf.keras.Model(X, Y)
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(df_train, df_y, batch_size=128, epochs=33)
model.summary()
