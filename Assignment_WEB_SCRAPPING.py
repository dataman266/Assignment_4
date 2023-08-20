#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[28]:


from bs4 import BeautifulSoup
import requests


# In[7]:


page = requests.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[8]:


page


# In[9]:


soup = BeautifulSoup(page.content)
soup


# In[11]:


table = soup.find('table', {'class': 'wikitable'})


# In[14]:


# Extract rows from the table
rows = table.findAll('tr')[1:]  # skip the header row


# In[16]:


data = []

for row in rows:
    cells = row.findAll('td')
    if len(cells) >= 5:  # Check if there are at least 5 <td> elements in the row
        rank = cells[0].text.strip()
        name = cells[1].text.strip()
        artist = cells[2].text.strip()
        views = cells[3].text.strip()
        upload_date = cells[4].text.strip()

        data.append([rank, name, artist, upload_date, views])
    else:
        print(f"Unexpected row format: {row}")

print(data)


# In[17]:


page2 = requests.get('https://www.bcci.tv/')
page2


# In[18]:


soup = BeautifulSoup(page2.content)
soup


# In[4]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[5]:


driver = webdriver.Chrome()


# In[34]:


# Go to BCCI website
driver.get('https://www.bcci.tv/')


# In[36]:


try:
    # Click the cookie accept or close button (you might need to adjust the selector)
    cookie_button = driver.find_element(By.CSS_SELECTOR, ".cookie-accept-button-class")
    cookie_button.click()
except Exception as e:
    print("Error clicking cookie notice:", e)


# In[37]:


# Navigate to the International Fixtures page (this step might need adjustments based on website structure)
fixtures_link = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/ul/li[1]/a")
fixtures_link.click()


# In[38]:


# Get page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')


# In[69]:


# Find all matches (this step might need adjustments based on website structure)
matches = []
for i in soup.find_all('div', class_="match-card-top"):
    matches.append(i.text)


# In[70]:


matches


# In[67]:


match_title = []
for i in soup.find_all('h5', class_="match-tournament-name ng-binding"):
    match_title.append(i.text)


# In[68]:


match_title


# In[66]:


place = []
for i in soup.find_all('span', class_="ng-binding ng-scope"):
    place.append(i.text)
place


# In[65]:


date = []
for i in soup.find_all('div', class_="match-dates ng-binding"):
    date.append(i.text)
date


# In[71]:


time = []
for i in soup.find_all('div', class_="match-time no-margin ng-binding"):
    time.append(i.text)
time


# In[29]:


page4 = requests.get('https://www.statisticstimes.com/')
page4


# In[30]:


soup = BeautifulSoup(page4.content)
soup


# In[49]:


drivr = webdriver.Chrome()


# In[50]:


driver.get('https://www.statisticstimes.com/')


# In[51]:


economy_link = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/button")
economy_link.click()


# In[52]:


india = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
india.click()


# In[53]:


states = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
states.click()


# In[54]:


# Get page source and parse it with BeautifulSoup
soup1 = BeautifulSoup(driver.page_source, 'html.parser')


# In[55]:


rank = []
for i in soup.find_all('id', class_="display dataTable"):
    rank.append(i.text)


# In[56]:


rank


# In[ ]:





# In[ ]:





# In[114]:


drivr.close()


# In[72]:


driver = webdriver.Chrome()


# In[ ]:


driver.get('https://billboard.com')


# In[ ]:


charts = driver.find_element(By.XPATH, '/html/body/div[4]/div[9]/div/div/div/ul/li[1]/h3/a')
charts.click()


# In[119]:


hot_100 = driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/span/a')
hot_100.click()


# In[134]:


song = []
for i in soup.find_all('h3', class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"):
    song.append(i.text)
song


# In[129]:


abc = driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div[2]/ul/li[4]/ul/li[1]/h3')
abc


# In[131]:


abc.content()


# In[135]:


name = []
for i in soup.find_all('span', class_="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"):
    name.append(i.text)
name


# In[62]:


driver = webdriver.Chrome()


# In[63]:


driver.get('https://github.com')


# In[66]:


button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[1]/div[2]/button')
button.click()


# In[68]:


button1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
button1.click()


# In[ ]:





# In[71]:


trend = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/span')
trend.click()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




