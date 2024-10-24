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

    # Click the 'post' button to edit a new post
    post_button = driver.find_element(By.XPATH, "//button[contains(., 'Start a post')]")
    post_button.click()
    time.sleep(2)

    # Clear the existing text and input the new text
    post_text_area = driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Text editor for creating content')]")
    post_text_area.clear()
    post_text_area.send_keys("hello world!")
    time.sleep(2)

    # Save the changes
    save_button = driver.find_element(By.XPATH, "//button[contains(., 'Post')]")
    save_button.click()
    time.sleep(5)

    print("Posted successfully!")

finally:
    # Close the browser
    driver.quit()

