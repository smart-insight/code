import re

import xlrd
import xlwt
from xlutils import copy
import openpyxl

# book = xlrd.open_workbook('名单完整版.xlsx')
# wbook = copy.copy(book)
# table = wbook.get_sheet(0)
# n = 6
# def demo():
#     f = open('报告.txt', 'r', encoding='utf-8')
#     for i in f.readlines():
#         i = i.strip('\n').split('  ')
#         a = re.sub('提示', '', i[0])
#         a = re.sub('检后咨询.*', '', a)
#         print(i)
#         print(a, i[-1])
#         global n
#         table.write(n, 7, a)
#         table.write(n, 8, i[-1])
#         n = n+1


def demo2():
    book = xlrd.open_workbook('2.xls')
    wbook = copy.copy(book)
    table = book.sheet_by_index(0)
    wtable = wbook.get_sheet(0)
    for i in range(1, 136):
        a = table.cell(i, 3).value
        a = re.sub('检后咨询.*体检代码：[0-9]{12,13}', '', a)
        result1 = re.compile(u'重大阳性体征需及时诊治.*重要慢病').findall(a)
        result2 = re.compile(u'重要慢病及阳性体征.*一般疾病').findall(a)
        result3 = re.compile(u'一般疾病及阳性体征.*其他异常').findall(a)
        result4 = re.compile(u'其他异常.*').findall(a)
        for r in result1:
            r = re.sub('重要慢病.*', '', r)
            wtable.write(i, 9, r)
        for s in result2:
            s = re.sub('一般疾病.*', '', s)
            wtable.write(i, 10, s)
        for t in result3:
            t = re.sub('重要慢病.*', '', t)
            wtable.write(i, 11, t)
        for u in result4:
            u = re.sub("'}", '', u)
            wtable.write(i, 12, u)

    wbook.save('3.xlsx')



        # print(a,result1,result2,result3,result4)
        # break





if __name__ == '__main__':
#     demo()
# wbook.save('2.xls')
    demo2()
