
# Facebook Automated Messaging Tool

I have created a Facebook Automated Messaging Tool using Python to send a private message to the profile links you provide!


## Installation

To install and run this project,

You can download the zip file or Clone the Project Repository using Git with the below command:
```bash
git clone https://github.com/DhruvAthaide/Facebook-Messaging-Automation.git
```


Once, you have installed the Repository then you can cd into the directory and pip install the requirements needed to run the tool:
```bash
cd Facebook-Messaging-Automation
```

```bash
pip install -r requirements.txt
```

Then, you need to create a CSV File and name it:
```bash
Name: profile_links.csv
```

Then, you need to set the following column name in the Excel File and paste the facebook profile's link you want to message in this column:
```bash
Column 1: Profile Links
```


Then, in the 'Facebook.py' file on Line 13 & 14 Enter your Username/Email ID and Password in between the Quotes for the String:
```bash
username = "Enter Your Username/Email"
password = "Enter Your Password"
```

Then, customize your messages which you want to send to the facebook profile's on Line 49-54 and you can add multiple messages which you want to send and the script will randomize the messages sent to each user:
```bash
messages = [
    "Message 1",
    "Message 2",
    "Message 3",
    # Add more messages as needed
]
```

Then, you can simply run the python file and not touch anything and it will execute the message sending to the facebook profile's provided in the CSV File.

Once the execution is done, there will be a new CSV File called 'profile_links_updated.csv' and in that file there will be a column next to the profile links and it will tell the status of whether it has messaged that particular profile or not. 

## Authors

- [@Dhruv Athaide](https://github.com/DhruvAthaide)
- [@Himanshu Nimonkar](https://github.com/BoomHimanshu)
- [@Chinmay Maitre](https://github.com/Chinmay-Maitre08)


## Languages & Tools Used:
<p align="left"> 
<a href="https://www.python.org/" target="_blank" rel="noreferrer"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.selenium.dev/" target="_blank" rel="noreferrer"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" alt="selenium" width="40" height="40"/> </a>
</p>