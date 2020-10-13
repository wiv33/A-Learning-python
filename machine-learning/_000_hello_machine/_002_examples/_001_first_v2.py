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
        temp['{}_tags'.format(id)] = " ".join(df[df[id] == u]['tagID'].values)
        result.append(temp)

    return pd.DataFrame(result)


job_match_df = grouping_tags(job_tag_df, 'jobID')
user_match_df = grouping_tags(user_tag_df, 'userID')

