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

        home = driver(text="首页")
        guess_like = driver(text="推荐")
        guess_like_page = driver(text='常见问题')
        news = driver(text="消息")
        news_id = 'com.ichinait.gbdriver:id/right_imageView'
        mine = driver(text="个人中心")
        mine_id = 'com.ichinait.gbdriver:id/rl_user_center'
        setting = driver(text="设置")
        wait_order_list_des = driver(text="待服务行程")

        # 如下操作可以使setUp中的变量被其他模块调用
        self.home = home
        self.guess_like = guess_like
        self.guess_like_page = guess_like_page
        self.news = news
        self.news_id = news_id
        self.mine = mine
        self.mine_id = mine_id
        self.setting = setting
        self.wait_order_list_des = wait_order_list_des

    def tearDown(self):
        self.driver.app_clear("com.ichinait.gbdriver")
        # self.driver.quit()

    # 切换推荐页
    def test_guess_like(self):
        print("-----test start -----")
        self.guess_like.click()
        assert self.guess_like_page.exists()
        print("----- test end -----")

    # 切回首页
    def test_home(self):
        self.home.click()
        assert self.wait_order_list_des.exists()
