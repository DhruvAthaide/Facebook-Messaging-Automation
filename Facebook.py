from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import random

# Facebook Login Credentials
username = "athaidedhruv@gmail.com"
password = "Jonathan1908"

# XLSX File Reading
data = pd.read_excel("profile_links.xlsx", header=None, names=['Profile Links'])

profile_links = data['Profile Links'].tolist()

# New XLSX file to store failed profile links
failed_profiles_file = "failed_profiles.xlsx"

# Create an empty DataFrame to store failed profile links
failed_profiles_df = pd.DataFrame(columns=['Profile Links'])

# Configuring the Chrome driver and Handling Notification Alert
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
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

# Different messages array
messages = [
    "Message 1",
    "Message 2",
    "Message 3",
    # Add more messages as needed
]

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))  # Wait for the page to load

        # XPath for the message button
        message_button_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div'

        # Wait for the message button to be clickable
        message_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, message_button_xpath))
        )
        message_button.click()


        # XPath for the message input field
        message_input_xpath = '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p'

        # Wait for the messaging popup to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, message_input_xpath))
        )

        # Find the message input field using XPath
        msg = driver.find_element(By.XPATH, message_input_xpath)

        # Randomly select a message from the array
        selected_message = random.choice(messages)

        for letters in selected_message:
            msg.send_keys(letters)
            time.sleep(random.uniform(0.1, 0.3))

        msg.send_keys(Keys.ENTER)
        print("Message sent to\t", profile_link)

        messages_sent += 1

        # Pause the script to avoid rapid actions
        time.sleep(random.uniform(3.2, 4.5))

        # Implement time interval check with a random additional delay
        if messages_sent % max_messages == 0:
            additional_delay = random.uniform(1, 60)  # Random number of seconds (1 to 60)
            total_delay = 240 + additional_delay  # 4 minutes + additional random seconds
            print(f"Waiting for {total_delay / 60} minutes to avoid detection...")
            time.sleep(total_delay)
            
        try:
            # Find the close chat button by Xpath
            close_chat_button_xpath = '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/span[4]/div'
            close_chat_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, close_chat_button_xpath))
            )
            close_chat_button.click()
            print("Clicked close chat button for previous Profile.")

        except Exception as close_button_error:
            print("Error clicking close chat button for previous Profile:", close_button_error)

    except Exception as e:
        print("Error sending message to", profile_link, ":", e)

        # Log the failed profile link to the CSV file
        with open(failed_profiles_file, 'a') as file:
            file.write(profile_link + '\n')

        print(f"Profile link {profile_link} added to {failed_profiles_file}")

    print(number, "-----------------------------------------Msg_automate_kaux---------------------------------------------")
    number += 1

driver.quit()