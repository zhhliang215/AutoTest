import uiautomator2 as u2
import time, subprocess, os
import uiautomator2.ext.htmlreport as htmlreport


class Driver(object):
    def __init__(self):
        try:
            self.d = u2.connect_usb('CSXDU17612012791')
        except Exception as e:
            print(e)
        # 全局设置,每个ui点击之后休眠1.5s
        self.d.click_post_delay = 5
        hrp = htmlreport.HTMLReport(self.d)
        hrp.patch_click()

    # 连接测试
    def link_test(self):
        if self.d.info['naturalOrientation'] == True:
            print('设备连接正常!')
            self.run_app()
        else:
            print('设备连接出现问题!请检查后重试!')

    # 运行app
    def run_app(self):
        # 先返回主菜单界面
        self.d.press('home')
        self.d(text="首约司机").click()
        self.login_app()
        time.sleep(2)
    # 登录app
    def login_app(self):
        self.d(resourceId="com.ichinait.gbdriver:id/et_user_name").set_text('17610375730')
        self.d(resourceId="com.ichinait.gbdriver:id/et_user_pwd").set_text('123456')
        try:
            self.d(text='登 录').click()
        except Exception as e:
            print(e)
        else:
            print('正在登录>>>>>>\n请稍后>>>>>>')

    def test_setting(self):
        self.d(resourceId='com.ichinait.gbdriver:id/tv_setting').click()

    def init_report(self):
        cmd = "allure generate --clean data -o reports"
        subprocess.call(cmd, shell=True)
        project_path = os.path.abspath(os.path.dirname(__file__))
        # report_path = project_path + "/reports/" + "index.html"
        # # logger.info("报告地址:{}".format(report_path))


if __name__ == '__main__':
    driver = Driver()
    driver.link_test()
    driver.init_report()
