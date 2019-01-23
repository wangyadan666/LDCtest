import HTMLTestRunner
import unittest
import os


# 用例路径
case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report.html")

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())

    # html报告文件路径
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()