import pandas as pd

date_list = [
    {'yyyy-mm-dd': '2000-06-27'},
    {'yyyy-mm-dd': '2002-09-27'},
    {'yyyy-mm-dd': '2005-03-27'},
]

df = pd.DataFrame(data=date_list, columns=['yyyy-mm-dd'])


def extract_year(col):
    return col.split("-")[0]


df['year'] = df['yyyy-mm-dd'].apply(extract_year)

print(df)


def get_age(year, current_year, pr):
    return pr(current_year - int(year))


df['age'] = df['year'].apply(get_age, current_year=2018, pr=lambda x: x ** 2)

print(df, end='\n\n')


# parameter의 순서가 중요하다.
def make_introduce(age, prefix, suffix):
    return '{0} {1} {2}'.format(prefix, age, suffix)


df['introduce'] = df['age'].apply(make_introduce, prefix='my age is ', suffix=' great')

print(df, end='\n\n\n')


# 여러 개 컬럼 apply 사용
# row를 parameter로 전달한다.
def get_introduce_2(row):
    return 'i was born in' + str(row.year) + ' my age ' + str(row.age)


df['introduce_2'] = df.apply(get_introduce_2, axis=1)
print(df)
