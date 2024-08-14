from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page_element.locators import SEARCH_BOX_ID, SEARCH_BUTTON_ID, SEARCH_SUGGESTIONS_CSS


class BasePage:
    """基础页面类，包含WebDriver实例和基础页面操作方法。"""

    def __init__(self, driver: WebDriver):
        """初始化WebDriver实例。"""
        self.driver = driver

    def find_element_by_id(self, id_):
        """通过ID查找元素。"""
        return self.driver.find_element(By.ID, id_)

    def find_elements_by_css_selector(self, css_selector):
        """通过CSS选择器查找所有匹配的元素。"""
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector)

    def get(self, url):
        """http://www.baidu.com"""
        self.driver.get(url)

    def close(self):
        """关闭浏览器窗口"""
        self.driver.close()


class SearchPage(BasePage):
    """搜索页面类，继承自BasePage，包含搜索页面特有的操作方法。"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def input_search(self, text):
        """在搜索框中输入文本。"""
        search_box = self.find_element_by_id(SEARCH_BOX_ID)  # 使用定位器常量
        search_box.send_keys(text)

    def click_search_button(self):
        """点击搜索按钮。"""
        search_button = self.find_element_by_id(SEARCH_BUTTON_ID)
        search_button.click()

    def get_search_suggestions(self):
        """获取搜索建议。"""
        suggestions_elements = self.find_elements_by_css_selector(SEARCH_SUGGESTIONS_CSS)
        return [suggestion.text for suggestion in suggestions_elements if suggestion.text]
