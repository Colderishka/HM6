# задание 2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_run():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(16)

    driver.get("http://uitestingplayground.com/textinput")
    line = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
    line.send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
    text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
    print(text)
    assert text == "SkyPro"

    driver.close()
    driver.quit()

test_run()