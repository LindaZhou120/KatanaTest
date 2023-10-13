import pytest
from pages.loginpage import _login

"""
case/conftest.py文件
登录功能调用
"""


@pytest.fixture(scope='session')
def login(driver, host):
    """登录功能fixture"""
    _login(driver, host)