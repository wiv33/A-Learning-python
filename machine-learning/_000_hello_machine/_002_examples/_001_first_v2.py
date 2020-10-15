import pandas as pd

DATA_DIR_PATH = "data/machine-learning/"


def cp(s):
    return "{}{}".format(DATA_DIR_PATH, s)


tags_df = pd.read_csv(cp('tags.csv'))
train_df = pd.read_csv(cp('train.csv'))
user_tag_df = pd.read_csv(cp('user_tags.csv'))
job_companies_df = pd.read_csv(cp('job_companies.csv'))
job_tag_df = pd.read_csv(cp('job_tags.csv'))


def grouping_tags(df: pd.DataFrame, id: str) -> {}:
    result = []
    for u, t in df.groupby(id):
        temp = {}
        temp[id] = u
        temp['{}_tags'.format(id)] = " ".join(df[df[id] == u]['tagID'])
        result.append(temp)

    return pd.DataFrame(result)


job_match_df = grouping_tags(job_tag_df, 'jobID')
user_match_df = grouping_tags(user_tag_df, 'userID')

user_match_df.head(2)

merge_user = pd.merge(train_df, user_match_df, how='left')
complete_merge = pd.merge(merge_user, job_match_df, how='left')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

tfidf = TfidfVectorizer()

tfidf_metric = tfidf.fit_transform(complete_merge.iloc[:, 3:].stack().values)
idf = tfidf.idf_


def l1_normalize(v):
    return v / np.sum(v)

euclidean_distances(1, 2)