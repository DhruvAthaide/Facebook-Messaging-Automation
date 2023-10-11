from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import random

# Add your Facebook login credentials
username = "Enter your Username/Email ID Here"
password = "Enter your Password Here"

# XLSX File Reading
data = pd.read_excel("profile_links.xlsx", header=None, names=['Profile Links'])

profile_links = data['Profile Links'].tolist()

# Configuring the Chrome driver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Log in to Facebook
driver.get("https://www.facebook.com")

# Find and input the username
username_field = driver.find_element(By.XPATH, "//input[@name='email']")
username_field.send_keys(username)

# Find and input the password
password_field = driver.find_element(By.XPATH, "//input[@name='pass']")
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element(By.XPATH, "//button[@name='login']")
login_button.click()

# Delay to allow Login Process
time.sleep(5)

number = 1
text = "your message"

# Limit the number of messages sent in total and within a specific timeframe
max_messages = 50  # Set your desired maximum number of messages
messages_sent = 0
time_interval = 600  # Set the time interval in seconds (e.g., 10 minutes)

for profile_link in profile_links:
    try:
        if messages_sent >= max_messages:
            print("Stress test limit reached. Exiting...")
            break

        driver.get(profile_link)
        driver.implicitly_wait(10)  # Increase the wait time if the webpage takes time to load

        # Add logic to handle permissions if needed
        # Example: You may need to click a button to grant permission for sending messages

        # Find and click the 'Message' button or the button leading to the messaging option
        message_button_xpath = '//*[@id="mount_0_0_mF"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div[2]/span/span'
        message_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, message_button_xpath))
        )
        message_button.click()

        # Wait for the messaging popup to load
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div._1mf._1mj'))
        )

        # Find the message input field
        msg = driver.find_element_by_css_selector('div._1mf._1mj')

        for letters in text:
            msg.send_keys(letters)
            time.sleep(random.uniform(0.1, 0.3))

        msg.send_keys(Keys.ENTER)
        print("Message sent to\t", profile_link)

        messages_sent += 1

        # Pause the script to avoid rapid actions
        time.sleep(random.uniform(3.2, 4.5))

        # Implement time interval check to prevent continuous messaging within a short timeframe
        if messages_sent % max_messages == 0:
            print(f"Waiting for {time_interval / 60} minutes to avoid detection...")
            time.sleep(time_interval)

    except Exception as e:
        print("Error sending message to", profile_link, ":", e)
        # Handle specific exceptions if needed
        # Example: If you encounter a permission denied error, handle it here

    print(number, "-----------------------------------------Msg_automate_kaux---------------------------------------------")
    number += 1

# Close the driver after processing
driver.quit()
