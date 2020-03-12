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

# 상품 가짓수가 1인 사용자 id
min_product_user_li = [k for k, v in user_product_dict.items() if len(v) == 1]

# 구매한 상품의 가짓수가 600개 이상인 사용자 id
max_product_user_li = [k for k, v in user_product_dict.items() if len(v) >= 600]

print("# of users purchased one product:%d" % (len(min_product_user_li)))
print("# of users purchased more than 600 product:%d" % (len(max_product_user_li)))


# 찾아낸 사용자를 군집화에 사용할 user_product_dict 에서 제회
user_product_dict = {k:v for k, v in user_product_dict.items() if 1 < len(v) <= 600}

print("# of left user:%d" % len(user_product_dict))

# 남아있는 사용자가 구매한 상품에서도 0에서 시작하는 고유 ID를 부여한다.
# 데이터셋에서 지외된 사용자가 구매한 상품은 군집화에서 사용하지 않기 때문에 이러한 처리를 한다.
id_product_dict = {}
for product_set_li in user_product_dict.values():
    for x in product_set_li:
        if x in id_product_dict:
            product_id = id_product_dict[x]
        else:
            id_product_dict.setdefault(x, len(id_product_dict))

print("# of left items:%d" % len(id_product_dict))