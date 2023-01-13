from ast import parse
import os
import argparse


#Configurations that could be read on the file
wslVersion = ""
kernel = ""
memory = ""
processors = ""
localhostForwarding = ""
kernelCommandLine = ""
swap = ""
swapFile = ""
pageReporting = ""
guiApplications = ""
debugConsole = ""
nestedVirtualization = ""
vmldleTimeout = ""

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="Echo the string you use here")



#print("Searching for .wslconfig file...")

#try:
#    file = open(os.environ['USERPROFILE']+'/.wslconfig', mode='r')
#    print("Config file found, reading configurations")
#    line = file.readline()
#    while line:
#       
#        line = file.readline()
#    
#    file.close()
#
#
#except FileNotFoundError:
#    print("Config file is not found, creating one...")
#    file = open(os.environ['USERPROFILE']+'/.wslconfig', mode='w+')