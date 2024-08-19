# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SurveyCreateEmpatick(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_survey_create_empatick(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1680,929 | ]]
        driver.get("https://portal.dev.empatick.com/dashboard")
        driver.find_element_by_xpath("//*[text() = \"Surveys\"]").click()
        driver.find_element_by_xpath("//*[text() = \"Create New Survey\"]").click()
        driver.find_element_by_xpath("//*[text() = \"Run Preview\"]").click()
        driver.find_element_by_xpath("//*[text() = \"Proceed with this template\"]").click()
        driver.find_element_by_xpath("//input[@placeholder = \"Enter Survey Name\"]").click()
        driver.find_element_by_xpath("//input[@placeholder = \"Enter Survey Name\"]").clear()
        driver.find_element_by_xpath("//input[@placeholder = \"Enter Survey Name\"]").send_keys("Survey create for blazemeter 2")
        driver.find_element_by_xpath("//*[text() = \"Add Unit\"]").click()
        driver.find_element_by_xpath("//*[text() = \"Add Unit\"]").click()
        driver.find_element_by_xpath("//*[contains(text(), \"Kauno grudai\")]").click()
        driver.find_element_by_css_selector("input.form-check-input").click()
        driver.find_element_by_xpath("//input[@placeholder = \"Enter date\"]").click()
        driver.find_element_by_xpath("(//*[text() = \"30\"])[3]").click()
        driver.find_element_by_xpath("//*[text() = \"9:00 PM\"]").click()
        driver.find_element_by_xpath("(//input[@placeholder = \"Enter date\"])[2]").click()
        driver.find_element_by_xpath("//*[text() = \"11:30 PM\"]").click()
        driver.find_element_by_xpath("//*[text() = \"Create Survey\"]").click()
        driver.find_element_by_xpath("//*[text() = \"In Queue\"]").click()
        driver.find_element_by_xpath("//*[text() = \"Cancel Survey\"]").click()
        driver.find_element_by_xpath("//*[text() = \"Yes, Cancel Survey\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
