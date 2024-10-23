#!/usr/bin/env python3

import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Load environment variables from .env file
load_dotenv()

# LinkedIn credentials
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
new_about_text = "Your updated 'About' section content."

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    # Log in
    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    email_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Navigate to your profile
    driver.get("https://www.linkedin.com/in/your-profile-username/")
    time.sleep(5)

    # Click the 'More' button to edit the About section
    more_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'More actions')]")
    more_button.click()
    time.sleep(2)

    # Click on 'Edit About' (make sure the button or link is available for this action)
    edit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Edit About')]")
    edit_button.click()
    time.sleep(2)

    # Clear the existing text and input the new text
    about_text_area = driver.find_element(By.XPATH, "//textarea[contains(@aria-label, 'About')]")
    about_text_area.clear()
    about_text_area.send_keys(new_about_text)
    time.sleep(2)

    # Save the changes
    save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
    save_button.click()
    time.sleep(5)

    print("Profile updated successfully!")

finally:
    # Close the browser
    driver.quit()

