from openpyxl import Workbook
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
import numpy as np


class OpenpyxTest:
    wb = Workbook()  # 实例化对象
    ws = wb.active  # 默认创建的是索引编号为0的第一页
    ws.title = "健康表"  # 给第一张表起名字

    # 写入数据方面我查了一些资料,决定用pandas里面的dataFrame(表格类型的数据结构),
    # 且openpyxl对dataFrame数据格式也是完美支持
    # 准备数据,数据的key是列索引,行索引自动编码,可以自定义行索引
    def creat_table(self):
        data = {'姓名': ['小王', '小李', '小二', '小白'],
                '性别': ['men', 'men', 'men', 'women'],
                '身高': ['180', '150', '170', '160'],
                '体重': ['170', '160', '150', '140']}
        # 实例化数据对象,并且根据自己想要的排序,如果columns没有的话就默认是rangecolumns
        df = pd.DataFrame(data, columns=['姓名', '性别', '身高', '体重'])

        for i in dataframe_to_rows(df, index=False, header=True):  # index要不要数据的行标题和列标题
            self.ws.append(i)
        self.wb.save("test.xlsx")

    def update_table(self):  # dataFrame处理方法
        # 增加一列为备注
        # 读取文件数据
        df = pd.read_excel('F:\\wanderer_work\\2020-5-8 openpyxl\\aa.xlsx')
        # 计算是否为健康体重，如果是健康体重，则在旁边备注健康，并将姓名打印出来
        # for height in df['身高']:
        #     print(height)
        for i in range(len(df['身高'])):
            print(df['身高'][i])


open = OpenpyxTest()
open.update_table()
