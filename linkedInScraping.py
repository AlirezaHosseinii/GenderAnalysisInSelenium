from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()


def login(driver):
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    driver.get("https://www.linkedin.com/login")
    driver.maximize_window()

    username_field = driver.find_element(By.ID,"username")
    username_field.clear()
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID,"password")
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
    login_button.click()

    driver.implicitly_wait(10)

    input("Type anything and enter to close the browser...")

    driver.quit()


login(driver)