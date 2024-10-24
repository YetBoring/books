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
profilename = os.getenv('PROFILENAME')
new_about_text = "Coming soon ..."

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

    me_button = driver.find_element(By.XPATH, "//button[contains(., 'Me')]")
    me_button.click()
    time.sleep(2)

    # Navigate to your profile
    profile_link = driver.find_element(By.LINK_TEXT, "View Profile")
    profile_link.click()
    time.sleep(2)

    # Click the 'More' button to edit the About section
    more_button = driver.find_element(By.XPATH, "//*[name()='svg'][contains(@aria-label, 'Edit about')]")
    more_button.click()
    time.sleep(2)

    # Clear the existing text and input the new text
    about_text_area = driver.find_element(By.XPATH, "//textarea")
    about_text_area.clear()
    about_text_area.send_keys(new_about_text)
    time.sleep(2)

    # Save the changes
    save_button = driver.find_element(By.XPATH, "//button[contains(., 'Save')]")
    save_button.click()
    time.sleep(5)

    print("Profile updated successfully!")

finally:
    # Close the browser
    driver.quit()

