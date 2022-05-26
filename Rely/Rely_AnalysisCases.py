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
        # print(case_path)
        self.workbook = xlrd.open_workbook(case_path)
        self.href = self.workbook.sheet_by_name('href')
        self.title = self.workbook.sheet_by_name('title')
        self.change_menu = self.workbook.sheet_by_name('change_menu')

    def get_all_data(self):
        for i, sheet_obj in enumerate(self.workbook.sheets()):
            all_data[i] = [sheet_obj.row_values(row)
                           for row in range(sheet_obj.nrows)]

        sheets = self.workbook.sheet_names()
        sheet_name = list(enumerate(sheets))
        for i in range(0, len(sheet_name)):
            all_data[sheet_name[i][1]] = all_data[sheet_name[i][0]]
            del all_data[sheet_name[i][0]]
        for cases in ("Readme", "login", "href", "title", "change_menu"):
            del all_data[cases]

        case_trans = {}
        for key in list(all_data.keys()):
            each_case = all_data[key]
            title_name = each_case[0]
            cases_all = []

            for each, items in groupby(each_case, key=itemgetter(0)):
                case_all = {}
                each_case = list(items)
                if each == 'cases':
                    pass
                else:
                    c = []
                    for i in range(0, len(each_case)):
                        s = {}
                        for j in range(0, len(title_name)):
                            s[title_name[j]] = each_case[i][j]
                        c.append(s)
                    case_all['case_name'] = each
                    case_all['case_data'] = c
                if case_all == {}:
                    pass
                else:
                    cases_all.append(case_all)

            case_trans[key] = cases_all
        print(case_trans)
        return case_trans

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

    def get_change_menu(self):
        href_data = {}
        for row in self.change_menu.get_rows():
            if row[0].value == "case_name":
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
