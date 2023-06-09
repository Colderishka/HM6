# задание 3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_run():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    waiter = WebDriverWait(driver, 30)
    waiter.until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "#text"), "Done!" ))
    atribute = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")
    print(atribute)
    assert atribute == 'https://bonigarcia.dev/selenium-webdriver-java/img/award.png'

    driver.close()
    driver.quit()

