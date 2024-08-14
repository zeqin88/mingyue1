import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from page_object.search_page import SearchPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = WebDriver(options=options)  # 确保 driver 在 yield 之前被创建
    yield driver
    driver.quit()  # 清理工作放在 yield 之后


@pytest.fixture(scope="function")
def search_page(driver):
    page = SearchPage(driver)
    page.get_url('http://www.baidu.com')
    yield page
    page.close()  # 确保 SearchPage 类中有 close 方法
