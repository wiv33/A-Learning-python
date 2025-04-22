import pandas as pd

df = pd.read_excel("/Users/auto/Documents/한양대_대학원/빅데이터기반_프로젝트/5장_데이터/01_시계열 분석 기초(시도별 주민등록인구).xlsx", engine='openpyxl')

print(df.head())
print(df.T.head())

df.T.to_csv("hanyang.csv")