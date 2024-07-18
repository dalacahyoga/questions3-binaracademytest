from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#------------------------------------------------------------------------------------------------------------
#--- This automation code use full XPATH due to there is "Shadow DOM" at https://www.traveloka.com/id-id/ ---
#------------------------------------------------------------------------------------------------------------

# Initialize the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the car rental page
driver.get("https://www.traveloka.com/id-id/")
time.sleep(2)

# Select Cars Product
driver.find_element(By.LINK_TEXT, 'Rental Mobil').click()

# Select tab Without Driver
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2][text()="Tanpa Sopir"]').click()

# Select Pick-up Location
driver.find_element(By.XPATH,'//*[@id="__next"]/div[6]/div/div[2]/div/div/div[3]/div[2]').click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div[6]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/h3[text()="Jakarta"]'))).click()
driver.execute_script("window.scrollBy(0, -300);")
time.sleep(1)

# Select Pick-up Date & Time
 # -Pick Up Date
from datetime import date
today = date.today()
pickUpDate = today.day + 2
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[1]/div').click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[3]/div['+str(pickUpDate)+']/div/div/div[2]/div[2]/div[text()="'+str(pickUpDate)+'"]'))).click()
driver.execute_script("window.scrollBy(0, -500);")
time.sleep(1)

# -Pick Up Time
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[3]/div/div[1]/input'))).click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[10]/div[2][text()="9"]').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[3]/div[2]/div/div/div[1]/div[2][text()="0"]').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[text()="Selesai"]').click()
driver.execute_script("window.scrollBy(0, -500);")
time.sleep(1)

# Select Drop-off Date & Time
 # -Drop Off Date
dropUpDate = today.day + 5
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[5]/div/div[1]/input').click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[5]/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[3]/div['+str(dropUpDate)+']/div/div/div[2]/div[2]/div[text()="'+str(dropUpDate)+'"]'))).click()
driver.execute_script("window.scrollBy(0, -500);")
time.sleep(1)

 # -Drop Off Time
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[7]/div/div[1]/input'))).click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[7]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[12]/div[text()="11"]').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[7]/div/div[2]/div/div/div[1]/div[3]/div[2]/div/div/div[1]/div[2][text()="0"]').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[7]/div/div[2]/div/div/div[2]/div/div[text()="Selesai"]').click()
driver.execute_script("window.scrollBy(0, -500);")
time.sleep(1)

# Click button Search Car
driver.find_element(By.XPATH, '//*[@id="__next"]/div[6]/div/div[2]/div/div/div[4]/div[9]/div/div[2]/div[2][text()="Cari Mobil"]').click()

# Select Car
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[5]/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[3]/div/div[2]/div[text()="Lanjutkan"]'))).click()

# Select Car Provider
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[5]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[text()="Lanjutkan"]'))).click()

# Select Pick-up Location in “Rental Office”
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="RENTAL_PICKUP_LOCATION"]/div/div/div[3]/div[1]/div[2]/div/div/div[2][text()="Kantor Rental"]'))).click()
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="RENTAL_PICKUP_LOCATION"]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div/div[1]/div'))).click()
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="RENTAL_PICKUP_LOCATION"]/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]'))).click() 

# Select Drop-off Location in “Other Location”
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="RENTAL_DROPOFF_LOCATION"]/div/div/div[5]/div[1]/div[2]/div'))).click() 
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="RENTAL_DROPOFF_LOCATION"]/div/div/div[5]/div[2]/div/div/div[1]/div/div[1]/input'))).click() 
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="RENTAL_DROPOFF_LOCATION"]/div/div/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]'))).click() 

# Input Pick-up/Drop-off notes (optional)
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[5]/div/div[1]/div/div[3]/div[3]/div/div[1]/h3[text()="Durasi Rental"]'))) 
driver.find_element(By.XPATH, '//*[@id="RENTAL_DROPOFF_LOCATION"]/div/div/div[5]/div[2]/div/div[2]/div/textarea').click() 
driver.find_element(By.XPATH, '//*[@id="RENTAL_DROPOFF_LOCATION"]/div/div/div[5]/div[2]/div/div[2]/div/textarea').send_keys('Optional Notes') 

# Click button Book Now
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[5]/div/div[1]/div/div[5]/div[3]/div/div[2]/div[text()="Lanjutkan"]').click() 

#-----------------------------------------------------------------------------------
#--- After this step, recaptcha display. To Handle Recaptcha Pass By Manual User ---
#-----------------------------------------------------------------------------------

# Fill Contact Details
WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/input'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/input'))).send_keys('John Doe New')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/input'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/input'))).send_keys('john.doe123@example.com')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/input'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/input'))).send_keys('6234567890')

# Fill Driver Details
title = Select(driver.find_element(By.XPATH, '//*[@id="adultForm0"]/div/div/div[2]/div[1]/div/div/select'))
title.select_by_value('MR')

driver.find_element(By.XPATH, '//*[@id="adultForm0"]/div/div/div[2]/div[2]/div/div[1]/input').click()
driver.find_element(By.XPATH, '//*[@id="adultForm0"]/div/div/div[2]/div[2]/div/div[1]/input').send_keys('John Doe New')

driver.find_element(By.XPATH, '//*[@id="adultForm0"]/div/div/div[2]/div[3]/div[1]/input').click()
driver.find_element(By.XPATH, '//*[@id="adultForm0"]/div/div/div[2]/div[3]/div[1]/input').send_keys('6234567890')

# Click Continue
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div[4]/div/div').click()

# Add a special request (optional)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[1]/div[9]/div/div/div[3]/div[1]/textarea')))
driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div[9]/div/div/div[3]/div[1]/textarea').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div[9]/div/div/div[3]/div[1]/textarea').send_keys('Optional Request')

# Check all rental requirements
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[1]/div[11]/div/div/div/div[2][text()="Ketuk untuk centang syarat rental."]')))
driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div[11]/div/div/div/div[2][text()="Ketuk untuk centang syarat rental."]').click()
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,'/html/body/div[8]/div/div[2]/div/div/div[2]/div')))
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[8]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[8]/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div[text()="Simpan"]'))).click()

# Click Continue
time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")
driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div[14]/div/div/div/div[2]').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div[text()="Lanjutkan"]'))).click()

# Select payment method and proceed with payment
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/div/div[1]'))).click()
time.sleep(2)
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[1]/div[1]/div/div[5]/div[2]/div[1]/div[2]'))).click()
time.sleep(5)

# Close the browser
driver.quit()



