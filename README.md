# <ins>Web Scraping Practice with Instagram and GitHub</ins>

Have you ever felt lost in the endless world of GitHub repositories or puzzled by Instagram connections? with GitHub Repository 
Scraper we will navigate through the repositories on GitHub, making it easier to find valuable resources. Meanwhile, 
Instagram Non-Follower Finder will give insights of social media connections by identifying non-followers

These are unofficial ways to interact with these websites you can also check both [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28) & [Instagram’s API](https://developers.facebook.com/products/instagram/apis/) through these links.

* In the [`Web_Scraping_IMDB_Most_Popular_Movies`](https://github.com/yavuzCodiin/Web_Scraping_IMDB_Most_Popular_Movies) I explained basic html structure you can go and check how website is built and how we can interact with it.

* In the [`Web Scraping X Feed Selenium`](https://github.com/yavuzCodiin/Web_Scraping_X_Feed_Selenium) I explained handling dynamic web content with `selenium`, enabling us to extract valuable data from one of the world's most active online communities, you can check how can you use selenium to interact with dynamic content.

## <ins>GitHub Repository Scraper</ins>

![image](https://github.com/yavuzCodiin/Web_Scraping_Practice_w_Instagram_and_GitHub/assets/82445309/5b5f966e-6e04-4622-a4f2-b702bc13b29b)

## | <ins>Importing Libraries</ins>
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
```

## | <ins>Function to Initialize Things We Need and Enter GitHub</ins>
```python
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
```

## | <ins>Function to find Search Area and Send Search Input</ins>

* You can change search input according to your needs.

```python
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
```

## | <ins>Search Repositories Through Pages and Write Data to Excel</ins>
```python
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
```

## | <ins>Save Excel Workbook and Close the Browser</ins>
```python
# Save the workbook
wb.save('github_repositories.xlsx')

# Close the browser
browser.quit()
```

First I have done this process by saving data to text file which you can guess it was messy then I tried to save the data into excel workbook which is much better.

![image](https://github.com/yavuzCodiin/Web_Scraping_Practice_w_Instagram_and_GitHub/assets/82445309/94284a05-3783-434a-b717-db38291bdd3a)

![image](https://github.com/yavuzCodiin/Web_Scraping_Practice_w_Instagram_and_GitHub/assets/82445309/7a3f78ed-95ce-48d4-9110-772fa3f5211a)

## <ins>Project Video</ins>

[![Project Git Scraper](https://img.youtube.com/vi/zA_kMK6cJtA/0.jpg)](https://www.youtube.com/watch?v=zA_kMK6cJtA "Project Git Scraper")

## <ins>Instagram Non-Follower Finder</ins>

![image](https://github.com/yavuzCodiin/Web_Scraping_Practice_w_Instagram_and_GitHub/assets/82445309/2ea401b4-4af2-4551-a5f5-bc22d281178c)

## | <ins>Importing Libraries</ins>
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
```

## | <ins>Initialize Things We Need and Enter Instragram</ins>
```python
browser = webdriver.Chrome()
actions = ActionChains(browser)

username_text = "Username"
password_text = "Password"

#Initialize Excel Workbook
wb = openpyxl.Workbook()
ws = wb.active

# Column Headers
ws.append(['Followers', 'Following', 'Non-Followers'])

browser.get("https://www.instagram.com/")

time.sleep(2)

username = browser.find_element(By.NAME, "username")
password = browser.find_element(By.NAME, "password")

username.send_keys(username_text)
time.sleep(5)
password.send_keys(password_text)
time.sleep(3)
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(10)

save_info = browser.find_element(By.TAG_NAME, "button")
save_info.click()

time.sleep(20)

# Using XPath to find the button by its text
turn_on_button = browser.find_element(By.XPATH, "//button[text()='Not Now']")
turn_on_button.click()

time.sleep(5)
```

## | <ins>Open Followers Section and Scroll down Until the End</ins>
```python
browser.get("https://www.instagram.com/{}/followers/".format(username_text))
time.sleep(15)

#The following variable is for scrolling down 
jscommand = """
followers = document.querySelector("._aano");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommand)

match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
```

## | <ins>Find Followers and Store Them in followersList</ins>
```python
followersList = []

html_content = browser.page_source
soup = BeautifulSoup(html_content, 'html.parser')

follower_elements = soup.find_all('span', class_='_ap3a _aaco _aacw _aacx _aad7 _aade')

for follower in follower_elements:
    followersList.append(follower.text)
print("Followers: {}".format(followersList))
```

## | <ins>Open Following Section and Scroll down Until the End</ins>
```python
browser.get("https://www.instagram.com/{}/following/".format(username_text))
time.sleep(15)
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
```

## | <ins>Find Following and Store Them in followingList</ins>
```python
html_content = browser.page_source
soup = BeautifulSoup(html_content, 'html.parser')

following_elements = soup.find_all('span', class_='_ap3a _aaco _aacw _aacx _aad7 _aade')

for following in following_elements:
    followingList.append(following.text)
print("Following: {}".format(followingList))
```

## | <ins>Find Non-Followers and Store Them in not_follower</ins>
```python
follows = set(followersList)
following = set(followingList)
not_follower = following.difference(follows)
```

## | <ins>Write Data to Excel</ins>
```python
# Writing to Excel

# Write Followers
row = 1  # Start from the second row (first row is for headers)
for follower in followersList:
    ws.cell(row=row, column=1, value=follower)
    row += 1

# Write Following
row = 1  # Reset row for following
for follow in followingList:
    ws.cell(row=row, column=2, value=follow)
    row += 1

# Write Non-Followers
row = 1  # Reset row for non-followers
for non_follow in not_follower:
    ws.cell(row=row, column=3, value=non_follow)
    row += 1
```

## | <ins>Save Excel Workbook and Close the Browser</ins>
```python
wb.save('non_follower.xlsx')     
          
browser.close()
```

## <ins>Project Video</ins>

[![Project Insta Non-Follower Scraper](https://img.youtube.com/vi/7tEgIswbPF0/0.jpg)](https://www.youtube.com/watch?v=7tEgIswbPF0 "Project Insta Non-Follower Scraper")

If you want to understand this in a more simpler language you can check my Medium writing published on `Level Up Coding`

LINK => 







