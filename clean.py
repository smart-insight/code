import re
from xlutils.copy import copy

import xlrd
import xlwt

data = xlrd.open_workbook('名单完整版.xlsx')

table = data.sheets()[0]

def clean():
    for i in range(1, 137):
        x = table.cell(i, 3).value
        x = re.sub('检后咨询:\d\d\d\d\d\d\d\d', '', x)
        x = re.sub('地址：海淀区阜成路81号院1号楼', '', x)
        x = re.sub('网站：www.bjtjzx.com3 /\d\d ', '', x)
        x = re.sub('页卡号：\d\d\d\d\d\d\d\d ', '', x)
        x = re.sub('体检代码：\d\d\d\d\d\d\d\d\d\d\d\d\d', '', x)
        wb = copy(data)
        ws = wb.get_sheet(0)
        ws.write(i, 3)
        wb.save('名单.xlsx')
        print(x)











if __name__ == '__main__':
    clean()