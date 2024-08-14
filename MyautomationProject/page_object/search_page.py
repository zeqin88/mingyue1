from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_by_id(self, id_):
        return self.driver.find_element(By.ID, id_)

    def find_elements_by_css_selector(self, css_selector):
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector)


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self, url):
        self.driver.get(url)

    def input_search(self, text):
        search_box = self.find_element_by_id('kw')  # 确保 'kw' 是搜索框的实际 ID
        search_box.send_keys(text)

    def click_search_button(self):
        search_button = self.find_element_by_id('su')  # 确保 'su' 是搜索按钮的实际 ID
        search_button.click()

    def get_search_suggestions(self):
        try:
            suggestions_elements = self.find_elements_by_css_selector('#content_left h3')
            return [suggestion.text for suggestion in suggestions_elements]
        except NoSuchElementException:
            return []

    def close(self):
        """关闭浏览器窗口"""
        self.driver.close()

# 其他方法定义可以继续添加到 BasePage 或 SearchPage 类中
