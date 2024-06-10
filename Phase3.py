# ********************************************* Phase3 **********************************************************

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
            # Example: clicking a search or submit button
            input_element = driver.find_element(By.CLASS_NAME, 'frm-btn')
            input_element.send_keys(Keys.ENTER)
            time.sleep(2)  # Wait for the page to reload or update


            back_button = driver.find_element(By.ID, 'IMG1')
            back_button.click()
            
            # Extract and handle the results as needed
            # Example: print a message or scrape some data
            print(f"Selected month: {month}, Selected year: {year}, Selected country: {country}")
            
            # Optionally, extract data from the results page
            # results = driver.find_element(By.ID, 'results')  # Adjust the locator as needed
            # data = results.text
            # print(data)
            
            # Navigate back to the original page if necessary
            # driver.back()
 
            time.sleep(2)

# Close the driver
driver.refresh()





































# # Open CSV file for writing
# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)

#     # Loop through each combination of month, year, and country
#     for month in months:
#         for year in years:
#             for country in countries:
#                 # Selecting the month
#                 select_element = driver.find_element(By.ID, 'select1')
#                 select = Select(select_element)
#                 print (months[month])
#                 select.select_by_visible_text(months[month])
#                 time.sleep(2)

#                 # Selecting the year
#                 select_element1 = driver.find_element(By.ID, 'select2')
#                 select1 = Select(select_element1)
#                 select1.select_by_value(year)
#                 time.sleep(2)

#                 # Selecting the country
#                 select_element3 = driver.find_element(By.ID, 'select3')
#                 select3 = Select(select_element3)
#                 select3.select_by_value(country)
#                 time.sleep(2)

#                 # Selecting the Hs code
#                 select_element4 = driver.find_element(By.ID, 'hslevel')
#                 select4 = Select(select_element4)
#                 select4.select_by_value("2")  # Example HS code level
#                 time.sleep(2)

#                 # Selecting the sort on
#                 select_element5 = driver.find_element(By.NAME, 'sort')
#                 select5 = Select(select_element5)
#                 select5.select_by_value("0")
#                 time.sleep(2)

#                 # Selecting the display record
#                 radio_button = driver.find_element(By.ID, 'radioDAll')
#                 radio_button.click()
#                 time.sleep(2)

#                 # Selecting quantity
#                 radio_button2 = driver.find_element(By.ID, 'radioqty')
#                 radio_button2.click()
#                 time.sleep(2)

#                 # Automating the submit button
#                 input_element = driver.find_element(By.CLASS_NAME, 'frm-btn')
#                 input_element.send_keys(Keys.ENTER)

#                 time.sleep(5)

#                 # Web scraping the table data
#                 table = driver.find_element(By.TAG_NAME, 'table')
#                 rows = table.find_elements(By.TAG_NAME, 'tr')