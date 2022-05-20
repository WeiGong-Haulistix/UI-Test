from Common.common_Login import login_by
from Rely.Rely_ExecuteMethod import change_href
from Rely.Rely_ExecuteMethod import case_common
from Rely.Rely_ExecuteMethod import case_to_menu
from Rely.Rely_StartApplication import start_saas
from Rely.Rely_AnalysisCases import GetTestCase
import unittest


# Get cases from excel
cases = GetTestCase()
all_data = cases.get_all_data()
saas_login = cases.get_data('login', 'saas login')
href_data = cases.get_href()
change_menu_data = cases.get_change_menu()

saas_driver = start_saas()


class TestExecute(unittest.TestCase):

    def test_case(self):
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed, can't execute test cases!"

        modules_name = list(all_data.keys())
        for module_name in modules_name:
            modules_data = all_data[module_name]
            for module_data in modules_data:
                cases_name = list(module_data.keys())
                for case_name in cases_name:
                    case_data = module_data[case_name]
                    print('***********' + case_name + '***********')
                    case_to_menu(saas_driver, change_menu_data, case_name)
                    case_exe = case_common(saas_driver, case_data)
                    assert case_exe, 'Case execute failed!'

        saas_driver.quit()
