from Rely.Rely_Element import *
from Rely.Rely_AnalysisCases import *
from Rely.Rely_AnalysisCases_FromYaml import *


def change_href(driver, href):
    href_data = GetTestCase().get_href()
    if href in ("dispatch center", "load board"):
        check_and_click(driver, 'xpath', href_data["dispatch"])
    elif href in ("POD", "accessorials"):
        check_and_click(driver, 'xpath', href_data["accounting"])
        check_and_click(driver, 'xpath', href_data["pre-accounting"])
    elif href in ("load", "invoice", "factored"):
        check_and_click(driver, 'xpath', href_data["accounting"])
        check_and_click(driver, 'xpath', href_data["account receivable"])
    elif href in ("load", "invoice", "factored"):
        check_and_click(driver, 'xpath', href_data["accounting"])
        check_and_click(driver, 'xpath', href_data["account payable"])
    elif href == "financial reports":
        check_and_click(driver, 'xpath', href_data["reports"])
    elif href in ("drivers", "dispatcher&management", "groups"):
        check_and_click(driver, 'xpath', href_data["setup"])
        check_and_click(driver, 'xpath', href_data["users&groups"])
    elif href in ("tractor", "trailer"):
        check_and_click(driver, 'xpath', href_data["setup"])
        check_and_click(driver, 'xpath', href_data["equipment"])
    elif href in ("customer", "contract", "vendor"):
        check_and_click(driver, 'xpath', href_data["setup"])
        check_and_click(driver, 'xpath', href_data["relations"])
    elif href in ("company info", "setting-accounting", "integration", "factoring"):
        check_and_click(driver, 'xpath', href_data["setup"])
        check_and_click(driver, 'xpath', href_data["settings"])

    check_and_click(driver, 'xpath', href_data[href])


def change_title(driver, title):
    print('*************Change title: ' + str(title) + '*****************')
    title_data = GetTestCase().get_title()
    button = title_data[0]
    by = title_data[1]
    value = title_data[2]
    if title in ["upcoming", "in progress", "canceled"]:
        print(by[2], value[2])
        check_and_click(driver, by[2], value[2])

    for i in range(0, len(button)):
        if title == button[i]:
            check_and_click(driver, by[i], value[i])


def case_to_menu(driver, menu_data, case_name):
    for i in range(0, len(menu_data)):
        if menu_data[i]['case name'] == str(case_name):
            change_href(driver, menu_data[i]['title name'])
        else:
            continue


def case_common(driver, test_data):
    case_re = execute_method(driver, test_data)
    if case_re is True:
        return True
    else:
        print('Testcase false!')
        return False
