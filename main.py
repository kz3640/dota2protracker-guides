from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the browser
driver = webdriver.Chrome()

try:
    # Navigate to the Steam login page
    driver.get("https://steamcommunity.com/login/home/?goto=login")

    # Wait for the page to load (optional, you may need to use WebDriverWait for dynamic content)
    driver.implicitly_wait(5)  # Waits up to 10 seconds for elements to be present

    # Steam Login Class
    LOGIN_CLASS = "_2GBWeup5cttgbTw8FM3tfx"
    # Find the username and password input fields
    username_field = driver.find_element(By.XPATH, f"(//input[@type='text' and @class='{LOGIN_CLASS}'])[1]")
    password_field = driver.find_element(By.XPATH, f"(//input[@type='password' and @class='{LOGIN_CLASS}'])[1]")

    print(username_field.get_attribute('outerHTML'))
    print(password_field.get_attribute('outerHTML'))

    # Input your login credentials
    username_field.send_keys("dota2protracker_guides")
    password_field.send_keys("JV2LRDA4w0eTUEW4bwCxg0S4lGL0FIGl")

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(10)  # Adjust the sleep time as needed

    # Additional actions can be performed here

finally:
    # Close the browser
    driver.quit()
