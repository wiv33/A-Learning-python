import pyodbc
import json
import pandas as pd
import re


def remove_txt(s):
    result = ''
    if not s:
        return ''

    try:
        removed_title = re.sub('(((<소제목>).+\n)|((<큰제목>).+\n))', '', s)
        result = re.sub('[^ ㄱ-ㅣ가-힣]+', '', removed_title)
    except TypeError as te:
        print(te)
        print(s)
    return result


# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
info = json.loads(open('db_info.json', 'r').readline())
server = f'tcp:{info["server"]}'
database = info['database']
username = info['username']
password = info['password']
pwd_password = 'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
cnxn = pyodbc.connect(pwd_password)
cursor = cnxn.cursor()

cursor.execute(f'SELECT ART_BDT FROM {info["table"]} WITH (NOLOCK)')
articles = open("articles.tsv", 'w+', encoding='utf-8')
for x in cursor:
    articles.writelines(remove_txt(x[0]) + '\t')
    articles.writelines('\r\n')

articles.close()

df = pd.read_csv('articles.tsv', sep='\t', header=None, index_col=None)
df.columns = ['본문', 'NaN']
print(df.head())
print('=' * 100)
print(df.info())
