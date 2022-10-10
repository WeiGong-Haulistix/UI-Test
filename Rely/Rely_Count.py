import re
import os


class ExecuteCount:
    def __init__(self):
        pass

    @staticmethod
    def count():
        var = 1
        path = os.path.abspath(os.path.dirname(os.getcwd())) + '/Rely/Rely_Count.py'
        with open(path, 'r', encoding='utf-8') as fl:
            fl.seek(4)
            var_line = fl.readlines()[10]
            # print(var_line)
            num = int(re.search('\\d+', var_line).group()) + 1
            fl.seek(0)
            txt = fl.read().replace(var_line, '        var = ' + str(num) + '\n')
        with open(path, 'w', encoding='utf-8') as file:
            file.write(txt)
        return num


if __name__ == '__main__':
    ct = ExecuteCount()
    print(ct.count())
