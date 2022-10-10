import xlrd
import os
from operator import itemgetter
from itertools import groupby
all_data = {}


class GetTestCase(object):
    def __init__(self):
        path = os.getcwd()
        subpaths = "Testcase"
        if subpaths in path:
            path = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        case_path = path + '\\DependencyFiles\\testData.xls'
        self.workbook = xlrd.open_workbook(case_path)
        self.href = self.workbook.sheet_by_name('href')
        self.title = self.workbook.sheet_by_name('title')

    def get_href(self):
        href_data = {}
        for row in self.href.get_rows():
            if row[0].value == "button":
                pass
            else:
                button = row[0].value
                xpath_val = row[1].value
                href_data[button] = xpath_val
        return href_data

    def get_title(self):
        buttons = []
        bys = []
        values = []
        for row in self.title.get_rows():
            if row[0].value == "button":
                pass
            else:
                buttons.append(row[0].value)
                bys.append(row[1].value)
                values.append(row[2].value)
        title_data = [buttons, bys, values]
        return title_data

    def get_data(self, sheet, case):
        table = self.workbook.sheet_by_name(sheet)
        row_num = table.nrows
        col_num = table.ncols
        s = []
        key = table.row_values(0)  # 这是第一行数据，作为字典的key值

        if row_num <= 1:
            print("No data!")
        else:
            j = 1
            for i in range(row_num - 1):
                d = {}
                values = table.row_values(j)

                if values[0] == case:
                    for x in range(col_num):
                        d[key[x]] = values[x]
                    s.append(d)
                j += 1
            return s


if __name__ == '__main__':
    GetTestCase().get_all_data()
