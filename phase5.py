# /***************************************** Phase5*************************************************************\
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import csv

# Path to the chromedriver executable
executable_path = 'chromedriver.exe'

# Create a service object
service = Service(executable_path)

# Function to initialize the driver and navigate to the webpage
def initialize_driver():
    driver = webdriver.Chrome(service=service)
    driver.get("https://tradestat.commerce.gov.in/meidb/cntcomq.asp?ie=e")
    driver.maximize_window()
    time.sleep(2)
    return driver

# Initialize the driver once
driver = initialize_driver()

# Locate the select elements
select_element_month = driver.find_element(By.ID, 'select1')
select_element_year = driver.find_element(By.ID, 'select2')
select_element_country = driver.find_element(By.ID, 'select3')
select_element_hscode = driver.find_element(By.ID, 'hslevel')

# Create Select objects
select_month = Select(select_element_month)
select_year = Select(select_element_year)
select_country = Select(select_element_country)
select_hscode = Select(select_element_hscode)
select_hscode.select_by_value('8')
time.sleep(3)

# Select the radio button with the id 'radioDALL'
radio_button_all = driver.find_element(By.ID, 'radioDAll')
radio_button_all.click()
time.sleep(3)

# Select quantity
quantity_button_all = driver.find_element(By.ID, 'radioqty')
quantity_button_all.click()
time.sleep(3)

# Select a specific country (e.g., Afghanistan)
country_name = 'AFGHANISTAN'  # Change this to the desired country
select_country.select_by_visible_text(country_name)
country = select_country.first_selected_option.text
time.sleep(1)  # Allow time for the page to update if necessary

# Select the year 2024
select_year.select_by_visible_text('2024')
year = select_year.first_selected_option.text
time.sleep(1)

# Open CSV file for writing
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Define the header with common columns
    header = ['Country', 'Sl.No.', 'HSCode', 'Commodity', 'Unit', 'Revised']
    csv_writer.writerow(header)

    # Iterate through each month of 2024 for the selected country
    for month_index in range(len(select_month.options)):
        select_month = Select(driver.find_element(By.ID, 'select1'))
        select_month.select_by_index(month_index)
        month = select_month.options[month_index].text
        time.sleep(1)
        
        # Append the Final_year_month for subsequent months
        if month_index > 0:
            header.append(f'Final_{year}_{month}')
            csv_writer.writerow(header)  # Write updated header
        
        # Perform the action required after selecting each combination
        input_element = driver.find_element(By.CLASS_NAME, 'frm-btn')
        input_element.send_keys(Keys.ENTER)
        time.sleep(3)  # Wait for the page to reload or update
        
        # Extract and handle the results as needed
        # Find all data cells directly
        data_cells = driver.find_elements(By.XPATH, '//table[@border="1"]/tbody/tr[position() > 1]/td[position() <= 6]')

        # Iterate through every 6 cells (representing one row) and extract data
        for i in range(0, len(data_cells), 6):
            row_data = [cell.text.strip() if cell.text.strip() != '' else 'NaN' for cell in data_cells[i:i+6]]
            csv_writer.writerow([country] + row_data)

        print(f"Selected country: {country}, Selected year: {year}, Selected month: {month}")
        
        # Navigate back to the original page
        driver.back()
        time.sleep(3)  # Wait for the page to reload or update

# Close the driver
driver.quit()

# Web scraping the table data
driver = initialize_driver()
table = driver.find_element(By.TAG_NAME, 'table')
rows = table.find_elements(By.TAG_NAME, 'tr')

# Write data to CSV
with open('output.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        header_cols = row.find_elements(By.TAG_NAME, 'th')
        if header_cols:
            writer.writerow([col.text.strip() for col in header_cols])
        else:
            cols = row.find_elements(By.TAG_NAME, 'td')
            # Replace blank spaces with 'NaN'
            row_data = [col.text.strip() if col.text.strip() != '' else 'NaN' for col in cols]
            writer.writerow(row_data)

# Close the driver
driver.quit()
