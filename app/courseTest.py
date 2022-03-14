#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:31:41 2022

@author: angela
"""

import os
import time
import lxml
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def getCourse(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless") #無頭模式
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    #driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

    driver.get('https://querycourse.ntust.edu.tw/querycourse/#/')
    driver.maximize_window()   
    driver.set_window_size(1000, 900)  

    #time.sleep(5) # Let the user actually see something!
    ActionChains(driver).move_by_offset(500, 400).click().perform() 
    time.sleep(2)
    search_class = driver.find_element_by_xpath('//input[@aria-label="課程名稱"]') #找到輸入帳號的位置 並先記錄之後要input
    search_class.send_keys(keyword) 
    search_class.send_keys(Keys.ENTER)

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "lxml")
        
    table = soup.find("table",class_="v-datatable v-table theme--light")
    #print(table)
    elements = table.find_all("tr")
    #print(elements)
    i=0
    courses = {}
    for element in elements:
        data_name = element.find_all("td")
        if(i>1):
            #print(getCourseInfo(data_name))
            courses['course'+str(i)]=str(getCourseInfo(data_name))
        i+=1
    print(courses)
    return(courses)        
        
def getCourseInfo(data):
    courseId = data[0]
    courseName = data[2]
    professor = data[6]
    notice = data[10]
    courseInfo = [courseId,courseName,professor,notice]
    #courseInfo[0] = (courseId.split('<td>'))[1]
    return courseInfo
    
    
    
#getCourse('python')
