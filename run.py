import os
import unittest

from util.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    report_title = '用例执行报告 我的标题'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './result.html'
    # test_dir 一定要注意创建的运行目录，不能
    test_dir = './testcase'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)