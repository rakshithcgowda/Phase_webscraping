# ************************************************ Phase 2*****************************************************

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# Path to the chromedriver executable
executable_path = 'chromedriver.exe'

# Create a service object
service = Service(executable_path)

# Create a WebDriver instance for Chrome using the service
driver = webdriver.Chrome(service=service)

# Function to initialize the driver and navigate to the webpage
def initialize_driver(driver):
    driver.get("https://tradestat.commerce.gov.in/meidb/cntcomq.asp?ie=e")
    driver.maximize_window()
    time.sleep(2)
    return driver

# Initialize the driver
driver = initialize_driver(driver)

# Selecting the month
select_element = driver.find_element(By.ID, 'select1')
select = Select(select_element)
select.select_by_value("7")  # July
time.sleep(2)

# Selecting the year
select_element1 = driver.find_element(By.ID, 'select2')
select = Select(select_element1)
select.select_by_value("2022")
time.sleep(2)

# Selecting the country
select_element3 = driver.find_element(By.ID, 'select3')
select = Select(select_element3)
select.select_by_value("1")  # India
time.sleep(2)

# Selecting the Hs code
select_element4 = driver.find_element(By.ID, 'hslevel')
select = Select(select_element4)
select.select_by_value("8")  # Example HS code level
time.sleep(2)

# Selecting the sort on
select_element5 = driver.find_element(By.NAME, 'sort')
select = Select(select_element5)
select.select_by_value("0")
time.sleep(2)

# Selecting the display record
radio_button = driver.find_element(By.ID, 'radioDAll')
radio_button.click()
time.sleep(2)

# Selecting quantity
radio_button2 = driver.find_element(By.ID, 'radioqty')
radio_button2.click()
time.sleep(2)

# Automating the submit button
input_element = driver.find_element(By.CLASS_NAME, 'frm-btn')
input_element.send_keys(Keys.ENTER)

time.sleep(5)

# Web scraping the table data
table = driver.find_element(By.TAG_NAME, 'table')
rows = table.find_elements(By.TAG_NAME, 'tr')

# Write data to CSV
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        header_cols = row.find_elements(By.TAG_NAME, 'th')
        if header_cols:
            writer.writerow([col.text for col in header_cols])
        else:
            cols = row.find_elements(By.TAG_NAME, 'td')
            # Replace blank spaces with 'NaN'
            row_data = [col.text if col.text.strip() != '' else 'NaN' for col in cols]
            writer.writerow(row_data)

driver.refresh()

