# test_search_page.py
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from conftest import search_page


class TestSearchPageFunctions:
    def test_search_function(self, search_page):
        # 打开百度首页
        search_page.get_url('https://www.baidu.com')

        # 输入搜索词 "Selenium"
        search_page.input_search("Selenium")

        # 点击搜索按钮
        search_page.click_search_button()

        # 显式等待直到页面上的搜索建议元素加载完成
        try:
            WebDriverWait(search_page.driver, 15).until(
                ec.presence_of_all_elements_located((By.CSS_SELECTOR, "#content_left"))
            )
        except TimeoutException:
            print("Timeout waiting for search suggestions to load")
            assert False  # 如果超时，断言测试失败

        # 验证搜索建议中是否包含 "Selenium"
        suggestions = search_page.get_search_suggestions()
        assert "Selenium" in suggestions, "Expected to find 'Selenium' in search suggestions"
