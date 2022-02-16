from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib3
import argparse

searchterm = 'bananas' # will also be the name of the folder
directory = os.path.join(os.getcwd(),'bananas')
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
# NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome()
browser.get(url)
header={'User-Agent':"Chrome/83.0.4103.39"}
counter = 0
succounter = 0

if not os.path.exists(directory):
    os.mkdir(directory)

for _ in range(500):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print("Total Count:{}".format(counter))
    print("Succsessful Count:{}".format(succounter))
    print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    try:
        req = urllib3.Request(img, headers={'User-Agent': header})
        raw_img = urllib3.urlopen(req).read()
        File = open(os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype), "wb")
        File.write(raw_img)
        File.close()
        succounter = succounter + 1
    except:
            print("can't get img")

browser.close()