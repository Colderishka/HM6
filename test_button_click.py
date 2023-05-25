# 1 задание
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_run():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(16)

    driver.get("http://uitestingplayground.com/ajax")
    path_to_button = '#ajaxButton'
    driver.find_element(By.CSS_SELECTOR, path_to_button).click()
    green_line = driver.find_element(By.CSS_SELECTOR, "#content")
    text = green_line.find_element(By.CSS_SELECTOR, "p.bg-success").text
    print(text)
    assert text == 'Data loaded with AJAX get request.'

    driver.close()
    driver.quit()
