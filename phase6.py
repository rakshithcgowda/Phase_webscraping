# /********************************************* Phase6*************************************************\
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

# Extract initial information to create the base header
input_element = driver.find_element(By.CLASS_NAME, 'frm-btn')
input_element.send_keys(Keys.ENTER)
time.sleep(3)  # Wait for the page to reload or update

# Extract the static information: Sl.No., HSCode, Commodity, Unit, and Revised
data_rows = driver.find_elements(By.XPATH, '//table[@border="1"]/tbody/tr[position() > 1]')
static_info = []
for row in data_rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    static_info.append([country] + [cell.text.strip() if cell.text.strip() != '' else 'NaN' for cell in cells[:5]])

# Open CSV file for writing
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Define the initial header
    header = ['Country', 'Sl.No.', 'HSCode', 'Commodity', 'Unit', 'Revised']
    
    # Add months to the header
    for month_index in range(len(select_month.options)):
        month = select_month.options[month_index].text
        header.append(f'Final_{year}_{month}')
    
    # Write the header to the CSV
    csv_writer.writerow(header)
    
    # Write the static information to the CSV
    for row in static_info:
        csv_writer.writerow(row + ['NaN'] * len(select_month.options))

# Reinitialize the driver to fetch monthly data
driver.quit()
driver = initialize_driver()

# Locate the select elements again
select_element_month = driver.find_element(By.ID, 'select1')
select_element_year = driver.find_element(By.ID, 'select2')
select_element_country = driver.find_element(By.ID, 'select3')
select_element_hscode = driver.find_element(By.ID, 'hslevel')

# Create Select objects again
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

# Select the specific country and year again
select_country.select_by_visible_text(country_name)
select_year.select_by_visible_text('2024')
time.sleep(1)

# Iterate through each month to fetch and append the monthly data
for month_index in range(len(select_month.options)):
    select_month = Select(driver.find_element(By.ID, 'select1'))
    select_month.select_by_index(month_index)
    month = select_month.options[month_index].text
    time.sleep(1)
    
    # Perform the action required after selecting each combination
    input_element = driver.find_element(By.CLASS_NAME, 'frm-btn')
    input_element.send_keys(Keys.ENTER)
    time.sleep(3)  # Wait for the page to reload or update
    
    # Extract the monthly data
    data_rows = driver.find_elements(By.XPATH, '//table[@border="1"]/tbody/tr[position() > 1]')
    
    # Open the CSV file for appending
    with open('output.csv', 'r+', newline='', encoding='utf-8') as csvfile:
        csv_reader = list(csv.reader(csvfile))
        csvfile.seek(0)
        csv_writer = csv.writer(csvfile)
        
        # Iterate through each row and update the respective column with monthly data
        for row_index, row in enumerate(data_rows, start=1):
            cells = row.find_elements(By.TAG_NAME, 'td')
            monthly_data = [cell.text.strip() if cell.text.strip() != '' else 'NaN' for cell in cells[5:6]]
            csv_reader[row_index].append(monthly_data[0])
        
        # Write back the updated rows to the CSV
        csv_writer.writerows(csv_reader)

    print(f"Selected country: {country}, Selected year: {year}, Selected month: {month}")

# Close the driver
driver.quit()
