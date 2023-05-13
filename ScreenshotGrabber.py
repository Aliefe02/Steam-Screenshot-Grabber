import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def GetScreenshotLink(ID):
    return "https://steamcommunity.com/profiles/"+ID+"/screenshots/"

def GetScreenshots(ID):
    ScreenshotList = []
    options = Options()
    browser = webdriver.Chrome(options=options)
    url = GetScreenshotLink(ID)
    browser.get(url)
    i = 0
    while i<10:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)   
        i += 1

    i = 0
    soup = BeautifulSoup(browser.page_source,features="lxml")
    browser.close()
    for link in soup.findAll('a'):
        if "https://steamcommunity.com/sharedfiles/filedetails" in link.get("href"):
            FullPhoto = requests.get(link.get('href'))
            soupPhoto = BeautifulSoup(FullPhoto.text,features="lxml")
            for PhotoLink in soupPhoto.findAll('a'):
                if "https://steamuserimages-a.akamaihd.net/ugc" in PhotoLink.get('href'):
                    i += 1
                    #print(PhotoLink.get('href'))
                    ScreenshotList.append(PhotoLink.get('href'))
                    break
    #print(str(i)+" Screenshots Are Found!")
    return ScreenshotList