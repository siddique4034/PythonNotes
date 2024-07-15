from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


NAME = "Md Siddique"
CONTACT_NUMBER = "+91 7858842229"
EMAIL = "siddiquemd4034@gmail.com"
ADDRESS = "Muslim gali Jugsalai Jamshedpur"
PINCODE = "831006"
DOB_DAY = "10"
DOB_MONTH = "03"
DOB_YEAR = "2006"
GENDER = "Male"
CAPTCHA_CODE = "GNFPYC"
SCREENSHOT_PATH = "confirmation_screenshot.png"
FORM_URL = 'https://forms.gle/WT68aV5UnPajeoSc8'
NAME_FIELD_XPATH = '//input[@aria-labelledby="i1"]'
CONTACT_NUMBER_FIELD_XPATH = '//input[@aria-labelledby="i5"]'
EMAIL_FIELD_XPATH = "//input[@aria-describedby='i10 i11' and @aria-disabled='true' and @aria-labelledby='i9' and @type='text']"
FULL_ADDRESS_FIELD_XPATH = '//textarea[@class="KHxj8b tL9Q4c" and @aria-label="Your answer"]'
PINCODE_FIELD_XPATH = "//input[@aria-describedby='i18 i19' and @aria-disabled='true' and @aria-labelledby='i17' and @autocomplete='off' and @class='whsOnd zHQkBf' and @data-initial-dir='auto' and @data-initial-value='' and @dir='auto' and @disabled='' and @jsname='YPqjbf' and @required='' and @tabindex='0' and @type='text']"
DOB_DAY_FIELD_XPATH = '//input[@aria-label="Day of the month" and @class="whsOnd zHQkBf"]'
DOB_MONTH_FIELD_XPATH = '//input[@aria-label="Month"]'
DOB_YEAR_FIELD_XPATH = '//input[@aria-label="Year" and @autocomplete="off" and @class="whsOnd zHQkBf" and @disabled="true" and @jsname="YPqjbf"]'
GENDER_FIELD_XPATH = "//input[@aria-describedby='i26 i27' and @aria-disabled='true' and @aria-labelledby='i25' and @class='whsOnd zHQkBf' and @disabled and @jsname='YPqjbf' and @required and @tabindex='0' and @type='text']"
CAPTCHA_FIELD_XPATH = '/html[1]/body[2]/div[8]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
SUBMIT_BUTTON_XPATH = "//span[contains(@class, 'NPEfkd') and contains(@class, 'RveJvd') and contains(@class, 'snByac') and text()='Submit']"


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver
webdriver_service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

driver.get(FORM_URL) #getting google form

time.sleep(2)

name_field = driver.find_element(By.XPATH, NAME_FIELD_XPATH)
contact_field = driver.find_element(By.XPATH, CONTACT_NUMBER_FIELD_XPATH)
email_field = driver.find_element(By.XPATH, EMAIL_FIELD_XPATH)
address_field = driver.find_element(By.XPATH, FULL_ADDRESS_FIELD_XPATH)
pincode_field = driver.find_element(By.XPATH, PINCODE_FIELD_XPATH)
dob_dd_field = driver.find_element(By.XPATH, DOB_DAY_FIELD_XPATH)
dob_mm_field = driver.find_element(By.XPATH, DOB_MONTH_FIELD_XPATH)
dob_yyyy_field = driver.find_element(By.XPATH, DOB_YEAR_FIELD_XPATH)
gender_field = driver.find_element(By.XPATH, GENDER_FIELD_XPATH)
captcha_field = driver.find_element(By.XPATH, CAPTCHA_FIELD_XPATH)
submit_button = driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH)


# Filling out form
name_field.send_keys(NAME)
contact_field.send_keys(CONTACT_NUMBER)
email_field.send_keys(EMAIL)
address_field.send_keys(ADDRESS)
pincode_field.send_keys(PINCODE)
dob_dd_field.send_keys(DOB_DAY)
dob_mm_field.send_keys(DOB_MONTH)
dob_yyyy_field.send_keys(DOB_YEAR)
gender_field.send_keys(GENDER)
captcha_field.send_keys(CAPTCHA_CODE)
submit_button.click() # Submit the form

time.sleep(2)

driver.save_screenshot(SCREENSHOT_PATH) # Capture Screenshot

driver.quit() # Close the browser
