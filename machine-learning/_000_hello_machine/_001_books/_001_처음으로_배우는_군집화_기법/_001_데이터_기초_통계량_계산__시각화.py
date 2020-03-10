import time
from scipy import stats
from openpyxl import load_workbook
import pandas as pd, xlrd

# 데이터 구조 정의
# 사용자 ID를 키로 갖고 상품 코드의 셋을 값으로 갖는 딕셔너리와
# 상품 코드를 키로 갖고 사용자 ID의 셋을 값으로 갖는 딕셔너리
user_product_dict = {}
product_user_dict = {}

# 상품 코드를 키로 갖고 상품명을 값으로 갖는 딕셔너리
# 군집화의 내용을 확인하는 단계에서 상품명을 사용한다.
product_id_name_dict = {}

# wb = load_workbook("./_000_Online_Retail.xlsx", data_only=True)
# ws = wb['Online Retail']
excel = pd.read_excel("./_000_Online_Retail.xlsx", header=1)
for i in excel.iterrows():
    print(i)
    user_code = excel[i]
    product_id = stockCode
    product_name = Description

    # 유저 코드가 없거나 영국이 아닐 경우
    if len(user_code) <= 0 or country != 'United Kingdom':
        continue

    # 연도 에러 처리
    try:
        invoice_year = time.strptime(invoiceDate, '%m/%d/%y %H:%M').tm_year
    except ValueError:
        continue

    if invoice_year != 2011:
        continue

    # 상품 가짓수를 고려하므로 상품 코드를 셋으로 저장
    user_product_dict.setdefault(user_code, set())
    user_product_dict[user_code].add(product_id)

    product_user_dict.setdefault(product_id, set())
    product_user_dict[product_id].add(user_code)

    product_id_name_dict[product_id] = product_name

# 각 사용자가 구매한 상품 가짓수로 리스트 생성
product_per_user_li = [len(x) for x in user_product_dict.values()]

print("# of users: ", len(user_product_dict))
print("# of products: ", len(product_user_dict))

# 각 사용자가 구매한 상품 가짓수로 기초 통계량을 출력.
print(stats.describe(product_per_user_li))