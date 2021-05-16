import re
import logging
import subprocess
import os
import configparser
import time
import socket
import sys 

nowtime = time.strftime('%Y%m%d')
config = configparser.ConfigParser()
inoutClientService = 'c:\\program files\\xyz.exe'

hostUserName = socket.gethostname()
hostIP = socket.gethostbyname(hostUserName)

def main():#directoryArg):
    directoryArg = 'c:\\code\\python\\inout\\'

    #capture login details
    inputStr = input('Enter UserName,Password : ')
    inputStr = re.split(',', inputStr)
    if not (len(inputStr) == 2):
        print ('enter username and password with , seperator')
        return
    else:
        applicationUserName = inputStr[0]
        applicationPassword = inputStr[1]

    #read ini file
    currDirectory = directoryArg + '\\'
    if not (os.path.exists(currDirectory + 'config.ini')):
        print ('config.ini file not found!')
        return
    else:
        print ('reading configurations ...')
        config.read(f'{currDirectory}config.ini')

    modules = config.get('modules','modules')
    modules = re.split('\n', modules)

    portfolios = config.get('portfolios','portfolios')
    portfolios = re.split('\n', portfolios)

    #create working, output and logging directories
    workingDirectory = f'{currDirectory}{nowtime}\\'
    if not (os.path.exists(workingDirectory)):
        os.mkdir(workingDirectory)

    outputDirectory = f'{workingDirectory}output\\'
    if not (os.path.exists(outputDirectory)):
        os.mkdir(outputDirectory)

    loggingDirectory = f'{workingDirectory}log\\'
    if not (os.path.exists(loggingDirectory)):
        os.mkdir(loggingDirectory)

    #set up log file
    logging.basicConfig(filename=f'{loggingDirectory}applog.log', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.getLogger()
    logging.info(f'*** process started by user:{hostUserName}, IP:{hostIP} applicationUser:{applicationUserName} ***')





    logging.info('*** process complete ***')


def CheckApplicationLogFileDoeErrors(fileLocation):

    logfile = open(fileLocation, 'r')
    for line in logfile:
        if re.match(' E ', line):
            return True
    
    return False



if __name__ == '__main__':
    #main(sys.argv[1])
    main()
