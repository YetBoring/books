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

    print("Login successfully!")

finally:
    # Close the browser
    driver.quit()

