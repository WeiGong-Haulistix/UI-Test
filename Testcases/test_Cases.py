from Common.common_Login import login_by
from Rely.Rely_ExecuteMethod import change_href
from Rely.Rely_ExecuteMethod import case_common
from Rely.Rely_ExecuteMethod import case_to_menu
from Rely.Rely_StartApplication import start_saas
from Rely.Rely_AnalysisCases import GetTestCase
from Rely.Rely_AnalysisCases_FromYaml import YamlHandle
import unittest
from ddt import ddt, data, unpack
# import numpy

# Get cases from excel
cases = GetTestCase()
all_data = cases.get_all_data()
# cases_data = all_data['driver']
saas_login = cases.get_data('login', 'saas login')
href_data = cases.get_href()
change_menu_data = cases.get_change_menu()

saas_driver = start_saas()

'''
    从Case_Config.yaml文件中取出满足要求的用例名
    将匹配的用例文件写入到cases_data
'''
cases_list = YamlHandle().load('Case_Config')
cases_data = []
for i in range(1, len(cases_list)):
    if cases_list[i]['case tag'] in cases_list[0]['tag_setting'] \
            and cases_list[i]['case property'] == cases_list[0]['property_setting']:
        case_data = YamlHandle().load(cases_list[i]['case name'])
        cases_data.extend(case_data)


@ddt
class TestExecute(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed, can't execute test cases!"

    # @data(*cases_data)
    # @unpack
    def test_cases(self, ):
        for j in range(len(cases_data)):
            print('---------------------Start Case: ' + str(cases_data[j]['case_name']) + '---------------------')
            case_to_menu(saas_driver, change_menu_data, cases_data[j]['case_name'])
            case_exe = case_common(saas_driver, cases_data[j]['case_data'])
            assert case_exe, 'Case execute failed!'

    @classmethod
    def tearDownClass(cls) -> None:
        saas_driver.quit()
