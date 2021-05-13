'''For downloading important attributes or txt content from HTML we have to import esential libraries.
Also it is important to install and add path to chrome webdriver from: 
https://selenium-python.readthedocs.io/installation.html
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

'''Add path to a chromedriver with which python will cooperate '''
driver = webdriver.Chrome("D:/webdriver/chromedriver.exe")

'''Add arrays where you would like to append final result. For us it
was company names and their pledges'''
company_names = []
pledges = []

'''Add URL for the python from witch you want to extract data'''
driver.get("https://www.wemeanbusinesscoalition.org/companies/#!")
content = driver.page_source
soup = BeautifulSoup(content)

'''Extract what you need and append it to an arrays above, in our case, we were looking for all 
"li" tags with classes:"js-hidden-state" or "js-visible-state", from those we wanted to find the
names of companies which were placed always in li's child "a" tag with class:"lightbox" and at the same time
we wanted to extract pledges for this company which were placed in li's attribute:"data-options"'''
for li in soup.findAll('li', attrs={'class': ('js-hidden-state' or 'js-visible-state')}):
    name = li.find('a', attrs={'class': 'lightbox'})
    pledges.append(li.get("data-options"))
    company_names.append(name.text)
    
'''Adding head to .csv file and also important content under it'''
df = pd.DataFrame({'CompNames': company_names, 'Pledges': pledges})

'''Adding path and filename for final output'''
df.to_csv('D:/Desktop/HTMLscrapper/allin.csv', index=False, encoding='utf-8', sep='|')

print("Success!!!")
