import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from scipy import stats

# 사용자 ID를 키로 갖고 상품 코드의 셋을 값으로 갖는 딕셔너리와
# 상품 코드를 키로 갖고 사용자 ID의 셋을 값으로 갖는 딕셔너리
user_product_dict = {}
product_user_dict = {}

# 상품 코드를 키로 갖고 상품명을 값으로 갖는 딕셔너리
# 군집화의 내용을 확인하는 단계에서 상품명을 사용한다.
product_id_name_dict = {}

excel = pd.read_excel("./_000_Online_Retail.xlsx", header=1)
items = excel.dropna() # row에 NaN column 이 한개 이상 포함되어 있을 경우 제외시킨다.
for i, v in items.iterrows():
    user_code = v.values[6]
    product_id = v.values[1]
    product_name = v.values[2]
    country = v.values[7]

    # 유저 코드가 없거나 영국이 아닐 경우
    if country != 'United Kingdom':
        continue

    invoiceDate = v.values[4]
    # 연도 에러 처리
    try:
        invoice_year = invoiceDate.year
    except ValueError:
        print("Occurred Error: {}".format(invoiceDate))
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
# 각 사용자가 구매한 상품 가짓수로 기초 통계량을 출력.
print(stats.describe(product_per_user_li))

plot_data_all = Counter(product_per_user_li)
plot_data_x = list(plot_data_all.keys())
plot_data_y = list(plot_data_all.values())
plt.xlabel('고유 상품 가짓수')
plt.ylabel('사용자 수')
plt.scatter(plot_data_x, plot_data_y, marker="+")

plt.show()
