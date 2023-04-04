from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    input("Type anything and enter... ")

    driver.implicitly_wait(10)


def find_images():
    driver.implicitly_wait(10)

    image_urls = []

    for i in range(3):
        elements = driver.find_elements(By.XPATH,"//img[contains(@class, 'ivm-view-attr__img--centered') and not(contains(@class, 'EntityPhoto'))]")
        for element in elements:
            image_url = element.get_attribute("src")
            if(image_url in image_urls):
                continue
            else:
                image_urls.append(image_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        driver.implicitly_wait(5)

    for image_url in image_urls:
        print(image_url)

    driver.implicitly_wait(10)


def searchPeople_basedOnCountry(search_keyword):
    search_field = driver.find_element(By.TAG_NAME,"input")
    search_field.click()
    search_field.clear()
    search_field.send_keys(search_keyword)
    search_field.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    people_filter_button = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[5]/button")
    people_filter_button.click()

    driver.implicitly_wait(10)



login(driver)
find_images()
searchPeople_basedOnCountry("Data science")