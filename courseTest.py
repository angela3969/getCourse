#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:31:41 2022

@author: angela
"""

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def getCourse(keyword):
    driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

    driver.get('https://querycourse.ntust.edu.tw/querycourse/#/');

    #time.sleep(5) # Let the user actually see something!
    ActionChains(driver).move_by_offset(1000, 100).click().perform() 
    time.sleep(2)
    search_class = driver.find_element_by_xpath('//*[@id="app"]/div[12]/main/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div/input') #找到輸入帳號的位置 並先記錄之後要input
    search_class.send_keys(keyword) 
    search_class.send_keys(Keys.ENTER)

    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "lxml")
        
    table = soup.find("table",class_="v-datatable v-table theme--light")
    elements = table.find_all("tr")
    i=0
    courses = []
    for element in elements:
        data_name = element.find_all("td")
        if(i>1):
            #print(getCourseInfo(data_name))
            courses.append(getCourseInfo(data_name))
        i+=1
    return(courses)        
        
def getCourseInfo(data):
    courseId = data[0]
    courseName = data[2]
    professor = data[6]
    notice = data[10]
    courseInfo = [courseId,courseName,professor,notice]
    #courseInfo[0] = (courseId.split('<td>'))[1]
    return courseInfo
    
    
    
getCourse('python')