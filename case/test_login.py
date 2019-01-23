import unittest
from globals.dirver import Driver
from loginPage import LoginPage
import xlrd
from time import sleep


loginPage = LoginPage()
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #登陆系统
        pass

    @classmethod
    def tearDownClass(cls):
        Driver.driver.close()


    def test_login(self):

        # 从excel文件中读取数据
        workbook = xlrd.open_workbook(r'C:\dandan\login.xlsx')
        sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
        # 获取sheet1的第一行的第一个单元格的内容
        username1 = int(sheet1.row(1)[0].value)
        password1 = int(sheet1.row(1)[1].value)
        loginPage.login(username1,password1)

        sleep(3)
        #成功登陆后获取页面的“所有”元素
        title=Driver.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/span")
        # 断言测试结果
        self.assertEqual(title.text, "所有")

if __name__=="__main__":
    unittest.main()