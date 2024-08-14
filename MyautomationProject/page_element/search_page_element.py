from selenium.webdriver.common.by import By
from MyautomationProject.page_element.locators import SEARCH_BOX_ID, SEARCH_BUTTON_ID, SEARCH_SUGGESTIONS_CSS


class SearchPageElement:
    SEARCH_BOX = (By.ID, SEARCH_BOX_ID)
    SEARCH_BUTTON = (By.ID, SEARCH_BUTTON_ID)
    SEARCH_SUGGESTIONS = (By.CSS_SELECTOR, SEARCH_SUGGESTIONS_CSS)
    # 其他元素定义...
