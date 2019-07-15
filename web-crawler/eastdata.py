# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import xlwt
import xdrlib
import sys





    

if __name__ == "__main__":

        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("Data")

        myProxy = "jpyoip01.mgmt.ericsson.se:8080"
        fp = webdriver.FirefoxProfile()
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.http", "150.236.159.44")
        fp.set_preference("network.proxy.http_port", "8080")
        fp.set_preference("network.proxy.socks", "150.236.159.44")
        fp.set_preference("network.proxy.socks_port", "8080")
        fp.update_preferences()
       
        driver = webdriver.Firefox(firefox_profile=fp)
        driver.implicitly_wait(10)
        base_url = "http://data.eastmoney.com"
        verificationErrors = []
        accept_next_alert = True
        
    
        driver.get("http://data.eastmoney.com/rzrq/total.html")

        #time.sleep(2)
        #print driver.page_source
     
        row_index = 0 

        page = 1 
        while page  < 16:
             print page 
             page = page + 1

             rows = driver.find_elements_by_xpath("id('dt_1')/tbody/tr");
             print len(rows)
             for  row in rows:
                col_index = 0
                txt = ""
                cols = row.find_elements_by_xpath("td");
                for col in cols:
                   txt = txt +  col.text
                   worksheet.write(row_index, col_index, col.text)
                   col_index = col_index + 1
                row_index = row_index + 1
                print txt
             driver.find_element_by_link_text(u"下一页").click()

        workbook.save('all_data.xls') 
        #driver.find_element_by_link_text(u"下一页").click()
        #driver.find_element_by_link_text(u"下一页").click()
        #driver.find_element_by_link_text(u"下一页").click()
        #driver.find_element_by_link_text(u"下一页").click()
        #driver.find_element_by_link_text(u"下一页").click()
        #driver.find_element_by_link_text(u"下一页").click()
        #driver.find_element_by_link_text(u"下一页").click()
    
        driver.quit()

