# Intentional review issues below

from utils.driverUtils import LaunchBrowser

def test_claim_processing():
    driver = LaunchBrowser()

    claimId = "12345"
    ClaimID = "99999"   # naming inconsistency

    if claimId == ClaimID
        print("same claim")   # syntax error: missing colon above

    driver.get("http://claims-app")

    unusedVariable = "review me"

    assert driver.title == "Claims"