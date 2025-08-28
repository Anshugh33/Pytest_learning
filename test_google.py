import allure

@allure.title("Google Search Test")
@allure.description("Verify that google page opens and title contains 'Google'")
def test_google_search(driver):  #<--'driver' comes from fixture
    with allure.step("Open Google Home Page"):
      driver.get("https://www.google.com")
      with allure.step("verify page title contains'Google'"):
       assert "Google" in driver.title,"title does not contain 'Google'"