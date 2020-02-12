import sys

import xlwt

sys.setrecursionlimit(100000000)
book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('1', cell_overwrite_ok=True)

n = 1
def dataprocess():
    f = open('122511195151.txt', 'r', encoding='utf-8')
    lines = []
    for line in f.readlines():
        line = line.strip().split(' ')
        line = list(filter(lambda x: x, line))
        # print(line,len(line))
        print(line)
        global n
        for j in range(len(line)):
            print(n, j, line[j])
            sheet.write(n, j, line[j])
        n = n + 1
        lines.append(line)


if __name__ == '__main__':
    dataprocess()
book.save('2.xlsx')