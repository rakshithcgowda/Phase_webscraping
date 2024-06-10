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

# Create Select objects
select_month = Select(select_element_month)
select_year = Select(select_element_year)
select_country = Select(select_element_country)

# Iterate through each combination of month, year, and country
for month_option in select_month.options:
    month = month_option.text
    select_month.select_by_visible_text(month)
    time.sleep(1)  # Allow time for the page to update if necessary
    
    for year_option in select_year.options:
        year = year_option.text
        select_year.select_by_visible_text(year)
        time.sleep(1)
        
        for country_option in select_country.options:
            country = country_option.text
            select_country.select_by_visible_text(country)
            time.sleep(1)
            
            # Perform the action required after selecting each combination
            input_element = driver.find_element(By.CLASS_NAME, 'frm-btn')
            input_element.send_keys(Keys.ENTER)
            time.sleep(2)  # Wait for the page to reload or update
            
            # Extract and handle the results as needed
            print(f"Selected month: {month}, Selected year: {year}, Selected country: {country}")
            
            # Optionally, extract data from the results page
            # results = driver.find_element(By.ID, 'results')  # Adjust the locator as needed
            # data = results.text
            # print(data)
            
            # Navigate back to the original page
            back_button = driver.find_element(By.ID, 'IMG1')
            back_button.click()
            time.sleep(2)  # Wait for the page to reload or update

# Close the driver
driver.quit()
