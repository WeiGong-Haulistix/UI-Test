from Common.common_Login import login_by
from Rely.Rely_ExecuteMethod import change_href
from Rely.Rely_ExecuteMethod import *
from Rely.Rely_ExecuteMethod import case_to_menu
from Rely.Rely_StartApplication import start_saas
from Rely.Rely_AnalysisCases import GetTestCase
from Rely.Rely_AnalysisCases_FromYaml import YamlHandle
import unittest
from ddt import ddt, data, unpack

# Get cases from excel
cases = GetTestCase()
cases_data = YamlHandle().return_case_data()
saas_login = cases.get_data('login', 'saas login')
href_data = cases.get_href()
change_menu_data = YamlHandle().get_change_menu()

saas_driver = start_saas()


@ddt
class TestExecute(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed, can't execute test cases!"

    @data(*cases_data)
    @unpack
    def test_cases(self, case_name, case_data):
        print('---------------------Start Case: ' + str(case_name) + '---------------------')
        case_to_menu(saas_driver, change_menu_data, case_name)
        case_exe = case_common(saas_driver, case_data)
        if DoMysql().close_connect() is True: DoMysql().close_connect()
        assert case_exe, 'Case execute failed!'

    @classmethod
    def tearDownClass(cls) -> None:
        saas_driver.quit()
