from collections import defaultdict

import pandas as pd

df = pd.read_excel("~/Downloads/SRT_data_correlation_analysis.xlsx", skiprows=1)

# print(df.head())

boolean = df['테이블명(한글명)'] == "실적사업다이아"

filteredDf = df[df['테이블명(한글명)'].str.contains("IF table", na=False)]

print(filteredDf.head())

print(filteredDf.iloc[:, 1], filteredDf.iloc[:, 2])

for x in filteredDf.values:
    d = {}
    d['생성주기'] = x[6]
    d['보관주기'] = x[7]
    d['table_IFS'] = x[10]
    d['table_TB'] = x[13]
    for i, y in enumerate(x[2].split(",")):
        d[f"column_{i}"] = y.replace(" ", "")

    pd.DataFrame(data=[d]).to_csv(f"./result/{x[1]}.csv", index=False)
    # localDf = pd.DataFrame(data=x[2])
    # localDf.to_csv("".format("%s.csv", x[1]), header=False, index=False)
