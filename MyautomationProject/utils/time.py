import time
import datetime
from functools import wraps
def timestamp ():
    """返回当前时间的时间戳。"""
    return time.time()
def dt_strftime(fmt="%Y%m"):
    """
    返回格式化的日期的字符串。
    :param fmt:格式化字符串
    :return:
     """
    return datetime.datetime.now().strftime(fmt)
def sleep(seconds=3.0):
        time.sleep(seconds)
def running_time(func):
    """装饰器，用语测量函数的运行时间。
    ：param fuc:要测量运行时间的函数
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = timestamp()
        res = func(*args,**kwargs)
        print(f"校验元素完成！用时{timestamp() - start:.3f}秒！")
        return res
    return wrapper
if __name__ == "__main__":
    print(dt_strftime("%Y%m%d%H%M%S"))