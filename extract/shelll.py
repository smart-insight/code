import xlrd
import xlwt
import re

from xlutils import copy

book = xlrd.open_workbook('诊断分解和超声放射版本.xlsx')
wbook = copy.copy(book)
table = book.sheet_by_index(0)
wtable = wbook.get_sheet(0)
def demo():
    f = open('wait.txt', 'a', encoding='utf-8')
    for i in range(1, 136):
        b = table.cell(i, 10).value
        if len(b) == 0:
            f.write(' '+'\n')
        else:
            x = b.split('。')
            print(x)
            for a in x:
                c = re.compile(u'\d.*\*').findall(a)
                a = re.compile(u'\d.*]').findall(a)
                w = ''.join(c)
                y = ''.join(a)
                print(w, y)
                if y + '*' == w:
                    f.write(y+' ')
                else:
                    f.write(w+' '+y+' ')
            f.write('\n')


def demo2():
    fr = open('wait1.txt', 'a', encoding='utf-8')
    for o in range(1, 136):
        b = table.cell(o, 11).value
        if len(b) == 0:
            fr.write(' ' + '\n')
        else:
            x = b.split('。')
            print(x)
            for a in x:
                c = re.compile(u'\d.*\*').findall(a)
                a = re.compile(u'\d.*]').findall(a)
                w = ''.join(c)
                y = ''.join(a)
                print(w, y)
                fr.write(w + ' ' + y + ' ')
            fr.write('\n')


def demo3():
    fw = open('wait2.txt', 'a', encoding='utf-8')
    for u in range(1, 136):
        b = table.cell(u, 12).value
        if len(b) == 0:
            fw.write(' ' + '\n')
        else:
            x = b.split('。')
            print(x)
            for a in x:
                c = re.compile(u'\d.*\*').findall(a)
                a = re.compile(u'\d.*]').findall(a)
                w = ''.join(c)
                y = ''.join(a)
                print(w, y)
                fw.write(w + ' ' + y + ' ')
            fw.write('\n')

i = 1
def demo4():

    f = open('wait.txt', 'r', encoding='utf-8')
    global i
    for line in f.readlines():
        print(line)

        wtable.write(i, 10, line)
        i += 1


k =1
def demo5():
    fr = open('wait1.txt', 'r', encoding='utf-8')
    global k
    for line in fr.readlines():
        print(line)

        wtable.write(k, 11, line)
        k += 1


l = 1
def demo6():
    fw = open('wait2.txt', 'r', encoding='utf-8')
    global l
    for line in fw.readlines():
        print(line)

        wtable.write(l, 12, line)
        l += 1



if __name__ == '__main__':

    # demo()
    # demo2()
    # demo3()
    demo4()
    demo5()
    demo6()
wbook.save('ool.xlsx')
