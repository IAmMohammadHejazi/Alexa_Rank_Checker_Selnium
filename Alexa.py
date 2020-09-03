# Alexa Rank Checker By Selenium
# Import | Any Website To Input
# MohamadReza Hassani
# Pythoniha.ir

# Import Module's
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Select Chrome # Chrome Version 85.0.0
driver = webdriver.Chrome('chromedriver')

# Alexa.com URL For Ranking Site's
driver.get("https://www.alexa.com/siteinfo/")

# Input Your URL 
url_ = input('Please Enter Site For Checking Rank  :  ')

# Fing Element For Enter Ranking URL !
site = driver.find_element_by_id("input-site")

site.send_keys(url_)
site.send_keys(Keys.ENTER)

time.sleep(10)
rank_Global = driver.find_element_by_css_selector("body.SiteInfo.noWidget:nth-child(2) div.body-container:nth-child(3) div.alx-top section.alx-content div.row-fluid section.fullWidth div.row-fluid.AlexaTool.siteinfo.MinHeight:nth-child(3) div.rest.BigContained.padding div.row-fluid.FullState:nth-child(3) div.MainPage section.CardContainer:nth-child(3) div.ACard.Half.rank:nth-child(1) section.rank div.rank-global div:nth-child(1) div:nth-child(2) > p.big.data")
rank_Con = driver.find_element_by_css_selector("body.SiteInfo.noWidget:nth-child(2) div.body-container:nth-child(3) div.alx-top section.alx-content div.row-fluid section.fullWidth div.row-fluid.AlexaTool.siteinfo.MinHeight:nth-child(3) div.rest.BigContained.padding div.row-fluid.FullState:nth-child(3) div.MainPage section.CardContainer:nth-child(3) div.ACard.Half.rank:nth-child(1) section.countryrank div.Half:nth-child(1) div.row-fluid div.CountryRank.minTablet p.small.data > span.num")

print('Global Rank : ', rank_Global.text)
print('Country Alexa Rank :  ', rank_Con.text)
