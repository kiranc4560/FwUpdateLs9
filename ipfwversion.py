import logging
import serial
import time

comport='COM4'
baudrate= 115200
def configure_serialport(portnumber, baudrate):
    #logging.info(f"Configuring Serial port {portnumber} with Baudrate {baudrate}")
    print(f"Configuring Serial port {portnumber} with Baudrate {baudrate}")
    serialport = serial.Serial()
    serialport.baudrate = baudrate
    serialport.port = portnumber
    serialport.bytesize = serial.EIGHTBITS
    serialport.parity = serial.PARITY_NONE
    serialport.stopbits = serial.STOPBITS_ONE
    # serialport.timeout = 1
    serialport.rtscts = False
    serialport.dsrdtr = False
    serialport.xonxoff = False
    return serialport   

def getfwversion(serial_obj):
    serial_obj.write(b'getenv FwVersion\r\n')
    logging.debug(f'Sent  getenv FwVersion through Serial port.')
    while True:
        readdata=serial_obj.readline().decode('utf-8')
        if 'ENV: Value found FwVersion :' in readdata:
            fwversion=readdata.split(':')[2]
            logging.debug(f'Latest FwVersion is : {fwversion}.')
            return fwversion.strip()
            
def updatefwversion(serial_obj):
    current_fwVersion=getfwversion(serial_obj)
    update_version=int(current_fwVersion[1:])-10
    time.sleep(0.5)
    logging.debug(f'updated FwVersion to : {update_version}.')
    ex_version='p'+str(update_version)
    update_fwversion='setenv FwVersion'+' '+ex_version+'\r\n'
    serial_obj.write(update_fwversion.encode('utf-8'))
    time.sleep(0.5)           
            
def getIpAddress(serial_obj):
    serial_obj.write(b'netcfg\r\n')
    logging.debug(f'Sent netcfg.')
    while True:
        readdata=serial_obj.readline().decode('utf-8')
        if 'wlan0    UP' in readdata:
            ipaddress=readdata.split(' ')
            ipaddress=ipaddress[-4].split('/')
            logging.debug(f'IPaddress {ipaddress[0]}.')
            return ipaddress[0]


def logcat(serial_obj):
    while True:
        logcat ='logcat &\r\n'
        serial_obj.write(logcat.encode('utf-8'))
        print(readline().decode('utf-8'))
        time.sleep(0.5)  
                    
def main():
    try:
        serial_obj = configure_serialport(comport, baudrate)
        serial_obj.open()
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
        
    
    

    
    

        
if __name__=='__main__':
    main()