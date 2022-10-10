import time
from selenium.webdriver.common.action_chains import ActionChains

from Rely.Rely_database import DoMysql


def is_element_exist(driver, by, value):
    s = driver.find_elements(by, value)
    if len(s) == 0:
        return False
    elif len(s) == 1:
        return True
    else:
        print("Result**** Existing" + str(len(s)) + "elements!")
        return True


def find_element_re(driver, by, value, times=20):
    print("Finding***** Trying to find keys: " + value)
    for i in range(times):
        if is_element_exist(driver, by, value):
            print("Result**** Found Element: " + value)
            return True
        else:
            continue


def move_to(driver, by, value):
    move = driver.find_element(by, value)
    ActionChains(driver).move_to_element(move).perform()


def check_and_click(driver, by, value):
    if find_element_re(driver, by, value):
        print("Operation**** Click element: " + str(value))
        time.sleep(1)
        driver.find_element(by, value).click()
        return True
    else:
        return False


def check_and_click_one(driver, by, value, number):
    number = int(number)
    if find_element_re(driver, by, value):
        print("Operation**** Click element: " + str(value))
        time.sleep(0.5)
        driver.find_elements(by, value)[number].click()
        return True
    else:
        return False


def scroll_to_click(driver, by, value):
    if find_element_re(driver, by, value):
        print("Operation**** Click element: " + str(value))
        driver.execute_script("window.scrollBy(0, 500)")
        time.sleep(1)
        driver.find_element(by, value).click()
        time.sleep(1)
        return True
    else:
        return False


def check_and_input(driver, by, value, keys):
    if find_element_re(driver, by, value):
        print("Operation**** Input data for element: " + str(value) + "***" + str(keys))
        driver.find_element(by, value).send_keys(keys)
        time.sleep(1)
        return True
    else:
        return False


def check_and_clear(driver, by, value):
    if find_element_re(driver, by, value):
        print("Operation**** Clear element: " + str(value))
        time.sleep(1)
        driver.find_element(by, value).clear()
        time.sleep(0.5)
        return True
    else:
        return False


def check_element(driver, by, value):
    for i in range(0, 10):
        if find_element_re(driver, by, value):
            print("Operation**** Check element: " + str(value))
            time.sleep(1)
            return True
        else:
            continue


def check_element_value(driver, by, value, attr, text):
    result = get_element_value(driver, by, value, attr)
    if str(result) == str(text):
        return True
    else:
        return False


def find_element_retry(driver, by, value, operate, times=100):
    for i in range(0, times):
        if find_element_re(driver, by, value):
            check_and_click(driver, by, value)
            print(("Operation**** Find element " + value + "for " + str(times) + "times"))
            return True
        else:
            check_and_click(driver, by, operate)
            print('Operation**** Find element retries: ' + str(operate) + '***' + str(i+1))
            continue


def get_element_value(driver, by, value, attribute):
    print("Finding**** Find element: " + str(value))
    if find_element_re(driver, by, value):
        attr = driver.find_element(by, value).get_attribute(attribute)
        print("Result**** Find element " + str(value) + ", and find attribute: " + str(attr))
        time.sleep(1)
        return attr
    else:
        print("Result**** Can not find element: " + str(value))
        return False


def get_element_text(driver, by, value):
    if find_element_re(driver, by, value):
        print("Finding**** Find element text: " + str(value))
        attr = driver.find_element(by, value).get_attribute("textContent")
        print("Result**** Element attribute: textContent")
        time.sleep(1)
        return attr
    else:
        return False


def get_elements_number(driver, by, value):
    if find_element_re(driver, by, value):
        print("Finding**** Find elements: " + str(value))
        number = driver.find_elements(by, value)
        print("Result**** Element number: " + str(len(number)))
        time.sleep(1)
        return len(number)
    else:
        return False


def scroll_screen(driver, t):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x * 0.5)  # x坐标
    y1 = int(y * 0.75)  # 起始y坐标
    y2 = int(y * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


def scroll_find_element(driver, by, value):
    for i in range(0, 1000):
        element = find_element_re(driver, by, value)
        if element is False:
            scroll_screen(driver, 1000)
            continue
        else:
            return True


def scroll_click_apps(driver, by, value):
    for i in range(0, 1000):
        element = find_element_re(driver, by, value)
        if element is False:
            scroll_screen(driver, 1000)
            continue
        else:
            check_and_click(driver, by, value)
            return True


def execute_unit(driver, unit_data):
    by = unit_data['by']
    value = unit_data['value']
    remark = unit_data['remark']
    print("steps========" + unit_data['cases'] + ": " + unit_data['button'])

    # exit_bullet(driver)
    if unit_data['execute'] == "input":
        check_and_input(driver, by, value, remark)
    elif unit_data['execute'] == "click":
        check_and_click(driver, by, value)
    elif unit_data['execute'] == "click one":
        check_and_click_one(driver, by, value, remark)
    elif unit_data['execute'] == "move-click":
        scroll_to_click(driver, by, value)
    elif unit_data['execute'] == "scroll-click":
        scroll_click_apps(driver, by, value)
    elif unit_data['execute'] == 'clear':
        check_and_clear(driver, by, value)
    elif unit_data['execute'] == "check":
        check = check_element(driver, by, value)
        if check is not True:
            return False
    elif unit_data['execute'] == 'scroll':
        scroll_find_element(driver, by, value)
    elif unit_data['execute'] == 'count':
        num = get_elements_number(driver, by, value)
        if str(num) == str(remark):
            return True
        else:
            print('Check elements number not correct: ' + value + '**' + str(num) + '**' + str(remark))
            return False
    elif unit_data['execute'] == "check result":
        res = get_element_text(driver, by, value)
        if res == remark:
            return True
        else:
            print('Check xpath attribute failed: ' + str(value) + '**' + str(res) + '**' + str(remark))
            return False
    elif unit_data['execute'] == "value":
        res = check_element_value(driver, by, value, 'value', remark)
        if res is False:
            return False
    # 执行sql
    elif unit_data['execute'] == "execute sql":
        res = DoMysql().execute_sql_string(value)
        DoMysql().close_connect()
        print('bool(res):', bool(res))
        if res:
            print('execute_sql_succeeded: ' + str(value))
            return True
        else:
            print('execute_sql_failed: ' + str(value))
            return False


def execute_method(driver, execute_data):
    for i in range(0, len(execute_data)):
        result = execute_unit(driver, execute_data[i])
        # print(execute_data[i], ':', bool(result))
        if result is True:
            print("Case Done: " + str(execute_data[i]['cases']))
            return True
        elif result is False:
            print("Case Failed: " + str(execute_data[i]['cases']))
            return False
        else:
            continue
