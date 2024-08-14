# readconfig.py
import configparser
import os


class ReadConfig:
    def __init__(self):
        # 定义配置文件的路径
        self.config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
        # 创建配置解析器
        self.config = configparser.ConfigParser()
        # 读取配置文件
        self.config.read(self.config_path)

    def get_config(self, section, option):
        # 尝试获取配置项的值
        try:
            value = self.config.get(section, option)
            print(f"The value for '{option}' in section '{section}' is: {value}")
            return value
        except configparser.NoSectionError:
            print(f"Error: The section '{section}' does not exist in the config file.")
        except configparser.NoOptionError:
            print(f"Error: The option '{option}' does not exist in the section '{section}'.")

# 脚本的主入口点


if __name__ == "__main__":
    # 创建ReadConfig实例
    config_reader = ReadConfig()
    # 调用实例方法，传入section名称和option名称
    host_url = config_reader.get_config('HOST', 'HOST')
    print(f"Host URL is: {host_url}")
