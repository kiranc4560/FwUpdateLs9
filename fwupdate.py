import unittest
import time
from datetime import datetime
from selenium import webdriver
from FwUpdate_sub import FwUpdate
import ipfwversion 
import logging


class TestStringMethods(unittest.TestCase):
    tm=datetime.now().strftime("%m-%d-%Y %H%M%S")
    logging.basicConfig(filename="logs\main"+tm+".log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    
    def setUp(self):
        try:
            self.serial_obj = ipfwversion.configure_serialport('COM4', 115200)
            self.serial_obj.open()
            logging.debug(f'Device ReadLog Thread Started.')
            logging.info(f"Configuring Serial port done")
            print(f"Configuring Serial port done")
            logging.debug(f"Configuring Serial port done")
        except Exception as e:
            print(f'{e}\n error in creating the serialport\n')
            logging.error(f'Error in creating the serialport\n')
            logging.error(e)
            logging.info(f'\t\t\t\t -------- END --------')
            exit(1)
        ipfwversion.updatefwversion(self.serial_obj)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://"+ipfwversion.getIpAddress(self.serial_obj)+"/index.asp")
        time.sleep(10)
        
    def test_FwUpdate(self):
        
        FwUpdate(self.driver)
        time.sleep(5)
        
        
        
    def tearDown(self):
        time.sleep(20)
        self.serial_obj.close()    
        self.driver.quit()
  
  
if __name__ == '__main__':
    for _ in range(1, 5):
        unittest.main()