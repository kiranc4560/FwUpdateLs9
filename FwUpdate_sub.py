import os
import logging
import serial
import time
import ipfwversion 
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

tm=datetime.now().strftime("%m-%d-%Y %H%M%S")
logging.basicConfig(filename="logs\FwUpdate_sub"+tm+".log",
                    format='%(asctime)s %(message)s',
                    filemode='w')


current_dir=os.getcwd()

def check_update(driver):
    driver.find_element_by_xpath('//input[@value="Update"]').click()
    firmware_page=WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, "//h2")))
    print(firmware_page.text)
    New_ls9image=driver.find_element_by_xpath('//table/tbody/tr[3]/td[3]').text
    time.sleep(1)
    driver.find_element_by_xpath('//input[@type="submit"]').click()
    bigfont=WebDriverWait(driver, 420).until(EC.presence_of_element_located((By.XPATH, "//div[@class='BigFont']")))
    print(bigfont.text)
    time.sleep(60)
    return True
    

def FwUpdate(driver):
    try:
        WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, "//div[@class='BigFont']")))
    except:
        print('Please check the IPAddress/check yout network/check u have connected to same network that the board connected to')
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    update_btn = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.ID, "AdvBtn_UPG")))
    update_btn.click()

    choose_file = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.ID, "fileid")))
    choose_file.send_keys(current_dir+'\image\83_IMAGE_network')
    time.sleep(1)
    check_update(driver)
    
        
        
       
