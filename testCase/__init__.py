import uiautomator2 as u2
import time, subprocess, os


# class Driver(object):
#     def __init__(self):
#         try:
#             self.d = u2.connect_usb('CSXDU17612012791')
#         except Exception as e:
#             print(e)
#         # 全局设置,每个ui点击之后休眠1.5s
#         self.d.click_post_delay = 5
#
#     # 连接测试
#     def link_test(self):
#         if self.d.info['naturalOrientation'] == True:
#             print('设备连接正常!')
#             self.run_app()
#         else:
#             print('设备连接出现问题!请检查后重试!')
#
#     # 运行app
#     def run_app(self):
#         # 先返回主菜单界面
#         self.d.press('home')
#         self.d(text="首约司机").click()
#         self.login_app()
#         time.sleep(2)
