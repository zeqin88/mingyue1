import logging
import os
from logging.handlers import RotatingFileHandler

# 确保日志目录存在
log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# 设置日志
logger = logging.getLogger('TestLogger')
logger.setLevel(logging.DEBUG)

# 创建文件处理器
log_file_path = os.path.join(log_directory, 'test.log')
handler = RotatingFileHandler(log_file_path, maxBytes=10000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 添加处理器到日志
logger.addHandler(handler)

# 定义日志记录方法
def debug(msg):
    logger.debug(msg)

def info(msg):
    logger.info(msg)

def warning(msg):
    logger.warning(msg)

def error(msg):
    logger.error(msg)

def critical(msg):
    logger.critical(msg)

# 测试日志记录
if __name__ == "__main__":
    debug('This is a debug message')
    info('This is an info message')
    error('This is an error message')