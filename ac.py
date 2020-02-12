#coding:utf-8

from xlutils.copy import copy
import os
import pickle
import codecs
import xlrd
import sys
sys.setrecursionlimit(100000)


class TrieNode:
    def __init__(self):
        self.success = dict()  # 转移表
        self.failure = None  # 错误表
        self.emits = set()  # 输出表


class CreateAcAutomaton(object):

    def __init__(self, patterns, save_path="  "):
        """
        :param patterns:  模式串列表
        :param save_path:   AC自动机持久化位置
        """
        self._savePath = save_path.strip()
        assert isinstance(self._savePath, str) and self._savePath != ""
        self._patterns = patterns
        if os.path.exists(self._savePath):
            self._root = self.__load_corasick()
        else:
            self._root = TrieNode()
            self.__insert_node()
            self.__create_fail_path()
            self.__save_corasick()

    def __insert_node(self):
        """
        Create Trie
        """
        for pattern in self._patterns:
            line = self._root
            for character in pattern:
                line = line.success.setdefault(character, TrieNode())
            line.emits.add(pattern)

    def __create_fail_path(self):
        """
        Create Fail Path
        """
        my_queue = list()
        for node in self._root.success.values():
            node.failure = self._root
            my_queue.append(node)
        while len(my_queue) > 0:
            gone_node = my_queue.pop(0)
            for k, v in gone_node.success.items():
                my_queue.append(v)
                parent_failure = gone_node.failure

                while parent_failure and k not in parent_failure.success.keys():
                    parent_failure = parent_failure.failure
                v.failure = parent_failure.success[k] if parent_failure else self._root
                if v.failure.emits:
                    v.emits = v.emits.union(v.failure.emits)

    def __save_corasick(self):
        with codecs.open(self._savePath, "wb") as f:
            pickle.dump(self._root, f)

    def __load_corasick(self):
        with codecs.open(self._savePath, "rb") as f:
            try:
                return pickle.load(f)
            except EOFError:
                return None

    def search(self, context):
        """"""
        search_result = list()
        search_node = self._root
        for char in context:
            while search_node and char not in search_node.success.keys():
                search_node = search_node.failure
            if not search_node:
                search_node = self._root
                continue
            search_node = search_node.success[char]
            if search_node.emits:
                search_result += search_node.emits
        return search_result



def ourdict():
    f = open('del/体征和可能诱发病.txt', 'r', encoding='utf-8')
    list = []
    for idx, i in enumerate(f.readlines()):
        if idx == 3000:
            break
        else:
            if len(i) == 0:
                continue
            else:
                i = i.strip()
                list.append(i)
    return list


def surgerydict():
    f = open('information/手术.txt')







if __name__ == "__main__":
    data = ourdict()
    # print(data)
    # data = ['甘油三脂', '心脑血管']
    book = xlrd.open_workbook('北京体检人员信息汇总.xlsx')
    table = book.sheets()[0]
    wb = copy(book)
    ws = wb.get_sheet(0)
    for a in range(1, 136):
        s = table.cell(a, 3).value
        ct = CreateAcAutomaton(data, "model.pkl")
        result = list(set(ct.search(s)))
        print(result)
        # for idx, i in enumerate(result):
        i = ' '.join(result)
        ws.write(a, 4, i)
    wb.save('aaa.xlsx')

        # print(result)
