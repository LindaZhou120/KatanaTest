from selenium import webdriver
from common.base import Base
import time
"""
page/login_page.py文件
"""
# url = 'https://staging.via.market/staff/login'
# host = 'staging'
# url = 'https://' + host +'.via.market/staff/login'
# -------定位元素信息--------#
loc1 = ('id', ':r0:')
loc2 = ('id', ':r1:')
loc3 = ('id', ':r2:')
result_loc = ('xpath', '//*[@id="__next"]/div[2]/div/div[1]/div/span') # login then display the store name


def _login(driver, host, user="8332691066", psw="0000"):
    '''
    登录函数
    '''
    zen = Base(driver)
    driver.get('https://' + host +'.via.market/staff/login')
    zen.sendkeys(loc1, user)
    zen.sendkeys(loc2, psw)
    zen.click(loc3)
    time.sleep(2)


def _login_result(driver, _text):
    '''
    login then display the store name
    :param driver:
    :param _text: 用户名
    :return: True or False
    '''
    zen = Base(driver)
    r = zen.is_text_in_element(result_loc, _text)
    return r


def _get_alert(driver):
    '''判断alert在不在,存在返回text文本内容，不存在返回空字符'''
    zen = Base(driver)
    try:
        alert = zen.is_alert()
        text = alert.text
        alert.accept()  # 点alert确定
        return text
    except:
        return ""


if __name__ == "__main__":
    driver = webdriver.Chrome()
    _login(driver, "staging")
