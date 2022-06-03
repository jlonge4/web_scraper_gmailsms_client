import time
import os
from gmail_sms_client import email_alert

from twilio.rest import Client

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_names():
    s = Service('chromedriver.exe')
    # print(num)
    WINDOW_SIZE = '1920,1080'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get("http://yourwebsite.org")

    time.sleep(2)
    number_of_days = browser.find_element(By.ID, 'DaysSearchBox')
    number_of_days.click()
    number_of_days.send_keys('7')
    time.sleep(1)
    browser.find_element(By.ID, 'DaysSearchButton').click()
    time.sleep(2)

    try:
        table_id = browser.find_element(By.ID, 'gvInmates_DXMainTable')
        rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        names = []
        for row in rows:
            # Get the columns (all the column 1)
            col = row.find_elements(By.TAG_NAME, "td")[0]  # note: index start from 0, 0 is col 1 (names)
            names.append(col.text)

        str_names = ' '.join([str(item) for item in names])
        email_alert("Arrest Records For 7 Days:", str_names, "your10digitnumber@vtext.com")
        
    except:
        email_alert("Arrest Records For 7 Days:", "No Arrests Made", "your10digitnumber@vtext.com")


get_names()
