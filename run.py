import os


def runcase(name="chrome", case_path=""):
    """执行CMD命令"""
    os.system("pytest -s --browser=%s %s" % (name, case_path))


if __name__ == '__main__':
    runcase(name="chrome", case_path="case/test_login.py")
