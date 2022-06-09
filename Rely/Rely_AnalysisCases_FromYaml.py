from ruamel.yaml import YAML
import os


class YamlHandle(object):

    @staticmethod
    def file_path(filename):
        """
        初始化要使用的yaml文件路径
        :param filename: 文件名
        :return: str
        """
        path = os.getcwd()
        subpaths = "Testcase"
        if subpaths in path:
            path = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        testcase_file = path + '\\DependencyFiles\\' + filename + '.yaml'
#       print('testcase_file:', testcase_file)
        return testcase_file

    def load(self, filename) -> dict:
        """
        读取yaml文件，获取用例数据
        :param filename: 文件名
        :return: dict
        """
        yaml = YAML(typ='safe')
        with open(file=self.file_path(filename), encoding='utf8') as file:
            data = yaml.load(file)
        return data

    def get_data(self, filename, node) -> list:
        """
        获取节点数据
        :param filename: 文件名
        :param node: 节点名称
        :return: dict&str
        """
        return self.load(filename)[node]
