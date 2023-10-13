import pytest
import time


def test_blog(driver):
    driver.get('https://blog.csdn.net/Au624605062?spm=1011.2124.3001.5343')
    time.sleep(3)
    t = driver.title
    print('测试结果：%s' % t)
    assert 'Au624605062' in t, '失败原因，打开博客失败'


if __name__ == '__main__':
    pytest.main(['-v', 'test_01.py'])
