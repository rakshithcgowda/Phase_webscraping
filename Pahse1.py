# /**************************************************Phase1******************************************************\
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

driver.get("https://tradestat.commerce.gov.in/meidb/cntcomq.asp?ie=e")
driver.maximize_window()
time.sleep(2)



# selecting the month ............................................................
select_element = driver.find_element(By.ID, 'select1')
select = Select(select_element)
select.select_by_value("4")
select_element.click()  # Optionally click the selected option
time.sleep(2)  # Add a delay to observe the changes

# making global variable
# for i in  select_element:




# selecting the year ............................................................
select_element1 = driver.find_element(By.ID, 'select2')
select = Select(select_element1)
select.select_by_value("2023")
select_element.click()  # Optionally click the selected option
time.sleep(2)  # Add a delay to observe the changes



# selecting the country .........................................................
select_element3 = driver.find_element(By.ID, 'select3')
select = Select(select_element3)
select.select_by_value("7")
select_element.click()  # Optionally click the selected option
time.sleep(2)  # Add a delay to observe the changes


# selecting the Hs code ........................................................
select_element4 = driver.find_element(By.ID, 'hslevel')
select = Select(select_element4)
select.select_by_value("8")
select_element.click()  # Optionally click the selected option
time.sleep(2)  # Add a delay to observe the changes


# selecting the sort on ......................................................
select_element5 = driver.find_element(By.NAME, 'sort')
select = Select(select_element5)
select.select_by_value("1")
select_element.click()  # Optionally click the selected option
time.sleep(2)  # Add a delay to observe the changes


# selecting the display record .................................................
radio_button = driver.find_element(By.ID, 'radioDAll')
# Click the radio button to select it
radio_button.click()
# Optionally, add a delay to observe the changes
time.sleep(2)




# # selecting the value ............................................................ 
# radio_button1 = driver.find_element(By.ID, 'radioval')
# # Click the radio button to select it
# radio_button1.click()
# # Optionally, add a delay to observe the changes
# time.sleep(2)


# selecting quantity................................................................
radio_button2 = driver.find_element(By.ID, 'radioqty')
# Click the radio button to select it
radio_button2.click()
# Optionally, add a delay to observe the changes
time.sleep(2)

# table = driver.find_element(By.TAG_NAME, 'table')
# header_row = table.find_element(By.TAG_NAME, 'tr')  # Assuming headers are in the first row

# header_cells = header_row.find_elements(By.TAG_NAME, 'th')
# for header_cell in header_cells:
#     print(header_cell.text)


# automating the submit button..................................................
input_element = driver.find_element(By.CLASS_NAME, 'frm-btn')
input_element.send_keys(Keys.ENTER)


back_button = driver.find_element(By.ID, 'IMG1')
back_button.click()
time.sleep(5)


























time.sleep(30)
driver.quit()