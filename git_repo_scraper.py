from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# Replace these with your actual GitHub username and password
username = 'Your Username'
password = 'Your Password'

# Initialize WebDriver
browser = webdriver.Chrome()
actions = ActionChains(browser)

#Initialize Excel Workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Repository Name', 'URL']) # Column Headers

# Open GitHub
browser.get('https://github.com/')
# Click on the "Sign in" button
sign_in_button = browser.find_element(By.LINK_TEXT, 'Sign in')
time.sleep(3)
sign_in_button.click()
time.sleep(5)

# Enter username and password, then log in
username_field = browser.find_element(By.ID, 'login_field')
password_field = browser.find_element(By.ID, 'password')

username_field.send_keys(username)
time.sleep(5)
password_field.send_keys(password)
time.sleep(3)
# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the main page to load
time.sleep(5)

# Click on the expand search button
expand_search_button = browser.find_element(By.CLASS_NAME, 'AppHeader-search-whenNarrow')
expand_search_button.click()

# Wait for the search area to expand
time.sleep(3)  # Again, it's better to use explicit waits here

# Find the search input field, send the search query, and press Enter
search_field = browser.find_element(By.NAME, 'query-builder-test')
time.sleep(3)
search_field.send_keys("machine learning")
time.sleep(5)
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(5)

# Extract and print the repository names and URLs
# Here I set range 1 to 16 you can change it so that it can go to end
for page in range(1, 16):
    # Extract repository names and URLs
    repo_elements = browser.find_elements(By.CSS_SELECTOR, '.Box-sc-g0xbh4-0.bItZsX .search-title a')
    for repo_element in repo_elements:
        name = repo_element.text
        url = repo_element.get_attribute('href')
        ws.append([name, url])  # Write data to Excel workbook

    # Find and click the 'Next' button
    try:
        next_button = browser.find_element(By.CSS_SELECTOR, 'a[rel="next"]')
        next_button.click()
        time.sleep(5)  # Wait for the next page to load
    except NoSuchElementException:
        break  # 'Next' button not found, exit the loop
      
# Save the workbook
wb.save('github_repositories.xlsx')

# Close the browser
browser.quit()








