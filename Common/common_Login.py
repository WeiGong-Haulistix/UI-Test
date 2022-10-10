from selenium import webdriver
from Rely.Rely_Element import *
from Rely.Rely_ExecuteMethod import execute_method


def login_by(driver, login_data):
    if login_data[0]['button'] == "login sign":
        login = check_element(driver, login_data[0]['by'], login_data[0]['value'])
    else:
        login = True
    if login is True:
        result = execute_method(driver, login_data)
        if result is False:
            print('Login Failed!')
        else:
            print('Login success!')
            return True
    else:
        print("Already login success!")
        return True
