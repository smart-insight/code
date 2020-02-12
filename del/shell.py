import os
import xlrd
from tqdm import tqdm

def all_files_path(rootDir):
    f1 = open('dir.txt', 'a', encoding='utf-8')
    filepaths = []
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            file_path = os.path.join(root, file)
            filepaths.append(file_path)
        for filepath in filepaths:
            f1.write(filepath + '\n')


def strueture_data():

    f2 = open('三级节点.txt', 'a', encoding='utf-8')
    f3 = open('二三级关系.txt', 'a', encoding='utf-8')
    f4 = open('dir.txt', 'r', encoding='utf-8')

    for filepath in tqdm(f4.readlines()):
        filepath = filepath.strip()
        book = xlrd.open_workbook(filepath)
        table = book.sheets()[0]
        nrows= table.nrows
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for nrow in range(2, nrows):
            id = str(table.cell(nrow, 0)).strip().split(':')[-1]
            name = str(table.cell(nrow, 1)).strip().split(':')[-1]
            lastname = str(table.cell(0, 1)).strip().split(':')[-1]
            list1.append(id)
            list1.append(name)
            list2.append(list1)
            list1 = []

            list3.append(lastname)
            list3.append(name)
            list4.append(list3)
            list3 = []
        # for i in list2:
        # print(list2, len(list2))
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                f2.write(str(list2[i][j]))
                f2.write('\t')
            f2.write('\n')
        # print(list4)
        for a in range(len(list4)):
            for b in range(len(list4[a])):
                f3.write(str(list4[a][b]))
                f3.write('\t')
            f3.write('\n')







    f2.close()
    f3.close()
    f4.close()




def test():
    f = open('三级节点.txt', 'r', encoding='utf-8')
    for i in f.readlines():
        print(i, type(i))

if __name__ == '__main__':
    # all_files_path('.\提取的数据')
    strueture_data()
    # test()