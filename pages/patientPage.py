from selenium.webdriver.common.by import By

class patientpage:
    patientName = (By.ID,"patientName")

    def getpatientname(self,driver):
        return driver.find_element(*self.patientName)

    def ClickSave(self,driver):
        driver.find_element(By.ID,"saveBtn").click()