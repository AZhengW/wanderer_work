import csv
from pandas.core.frame import DataFrame
import pandas as pd
import xlrd

import re, time

file_name = "C:\\Users\\56384\\Desktop\\消耗数据(1).csv"
file_name1 = "C:\\Users\\56384\\Desktop\\新建文件夹\\规格匹配.xlsx"
tmp_lst = []
with open(file_name, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tmp_lst.append(row)
df = pd.DataFrame(tmp_lst[1:], columns=tmp_lst[0])


data = xlrd.open_workbook(file_name1)
sheet = data.sheet_by_index(0)
cols = sheet.col_values(0)
cols2 = sheet.col_values(1)
df['规格名称'] = df['规格名称'].replace(cols, cols2)
df['推广计划名称'] = df['推广计划名称'].str.extract('(^[^:]{3})', expand=True)
list = ["展现量",'点击量','广告消耗','订单行量','订单金额']
for i in range(len(list)):
    df[list[i]] =pd.to_numeric(df[list[i]])
value = df.groupby(['规格名称', '推广计划名称'])[['展现量', '点击量', '广告消耗', '订单行量', '订单金额']]
aa = value.sum()
aa.to_excel('D:\\a.xls', encoding='utf-8')
print(aa)

