# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 21:00:44 2022

@author: ryan
"""
import selenium
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import bs4
import numpy as np
import pandas as pd
import requests
import re
import urllib

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import xlwt

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'x-api-source': 'pc',
    'referer': f'https://www.the-citizenry.com/collections/shop-all-bedding'
}
categories=['shop-all-rugs','shop-all-bedding','shop-all-pillows','all-wall-art','shop-all-furniture','shop-all-decor','shop-all-bath','shop-all-kitchen']
path="D:/chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
rugURL='https://www.the-citizenry.com/collections/shop-all-bedding'  
driver.get(rugURL)
#search for all products 
search=driver.find_elements_by_class_name('w-full.mt-12.flex.justify-between.flex-wrap')
for title in search:
    print(title.text)
#search all links of products in category
product=driver.find_elements(By.XPATH,'//a[@class="tc-product-list__title tc-header-xs uppercase text-left hover:text-grey pr-12"]')
len(product)
URL=[]
for i in range(len(product)):
    URL.append(product[i].get_attribute('href'))

time.sleep(5)
driver.close()
#get product information
#settings
path="D:/chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
driver.get(URL[0]) 
data=requests.get(URL[0])
html=bs4.BeautifulSoup(data.text,"html")
#name of product
name=html.find('h1').getText()
#ratings

try:

    ratings=driver.find_element_by_class_name('stamped-badge').get_attribute('data-rating')
except:
    ratings='none'

#colors&patterns
        
try:
                colors=driver.find_elements_by_css_selector('ul[class="tc-product__details"]>li:nth-child(4)>div>p')
                Color=[]
                for col in colors:
                    Color.append(col.text)
                Color_string= "\n".join(Color)
except:
                Colors=[]
                colors=driver.find_elements(By.XPATH,'//button[@data-stage="js-selected-color-classic"]')+driver.find_elements(By.XPATH,'//button[@data-stage="js-selected-color-limited"]')
                for color in range(len(colors)) :
                    Colors.append(colors[color].get_attribute('data-title'))
                Color_string = "\n".join(Colors)
                Color_string
                colors  

#measurements
Size=[]
size_list= driver.find_elements_by_css_selector('ul[class="tc-product-form__size-list mb-6 mt-24 lg:mt-6 flex-wrap justify-between flex"] > li > button')
for size in size_list:
    Size.append((size).text)
Size_string = "\n".join(Size)
Size_string
#price_list
if len(Size)==0:
     price=driver.find_element_by_class_name("js-product-price.tc-p-lg").text

else: 
    price=[]
    for size in size_list:
        driver.execute_script('arguments[0].click();', size)
        price.append(driver.find_element_by_class_name('js-product-price.tc-p-lg').text)
#origin
origin=driver.find_elements(By.XPATH,'//label[@class="tc-product-form__origin center tc-subheader text-center lg:text-left"]')[0].text
origin
#status
try:
    status=driver.find_element_by_css_selector('label[class="flex items-center justify-center tc-product-form__availability"]>span').text
    if status=="":
     status='Join waitlist'
except: 
        status="Join Waitlist"
status
#Materials
labels=driver.find_elements_by_css_selector('ul[class="tc-product__details"]>li:nth-child(3)>div>p')
materials=[]
for label in labels:
    materials.append(label.text)
Materials= "\n".join(materials)
driver.quit

# get all URL of the products
Bath=[]
URL=[]
categories=['shop-all-rugs','shop-all-bedding','shop-all-pillows','all-wall-art','shop-all-furniture','shop-all-decor','shop-all-bath','shop-all-kitchen']
for cat in categories:
    path="D:/chromedriver.exe"
    s=Service("D:/chromedriver.exe")
    driver=webdriver.Chrome(service=s)
    rugURL='https://www.the-citizenry.com/collections/shop-all-bath'  
    driver.get(rugURL)
    time.sleep(5)
    #search all links of products in category
    product=driver.find_elements(By.XPATH,'//a[@class="tc-product-list__title tc-header-xs uppercase text-left hover:text-grey pr-12"]')
    time.sleep(5)
    len(product)
    for i in product:
       Bath.append(i.get_attribute('href'))
    
    driver.close()
len(URL)
URL
#all items information
for urls in range(len(URL)):
    path="D:/chromedriver.exe"
    driver=webdriver.Chrome(executable_path=path)
    rugURL='https://www.the-citizenry.com/collections/'  
    driver.get(URL[i])

# 定義Crawl_SongGuo函數，輸入商品網址，輸出該商品的各項屬性
def ProductDataframe(info):
    path="D:/chromedriver.exe"
    driver=webdriver.Chrome(executable_path=path)
    driver.get(info) 
    driver.implicitly_wait(5)
    data=requests.get(info)
    html=bs4.BeautifulSoup(data.text,"html")
    #name of product
    name=html.find('h1').getText()
    #ratings
    try:
        ratings=driver.find_element_by_class_name('stamped-badge').get_attribute('data-rating')
    except:
        ratings='none'
    #colors&patterns
            
    try:
        colors=driver.find_elements_by_css_selector('ul[class="tc-product__details"]>li:nth-child(4)>div>p')
        Color=[]
        for col in colors:
            Color.append(col.text)
        Color_string= "\n".join(Color)
    except:
        Colors=[]
        colors=driver.find_elements(By.XPATH,'//button[@data-stage="js-selected-color-classic"]')+driver.find_elements(By.XPATH,'//button[@data-stage="js-selected-color-limited"]')
        for color in range(len(colors)) :
            Colors.append(colors[color].get_attribute('data-title'))
        Color_string = "\n".join(Colors)
        Color_string
        colors  
   
    #measurements
    try:
        size=driver.find_elements_by_css_selector('ul[class="tc-product__details"]>li:nth-child(2)>div>p')
        Size=[]
        for s in size:
           Size.append(s.text)
        Size_string = "\n".join(Size)    
    except:
        Size=[]
        size_list= driver.find_elements_by_css_selector('ul[class="tc-product-form__size-list mb-6 mt-24 lg:mt-6 flex-wrap justify-between flex"] > li > button')
        for size in size_list:
                Size.append((size).text)
        Size_string = "\n".join(Size)
            
    
    #price_list
    if len(Size)<=1:
         price=driver.find_element_by_class_name("js-product-price.tc-p-lg").text
    
    else: 
        price=[]
        size_list= driver.find_elements_by_css_selector('ul[class="tc-product-form__size-list mb-6 mt-24 lg:mt-6 flex-wrap justify-between flex"] > li > button')
        for size in size_list:
            driver.execute_script('arguments[0].click();', size)
            price.append(driver.find_element_by_class_name('js-product-price.tc-p-lg').text)
    #origin
    try:
       origin=driver.find_elements(By.XPATH,'//label[@class="tc-product-form__origin center tc-subheader text-center lg:text-left"]')[0].text
    except:
          Ori=driver.find_elements_by_css_selector('ul[class="tc-product__details"]>li:nth-child(5)>div>p')
          Origin=[]
          for o in Ori:
               Origin.append(o.text)
          origin = "\n".join(Size)
        
    #status
    try:
        status=driver.find_element_by_css_selector('label[class="flex items-center justify-center tc-product-form__availability"]>span').text
        if status==" ":
            status='Out of Stock'
    except: 
        status="Join Waitlist"
    #Materials
    try:
        labels=driver.find_elements_by_css_selector('ul[class="tc-product__details"]>li:nth-child(3)>div>p')
        materials=[]
        for label in labels:
            materials.append(label.text)
        Materials= "\n".join(materials)
    except:
        Materials='unknown'
    driver.quit()

    return(pd.DataFrame(
            data=[{
                'Product Name':name,
                'Origin':origin,
                'Measurements':Size_string,
                'Price':price,
                'Ratings':ratings,
                'Status':status,
                'Color and Patterns':Color_string,               
                'Materials':Materials,
                'URL': info , }],
            columns = ['Product Name', 'Origin', 'Measurements', 'Price', 'Ratings',  'Status', 'Color and Patterns','Materials','URL']))
#all items information
df = pd.DataFrame()

for urls in range(294,len(URL)):
    
    df = df.append(ProductDataframe(URL[urls]), ignore_index=True)
df   
df.to_csv('D:/product.csv') 
dict={'URL':URL}  
u=pd.DataFrame(dict)
u.to_csv('D:/u.csv')

URLss=[]
Categories=[]
Cat=['Rugs','Bedding','Pillows & Throws','Mirrors & Wall Art','Furnitures','Basket & Decor','Bath','Kitchen']
categories=['shop-all-rugs','shop-all-bedding','shop-all-pillows','all-wall-art','shop-all-furniture','shop-all-decor','shop-all-bath','shop-all-kitchen']
for cat in categories:
    path="D:/chromedriver.exe"
    s=Service("D:/chromedriver.exe")
    driver=webdriver.Chrome(service=s)
    rugURL='https://www.the-citizenry.com/collections/'  
    driver.get(rugURL+str(cat))
    time.sleep(5)
    #driver.implicitly_wait(10)
    #search all links of products in category
    product=driver.find_elements(By.XPATH,'//a[@class="tc-product-list__title tc-header-xs uppercase text-left hover:text-grey pr-12"]')
    time.sleep(5)
    len(product)
    for i in product:
       URLss.append(i.get_attribute('href'))
       #Categories.append('Mirrors & Wall Art')
driver.quit()
    
len(URLss)
df2 = pd.DataFrame()
for urls in range(312,len(URLss)):
    
    df2 = df2.append(ProductDataframe(URLss[urls]), ignore_index=True)
df2   
df2.to_csv('D:/product_information.csv')

b = pd.DataFrame()
for urls in range(len(Bath)):
    
    b =b.append(ProductDataframe(Bath[urls]), ignore_index=True)
b   
b.to_csv('D:/ath.csv')
