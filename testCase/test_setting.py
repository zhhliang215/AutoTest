# -*- coding:utf-8 -*-
import uiautomator2 as u2
# import time, subprocess, os
import unittest, time


class Setting(unittest.TestCase):
    def setUp(self):
        try:
            driver = u2.connect_usb('CSXDU17612012791')
        except Exception as e:
            print(e)
        # 全局设置,每个ui点击之后休眠1.5s
        driver.click_post_delay = 5

        self.driver = driver
        self.driver.app_start("com.ichinait.gbdriver")

        setting = driver(text="设置")
        wait_order_list_des = driver(text="待服务行程")

        # 如下操作可以使setUp中的变量被其他模块调用
        self.setting = setting
        self.wait_order_list_des = wait_order_list_des


    def tearDown(self):
        self.driver.app_clear("com.ichinait.gbdriver")
        # self.driver.quit()

    # 成功登录
    def test_setting(self):
        print("-----test start -----")


        # t通过新窗口的title验证用例是否通过
        # self.assertEqual(self.driver.title, "网易邮箱6.0版", "登录失败")

    #     # t通过新窗口的title验证用例是否通过
    #     self.assertEqual(self.driver.title, "网易帐号中心 > 用户验证", "未跳转至用户验证界面")
