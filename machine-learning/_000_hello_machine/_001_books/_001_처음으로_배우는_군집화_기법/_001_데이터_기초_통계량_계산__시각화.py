import time
from scipy import stats
from openpyxl import load_workbook


user_product_dict = {}
product_user_dict = {}

wb = load_workbook("./_000_Online_Retail.xlsx", data_only=True)
ws = wb['Online Retail']


