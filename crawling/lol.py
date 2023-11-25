import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
# def lol_find(nickname):
urls = "https://www.op.gg/summoners/kr/%EA%B8%8D%EC%A0%95%EC%99%95%EC%97%84%EC%84%9D%EB%8C%80-KR1"

browser.get(urls)
time.sleep(1)

soup = BeautifulSoup(browser.page_source, "lxml")
name = soup.find("div", attrs = {"class" : "css-ao94tw elswkqyql"})
tier = soup.find("div", attrs = {"class" : "tier"})
kda = soup.find("div", attrs = {"class" : "k-d-a"})

print(name.text, tier.text, kda.text)

