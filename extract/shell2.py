

import xlrd
import xlwt
import re

from xlutils import copy

book = xlrd.open_workbook('改(补).xlsx')
wbook = copy.copy(book)
table = book.sheet_by_index(0)
wtable = wbook.get_sheet(0)

def run():
    list = ['未见', '未见异常', '未见明显异常']
    nrow = table.nrows
    for i in range(1, nrow):
        data = table.cell(i, 7).value
        # print(data)
        data = data.replace('超声检查报告超声所见：', '', 100)
        data = data.split('。')
        # print(data)
        for o in list:
            data = [k for k in data if o not in k and k != '']
            m = "".join(data)
            # print(m)
            wtable.write(i, 7, m)
        for x in data:
            a = re.compile(u'\d+mmx\d+mm').findall(x)
            b = re.compile(u'\d+\.\d+mmx\d+\.\d+mm').findall(x)
            s_list = []
            if len(a) != 0 and len(b) == 0:
                # print(str(x).split(':')[0])
                # print(' '.join(a))
                s1 = str(x).split(':')[0] + ":" + ' '.join(a) + '\n'
                s_list.append(s1)
                wtable.write(i, 9, '  '.join(s_list))
            if len(b) != 0 and len(a) == 0:
                # print(str(x).split(':')[0])
                # print(''.join(b))
                s2 = str(x).split(':')[0] + ":" + ' '.join(b) + '\n'
                s_list.append(s2)
                wtable.write(i, 9, '  '.join(s_list))
            if len(a) != 0 and len(b) != 0:
                s1 = str(x).split(':')[0] + ":" + ' '.join(a) + '\n'
                s_list.append(s1)
                s2 = str(x).split(':')[0] + ":" + ' '.join(b) + '\n'
                s_list.append(s2)

                wtable.write(i, 9, '  '.join(s_list))

run()
wbook.save('改改改.xlsx')

