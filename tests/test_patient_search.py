from pages.patientPage import patientpage
from utils.driverUtils import LaunchBrowser

def TestPatientSearch():
    driver = LaunchBrowser()
    page = patientpage()

    driver.get("http://dummy-healthcare-app")

    page.getpatientname(driver).send_keys("John Doe")
    page.ClickSave(driver)

    assert True