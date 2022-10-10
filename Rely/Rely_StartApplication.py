import time

from appium import webdriver as app
from selenium import webdriver as web
import os


def start_app():
    server = 'http://localhost:4723/wd/hub'
    cr = os.path.abspath('..')
    app_path = cr + "\Dependencies\BeyondTrucks_Stage_v1.1.0.apk"
    # Galaxy s20
    # desired_caps = {
    #     "platformName": "Android",
    #     "deviceName": "RFCN201D4YX",
    #     "appPackage": "com.haulistix.driver",
    #     "appActivity": "com.haulistix.driver.module.splash.SplashActivity",
    #     "noSign": "True",
    #     "noReset": "True"
    # }

    # Pixel 4a
    # desired_caps = {
    #     "platformName": "Android",
    #     "deviceName": "0B171JEC209758",
    #     "appPackage": "com.haulistix.driver.exam",
    #     "appActivity": "com.haulistix.driver.android.module.splash.SplashActivity",
    #     "noSign": "True",
    #     "noReset": "True"
    # }

    #
    desired_caps = {
        "platformName": "Android",
        "devicesName": "127.0.0.1:62001",
        "automationName": "uiautomator2",
        "app": app_path,
        "noSign": "True",
        "noReset": "True"
    }
    driver = app.Remote(server, desired_caps)
    driver.implicitly_wait(10)
    return driver


def start_saas():
    url = 'https://console-test.beyondtrucks.com/'
    # 不关闭浏览器；窗口最大化；页面响应超时时间：90s
    option = web.ChromeOptions()
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)
    # option.add_argument('--headless')
    driver = web.Chrome(chrome_options=option)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(5)
    return driver


if __name__ == '__main__':
    start_saas()
