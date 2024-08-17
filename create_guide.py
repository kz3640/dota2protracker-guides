import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# get login creds
secrets_file_path = 'secrets.json'
with open(secrets_file_path, 'r') as file:
    secrets = json.load(file)
steam_credentials = secrets.get('steam_credentials', {})

username = steam_credentials.get('username')
email = steam_credentials.get('email')
password = steam_credentials.get('password')

# login to steam
driver = webdriver.Chrome()

try:
    driver.get("https://steamcommunity.com/login/home/?goto=login")
    #driver.implicitly_wait(5)  # wait for page to load

    LOGIN_CLASS = "_2GBWeup5cttgbTw8FM3tfx"
    # Wait until both elements are present
    wait = WebDriverWait(driver, 1)  # Adjust the timeout as needed
    username_field = wait.until(
        EC.presence_of_element_located((By.XPATH, f"(//input[@type='text' and @class='{LOGIN_CLASS}'])[1]"))
    )

    password_field = wait.until(
        EC.presence_of_element_located((By.XPATH, f"(//input[@type='password' and @class='{LOGIN_CLASS}'])[1]"))
    )

    # input creds
    username_field.send_keys(username)
    password_field.send_keys(password)

    # submit
    password_field.send_keys(Keys.RETURN)

    time.sleep(5)  # wait for page to load

    # navigate to create dota 2 guide page
    driver.get("https://steamcommunity.com/sharedfiles/editguide/?appid=570")
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
