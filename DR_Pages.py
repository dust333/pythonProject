
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class DRLocators:
    LOCATOR_DR_NUMBER_FIELD_CLICKED = (By.CSS_SELECTOR, '#__next > div.sc-bdVaJa.web-promo__PageWrapper-sc-1mceb97-0.wrapper.jiQNER > div.sc-bdVaJa.web-promo__ContentBox-sc-1mceb97-1.wrapper.jbRvoG > div > div > div > div.sc-bdVaJa.wrapper.bmcsUd > div.sc-bdVaJa.wrapper.gChIVn > input')
    LOCATOR_DR_BUTTON = (By.CSS_SELECTOR, '#__next > div.sc-bdVaJa.web-promo__PageWrapper-sc-1mceb97-0.wrapper.jiQNER > div.sc-bdVaJa.web-promo__ContentBox-sc-1mceb97-1.wrapper.jbRvoG > div > div > div > div.sc-bdVaJa.wrapper.bmcsUd > div.sc-bdVaJa.wrapper.jGoBmg > button')
    LOCATOR_DR_CODE_FIELD = (By.CSS_SELECTOR, '#__next > div.sc-bdVaJa.web-promo__PageWrapper-sc-1mceb97-0.wrapper.jiQNER > div.sc-bdVaJa.web-promo__ContentBox-sc-1mceb97-1.wrapper.jbRvoG > div > div > div > div.sc-bdVaJa.wrapper.bmcsUd > div.sc-bdVaJa.wrapper.iwAOFP > div.sc-bdVaJa.input-field__FieldRoot-yyniwk-5.wrapper.dWfwyk > div > input')
    LOCATOR_FAULT = (By.CSS_SELECTOR, '#__next > div.Toastify > div > div')


class DRAuth(BasePage):

    def enter_number(self, number):
        number_field = self.find_element(DRLocators.LOCATOR_DR_NUMBER_FIELD_CLICKED)
        number_field.click()
        number_field.clear()
        number_field.send_keys(number)
        return number_field

    def click_on_login(self):
        return self.find_element(DRLocators.LOCATOR_DR_BUTTON, time=5).click()

    def check_code_field(self):
        return self.find_element(DRLocators.LOCATOR_DR_CODE_FIELD, time=2)

    def check_fault(self):
        return self.find_element(DRLocators.LOCATOR_FAULT, time=2)
