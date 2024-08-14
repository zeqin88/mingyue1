import os
from selenium.webdriver.common.by import By
from utils.time import dt_strftime


class ConfigManager(object):
    """
    配置管理类，用于集中管理项目中的配置信息。
    """

    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR,
                                'page_element')
    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR,
                               'report.html')
    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }
    # 邮件信息
    EMAIL_INFO = {
        'username': '1418779364@qq.com',
        'password': '200088zq.',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465,
    }
    # 收件人
    ADDRESSEE = ['1418779364@qq.com']

    @property
    def log_file(self):
        """
        日志文件路径
        """
        log_dir = os.path.join(self.BASE_DIR,
                               'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir,
                            '{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        """
        配置文件路径
        """
        ini_file = os.path.join(self.BASE_DIR,
                                'config',
                                'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file


if __name__ == '__main__':
    # 创建配置管理实例
    cm = ConfigManager()
    # 打印项目基础目录，用于验证路径是否正确
    print(cm.BASE_DIR)
