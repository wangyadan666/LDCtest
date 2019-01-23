from globals.dirver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


username_locator=(By.XPATH,"/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/input")
password_locator=(By.XPATH,"/html/body/div[1]/div/div/main/div/div[2]/div[3]/div/div[2]/input")
class LoginPage:
    def __init__(self):
        Driver.driver.get("http://139.159.231.200/m/")
        #设置等待
        wait=WebDriverWait(Driver.driver, 5, 0.5)
        wait.until(EC.visibility_of_element_located(username_locator))
        self.username_webelement=Driver.driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/input")
        self.password_webelement=Driver.driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[3]/div/div[2]/input")
        self.login_webelement=Driver.driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[3]/button[1]")

    def login(self,username,password):
        self.username_webelement.send_keys(username)
        self.password_webelement.send_keys(password)
        self.login_webelement.click()

