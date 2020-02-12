import docx
import re
import os
import  pandas as pd
def dataprocess():
    f = open('121915361617_047-62907(刘和平17.8).docx','r',encoding='utf-8')
    lines = []
    for line in f.readlines():
        line = line.strip(' ').strip('\n').strip('\t')
        if len(line) != 0:
            print(line)
            lines.append(line)
    print(lines)




def findAllfile(path,allfile):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            findAllfile(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile


# def process(srcpath,imgproccess_result):
#
#     files = findAllfile(srcpath, [])
#     for facepath in files:
#         data_split = facepath.strip().split("/")
#

def read_docx(path):
    data = docx.Document(path)
    lines = []
    f = open('1.txt', 'w', encoding='utf-8')
    for index, para in enumerate(data.paragraphs):
        # print(index, para.text)
        line = para.text.strip(' ').strip('\n').strip("\t")
        # print(line, len(line), type(line))
        if len(line) != 0 :
            f.write(line)
            lines.append(line)
    # print(lines)

    f.close()


def match():
    logyzm = open("1.txt", 'rb').read()
    temp = logyzm.decode("utf8")
    findword = u"(超声检查报告.*提示)"
    findword2 = u"(放射检查报告.*)"

    pattern = re.compile(findword)
    pattern2 = re.compile(findword2)

    results = pattern.findall(temp)
    results2 = pattern2.findall(temp)
    print(len(results), results)
    print(len(results2),results2)
    # global result, result2
    if len(results) == 0 and len(results2) == 0:
        return str(1), str(1)
    if len(results) != 0 and len(results2) == 0:
        for result in results:
            result = re.sub('检查日期：.*', '', result)
        return result,str(1)
    if len(results) == 0 and len(results2) != 0:
        for result2 in results2:
            result2 = re.sub('检查日期：.*', '', result2)
        return str(1),result2
    if len(results) != 0 and len(results2) != 0:
        for result in results:
            result = re.sub('检查日期：.*', '', result)
    #         k = result[0:2]
    #         v = result[-3:]
    #         if v[-1] == '卡':
    #             v = result[-3:-1]
    #             dict[k] = v
    #         else:
    #             dict[k] = v
    #         # print(k, v)
        for result2 in results2:
            result2 = re.sub('检查日期：.*', '', result2)
        return result, result2
        # print(len(result), len(result2))
        # if len(result) !=0 and len(result2) != 0:
        #     return result, result2
        # elif len(result) !=0 and len(result2) == 0:
        #     return result, 1
        # elif len(result) == 0 and len(result2) != 0:
        #     return 1, result2



        # print(result2)
#
#     for result3 in results3:
#         k3 = result3[0:4]
#         v3 = result3[5:]
#         dict[k3] = v3
#         # print(k3, v3)
#
#     for result4 in results4:
#         k4 = result4[0:7]
#         v4 = result4[7:-2]
#         v4 = re.sub('检后咨询:68866336', '', v4)
#         v4 = re.sub('地址：海淀区阜成路81号院1号楼', '', v4)
#         v4 = re.sub('网站：www.bjtjzx.com3', '', v4)
#         v4 = re.sub('/\d\d ', '', v4)
#         v4 = re.sub(' 页卡号：\d{8} ', '', v4)
#         v4 = re.sub('体检代码：\d{12,13}', '', v4)
#         dict[k4] = v4
#         # print(k4, v4)if




if __name__ == "__main__":
    # read_docx(".docx")
    # # pd = pd.DataFrame(columns=['姓名', '体检日期', '身份证号', '总检结论与建议'])
    f = open('补.txt', 'a', encoding='utf-8')
    o = findAllfile('补/', [])
    for data_path in o:
        read_docx(data_path)
        a, b = match()
        # print(a, b)
        # if a is None:
        #     a = 2
        # if b is None:
        #     b = 2
        # pd = pd.append(dict, ignore_index=True)
        f.write(a + '  ' + b + '\n')
    f.close()
        # print(dict)
        # break
    # print(pd)


