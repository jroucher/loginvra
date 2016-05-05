# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from tests.pageobjects.common import CommonPageObject
from toolium.pageelements import *

class LoginPageObject(CommonPageObject):
    def init_page_elements(self):
        return self;

    def setElements(self):
        self.username = InputText(By.NAME, 'username');
        self.password = InputText(By.NAME, 'password');
        self.loginBtn = Button(By.ID, 'btnLogin');
        self.portal = Button(By.ID, 'rbPortal');
        self.vra = Button (By.XPATH, '//*[@id="rbPortal"]/option[1]')
        self.vcd = Button (By.XPATH, '//*[@id="rbPortal"]/option[2]')
        return self;

    def waitToDrawSection(self):
        self.utils.wait_until_element_visible(PageElement(By.ID, "frmLogin").locator)
        return self

    def getUserName(self):
        return Text(By.ID, "SHELL_GREETING")

    def resetForm(self):
        self.username.clear();
        self.password.clear();
        return self;
