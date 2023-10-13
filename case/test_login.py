from selenium import webdriver
from common.base import Base
import pytest

# ----------------测试数据-------------#
test_login_data = [('8332691066', '0000', 'Staging env for Ky'), ('2345678902', '0000', 'test xxx')]
# -------------定位元素------------------#
loc1 = ('id', ':r0:')
loc2 = ('id', ':r1:')
loc3 = ('id', ':r2:')
login_user = ('xpath', '//*[@id="__next"]/div[2]/div/div[1]/div/span')  # 登录后的用户名
driver = webdriver.Chrome()
zen = Base(driver)
url = 'https://staging.via.market/staff/login'


def setup_function():
    driver.get(url)


def teardown_function():
    '''数据清理'''
    print('清空cookies,退出登录状态')
    driver.delete_all_cookies()
    driver.refresh()


def teardown_module():
    '''用例执行完后退出'''
    print('teardown_module：用例执行完成关闭浏览器')
    driver.quit()


def login(user='admin', psw='123456'):
    '''普通登录函数'''
    zen.sendkeys(loc1, user)
    zen.sendkeys(loc2, psw)
    zen.click(loc3)


@pytest.mark.parametrize('user,psw,expect', test_login_data)
def test_login(user, psw, expect):
    '''登录用例'''
    login(user, psw)
    result = zen.get_text(login_user)
    print('登录结果，获取到用户名：%s' % result)
    assert result == expect


if __name__ == '__main__':
    pytest.main(['-v', 'test_login.py'])