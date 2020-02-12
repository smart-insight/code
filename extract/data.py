from cocoNLP.extractor import extractor
import hanlp
# ex = extractor()
#
#
# def data_res():
#     f = open('./extract/res.txt', 'r', encoding='utf-8')
#     fw = open('./extract/res_data.txt', 'w+', encoding='utf-8')
#     result = f.read()
#     result = result.split('\n\n\n\n\n\n')
#     for i in result:
#         i = i.replace('\n', ',')
#         fw.write(i+'\n')
#
#         # print(i)
#     f.close()
#     fw.close()
# # data_res()
#
def test_time():
    f = open('./extract/res_data.txt', 'r', encoding='utf-8')
    list_test = []

    for i in f.readlines():
        list_test.append(i.strip('\n'))

        # times = ex.extract_time(i)
        # names = ex.extract_name(i)
        # location = ex.extract_locations(i)
        # print(times, names, location)
    return list_test
#
# res = test_time()
# # print(res)


# print(hanlp.pretrained.ALL)
def run():
    recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_ALBERT_BASE_ZH)
    res = test_time()
    ret = []
    for i in res:
        i = i.split(',')
        for k in i :
            ret.append(list(k))
        recognizer(ret)
if __name__ == '__main__':
    run()