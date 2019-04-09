from selenium import webdriver
import unittest, time


class Login(unittest.TestCase):
    def setUp(self):
        # 打开百度，搜索“163网易邮箱”，登录
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        self.driver = driver
        driver.get("https://www.baidu.com/")

        driver.find_element_by_id("kw").send_keys("163邮箱登录")
        driver.find_element_by_id("su").click()

        name = driver.find_element_by_id("op_email3_username")
        password = driver.find_element_by_class_name("op_email3_password")
        login = driver.find_element_by_css_selector(".c-btn")

        # 如下操作可以使setUp中的变量被其他模块调用
        self.name = name
        self.password = password
        self.login = login

    def tearDown(self):
        self.driver.quit()

    def switch_window(self):
        # 切换窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            # j增加等待时间，可以提高测试用例执行的健壮性
            time.sleep(2)
        time.sleep(3)

    # 成功登录
    def test_right_login(self):
        # 账号密码自行填写
        self.name.send_keys("xxx")
        self.password.send_keys("xxx")
        self.login.click()

        self.switch_window()
        # t通过新窗口的title验证用例是否通过
        self.assertEqual(self.driver.title, "网易邮箱6.0版", "登录失败")

    # 密码为空登录
    def test_null_psw_login(self):
        self.name.send_keys("xxx")
        time.sleep(3)
        self.login.click()
        self.switch_window()
        # t通过新窗口的title验证用例是否通过
        self.assertEqual(self.driver.title, "网易帐号中心 > 用户验证", "未跳转至用户验证界面")
