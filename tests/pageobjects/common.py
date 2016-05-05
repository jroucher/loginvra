# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

import time, string, random

class CommonPageObject(PageObject):
    def open(self, sectionName = None):
        """ Open app url in browser
        :returns: this page object instance
        """
        url = self.config.get('Common', 'url')
        self.driver.get(url)
        return self

    def waitToDrawSection(self):
        self.utils.wait_until_element_visible(self.getContentSection().locator);
        return self

# ##############################################
#    def wait_for_page_load(self, timeout=30):
#        old_page = self.browser.find_element_by_tag_name('html')
#        yield
#        WebDriverWait(self.browser, timeout).until(
#            staleness_of(old_page)
#        )
# ##############################################
#
#    def setLanguage(self, id):
#        idMap = {
#            'es': 'LiteralSpanish',
#            'en': 'LiteralEnglish',
#            'pt': 'LiteralBrazilian'
#        }
#        # open select
#        self.driver.find_element_by_xpath('//div[@id="language-header"]//div[@data-toggle="dropdown"]').click()
#        # click on button
#        Button(By.ID, idMap.get(id, '')).click()
#        return self
# ##############################################

    def getConfig(self, section):
        config = {}
        options = self.config.options(section)
        for option in options:
            try:
                config[option] = self.config.get(section, option)
            except:
                config[option] = None
        return config


    def hasElement(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def getMessage(self):
        messageElement = Text(By.XPATH, "//div[contains(@class,'alert-warning')]/p");
        return messageElement.wait_until_visible(20).text;

    def getContentSection(self):
            return PageElement(By.ID, "SHELL_GREETING");

    def getApp(self):
            return PageElement(By.ID, "application");

    def getMainMenu(self):
        return PageElement(By.XPATH, "//div[@class='sidebar']//div[@class='nav-sidebar']");

    def getHeaderSection(self):
        return PageElement(By.XPATH, "//div[@class='topbar']");

    def getPageSection(self):
        return PageElement(By.XPATH, "//div[@class='page-content']");
