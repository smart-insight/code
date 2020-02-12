import re
from xlutils.copy import copy

import xlrd
import xlwt

data = xlrd.open_workbook('北京体检人员信息汇总.xlsx')

table = data.sheets()[0]

def clean():
    for i in range(1, 136):
        x = table.cell(i, 3).value

        print(x)




if __name__ == '__main__':
    clean()