import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
import csv


def get_value_by_label(driver, label):
    """Extract the associated value for a given label."""
    try:
        element = driver.find_element(By.XPATH, f"//td[contains(., '{label}')]/following-sibling::td/div[@class='small']")
        return element.text.strip()
    except:
        return None

# Initialize the driver
driver = webdriver.Chrome()

# Open the webpage 
driver.get('http://192.168.0.217/cgi-bin/spectra-menu.cgi?language=en')

# Find the username and password fields and enter the values
driver.find_element(By.NAME, 'name').clear()
driver.find_element(By.NAME, 'name').send_keys('webuser')
driver.find_element(By.NAME, 'pass').send_keys('1234')

# Select "Current production report" from the dropdown
select = Select(driver.find_element(By.NAME, 'option'))
select.select_by_value('2')


# Click the "Display" button
driver.find_element(By.NAME, 'show').click()

# Extract the desired values using the defined function
project_no = get_value_by_label(driver, 'Project No.')
software_version = get_value_by_label(driver, 'Software Version')
document = get_value_by_label(driver, 'Document')
user = get_value_by_label(driver, 'User')
system_date_time = get_value_by_label(driver, 'System Date & Time')
Format_Name = get_value_by_label(driver, 'Format name')
Number_of_blisters_in_format = get_value_by_label(driver, 'Number of blisters in format')
Position_error_detection = get_value_by_label(driver, 'Position error detection')
Start_of_production_run = get_value_by_label(driver, 'Start of production run')
End_of_production_run = get_value_by_label(driver, 'End of production run')
Number_of_evaluation_cycles = get_value_by_label(driver, 'Number of evaluation cycles')
Total_no_of_blisters = get_value_by_label(driver, 'Total no. of blisters')
Correctly_filled_blisters = get_value_by_label(driver, 'Correctly filled blisters')
Bad_blisters = get_value_by_label(driver, 'Bad blisters')
empty = get_value_by_label(driver, 'empty')
with_other_defects = get_value_by_label(driver, 'with other defects')
Violation_of_minus_tolerance = get_value_by_label(driver, 'Violation of minus tolerance')
Violation_of_plus_tolerance = get_value_by_label(driver, 'Violation of plus tolerance')
Empty_pocket = get_value_by_label(driver, 'Empty pocket')
Undefined_colour = get_value_by_label(driver, 'Undefined colour')
Wrong_colour = get_value_by_label(driver, 'Wrong colour')
Incorrect_location = get_value_by_label(driver, 'Incorrect location')
Shape = get_value_by_label(driver, 'Shape')
Perimeter = get_value_by_label(driver, 'Perimeter')


# Print the extracted values
print(f"Project No.: {project_no}")
print(f"Software Version: {software_version}")
print(f"Document: {document}")
print(f"User: {user}")
print(f"System Date & Time: {system_date_time}")
print(f"Format Name: {Format_Name}")
print(f"Number of blisters in format: {Number_of_blisters_in_format}")
print(f"Position error detection: {Position_error_detection}")
print(f"Start of Production Run: {Start_of_production_run}")
print(f"End of production run: {End_of_production_run}")
print(f"Number of evaluation cycles: {Number_of_evaluation_cycles}")
print(f"Total no. of blisters: {Total_no_of_blisters}")
print(f"Correctly filled blisters: {Correctly_filled_blisters}")
print(f"Bad blisters: {Bad_blisters}")
print(f"empty: {empty}")
print(f"with other defects: {with_other_defects}")
print(f"Violation of minus tolerance: {Violation_of_minus_tolerance}")
print(f"Violation of plus tolerance: {Violation_of_plus_tolerance}")
print(f"Empty Pocket: {Empty_pocket}")
print(f"Undefined Colour: {Undefined_colour}")
print(f"Wrong Colour: {Wrong_colour}")
print(f"Incorrect Location: {Incorrect_location}")
print(f"Shape: {Shape}")
print(f"Perimeter: {Perimeter}")


# Define a directory where you want to save the file (please replace with your actual directory)
directory_path = r"C:\Users\kblj946\Desktop\Example_CSV_Output_File"

# Get current timestamp
current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Define filename with current timestamp
filename = f"{directory_path}/Scanware_Output_{current_timestamp}.csv"

# Write the extracted values to CSV
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Label', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Label': 'Project No.', 'Value': project_no})
    writer.writerow({'Label': 'Software Version', 'Value': software_version})
    writer.writerow({'Label': 'Document', 'Value': document})
    writer.writerow({'Label': 'User', 'Value': user})
    writer.writerow({'Label': 'System Date & Time', 'Value': system_date_time})
    writer.writerow({'Label': 'Format Name', 'Value': Format_Name})
    writer.writerow({'Label': 'Number of blisters in format', 'Value': Number_of_blisters_in_format})
    writer.writerow({'Label': 'Position Error Detection', 'Value': Position_error_detection})
    writer.writerow({'Label': 'Start of Production Run', 'Value': Start_of_production_run})
    writer.writerow({'Label': 'End of production run', 'Value': End_of_production_run})
    writer.writerow({'Label': 'Number of evaluation cycles', 'Value': Number_of_evaluation_cycles})
    writer.writerow({'Label': 'Total no. of blisters', 'Value': Total_no_of_blisters})
    writer.writerow({'Label': 'Correctly filled blisters', 'Value': Correctly_filled_blisters})
    writer.writerow({'Label': 'Bad blisters', 'Value': Bad_blisters})
    writer.writerow({'Label': 'empty', 'Value': empty})
    writer.writerow({'Label': 'with other defects', 'Value': with_other_defects})
    writer.writerow({'Label': 'Violation of minus tolerance', 'Value': Violation_of_minus_tolerance})
    writer.writerow({'Label': 'Violation of plus tolerance', 'Value': Violation_of_plus_tolerance})
    writer.writerow({'Label': 'Empty Pocket', 'Value': Empty_pocket})
    writer.writerow({'Label': 'Undefined Colour', 'Value': Undefined_colour})
    writer.writerow({'Label': 'Wrong Colour', 'Value': Wrong_colour})
    writer.writerow({'Label': 'Incorrect Location', 'Value': Incorrect_location})
    writer.writerow({'Label': 'Shape', 'Value': Shape})
    writer.writerow({'Label': 'Perimeter', 'Value': Perimeter})
    
time.sleep(5)
