# -*- coding:utf-8 -*-
import uiautomator2 as u2
# import time, subprocess, os
import unittest, time


class Login(unittest.TestCase):
    def setUp(self):
        try:
            driver = u2.connect_usb('CSXDU17612012791')
        except Exception as e:
            print(e)
        # 全局设置,每个ui点击之后休眠1.5s
        driver.click_post_delay = 5

        # driver.implicitly_wait(5)
        self.driver = driver
        self.driver.app_start("com.ichinait.gbdriver")

        name = driver(resourceId="com.ichinait.gbdriver:id/tv_mobile")
        password = driver(resourceId="com.ichinait.gbdriver:id/tv_pwd")
        login = driver(text='登录')

        # 如下操作可以使setUp中的变量被其他模块调用
        self.name = name
        self.password = password
        self.login = login

    def tearDown(self):
        self.driver.app_clear("com.ichinait.gbdriver")
        # self.driver.quit()

    # 成功登录
    def test_login(self):
        print("-----test start -----")
        test = self.driver(text="获取短信验证码")
        if test.exists:
            print("----- 2 -----")
            self.driver(resourceId="com.ichinait.gbdriver:id/tv_mobile").send_keys("17610375730")
            time.sleep(3)
            self.driver(text="获取短信验证码").click()
        print("----- 3 -----")
        self.driver(text="收不到验证码，密码登录").click()
        # 账号密码自行填写
        self.name.send_keys("17610375730")
        time.sleep(3)
        self.password.send_keys("123456")
        time.sleep(3)
        self.driver.press("back")
        time.sleep(3)
        self.login.click()

        self.switch_window()
        # t通过新窗口的title验证用例是否通过
        # self.assertEqual(self.driver.title, "网易邮箱6.0版", "登录失败")

    # 密码为空登录
    # def test_null_psw_login(self):
    #     self.name.send_keys("xxx")
    #     time.sleep(3)
    #     self.login.click()
    #     self.switch_window()
    #     # t通过新窗口的title验证用例是否通过
    #     self.assertEqual(self.driver.title, "网易帐号中心 > 用户验证", "未跳转至用户验证界面")
