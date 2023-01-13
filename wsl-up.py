from ast import parse
import sys
import os
import argparse

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

#Searches for wsl.conf file
try:
    #Checks if the path exists in %UserProfile%/.wslconfig
    if os.path.exists(os.environ['USERPROFILE']+"/.wslconfig"):
        print("WSL configuration file found")
        with open(os.environ['USERPROFILE']+"/.wslconfig", "r") as f:
            for line in f.readlines():
                if line.startswith("wslVersion="):
                    wslVersion = line.split("=")[1]
                
                elif line.startswith("kernel="):
                    kernel = line.split("=")[1]
                
                elif line.startswith("memory="):
                    memory = line.split("=")[1]
                
                elif line.startswith("processors="):
                    processors = line.split("=")[1]
                
                elif line.startswith("localhostForwarding="):
                    localhostForwarding = line.split("=")[1]
                
                elif line.startswith("kernelCommandLine="):
                    kernelCommandLine = line.split("=")[1]
                
                elif line.startswith("swap="):
                    swap = line.split("=")[1]
                
                elif line.startswith("swapFile="):
                    swapFile = line.split("=")[1]
                
                elif line.startswith("pageReporting="):
                    pageReporting = line.split("=")[1]
                
                elif line.startswith("guiApplications="):
                    guiApplications = line.split("=")[1]
                
                elif line.startswith("debugConsole="):
                    debugConsole = line.split("=")[1]
                
                elif line.startswith("nestedVirtualization="):
                    nestedVirtualization = line.split("=")[1]
                
                elif line.startswith("vmldleTimeout="):
                    vmldleTimeout = line.split("=")[1]
        
        f.close();
    
    else:
        print("WSL configuration file not found")
        with open(os.environ['USERPROFILE']+"/.wslconfig", "w+") as f:
            f.write("")
            print("WSL configuration file created")

except:
    print("Error while reading the file")
    print("Please check if the file exists in %UserProfile%/.wslconfig")
    print("Error: ", sys.exc_info()[0])

#Configurations that could be read on the file


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="WSL version")
parser.add_argument("-k", "--kernel", help="Kernel version")
parser.add_argument("-m", "--memory", help="Memory limit")
parser.add_argument("-p", "--processors", help="Number of processors")
parser.add_argument("-l", "--localhost", help="Localhost forwarding")
parser.add_argument("-c", "--command", help="Kernel command line")
parser.add_argument("-s", "--swap", help="Swap space")
parser.add_argument("-f", "--file", help="Swap file")
parser.add_argument("-r", "--report", help="Page reporting")
parser.add_argument("-g", "--gui", help="GUI applications")
parser.add_argument("-d", "--debug", help="Debug console")
parser.add_argument("-n", "--nested", help="Nested virtualization")
parser.add_argument("-t", "--timeout", help="VM idle timeout")
args = parser.parse_args()

#Checks if the user wants to change the WSL version
if args.version:
    if args.version == "1" or args.version == "2":
        wslVersion = args.version + "\n"
    else:
        print("Invalid WSL version")
        print("Please use 1 or 2")
    
#Checks if the user wants to change the kernel version
if args.kernel:
    kernel = args.kernel + "\n"

#Checks if the user wants to change the memory limit
if args.memory:
    memory = args.memory + "\n"

#Checks if the user wants to change the number of processors
if args.processors:
    processors = args.processors + "\n"

#Checks if the user wants to change the localhost forwarding
if args.localhost:
    if args.localhost == "true" or args.localhost == "false":
        localhostForwarding = args.localhost + "\n"
    else:
        print("Invalid localhost forwarding")
        print("Please use true or false")
    
#Checks if the user wants to change the kernel command line
if args.command:
    kernelCommandLine = args.command + "\n"

#Checks if the user wants to change the swap space
if args.swap:
    if args.swap == "true" or args.swap == "false":
        swap = args.swap + "\n"
    else:
        print("Invalid swap space")
        print("Please use true or false")

#Checks if the user wants to change the swap file
if args.file:
    swapFile = args.file + "\n"

#Checks if the user wants to change the page reporting
if args.report:
    if args.report == "true" or args.report == "false":
        pageReporting = args.report + "\n"
    else:
        print("Invalid page reporting")
        print("Please use true or false")

#Checks if the user wants to change the GUI applications
if args.gui:
    if args.gui == "true" or args.gui == "false":
        guiApplications = args.gui + "\n"
    else:
        print("Invalid GUI applications")
        print("Please use true or false")

#Checks if the user wants to change the debug console
if args.debug:
    if args.debug == "true" or args.debug == "false":
        debugConsole = args.debug + "\n"
    else:
        print("Invalid debug console")
        print("Please use true or false")

#Checks if the user wants to change the nested virtualization
if args.nested:
    if args.nested == "true" or args.nested == "false":
        nestedVirtualization = args.nested + "\n"
    else:
        print("Invalid nested virtualization")
        print("Please use true or false")

#Checks if the user wants to change the VM idle timeout
if args.timeout:
    vmldleTimeout = args.timeout + "\n"

#Saves all the configurations on the file
with open(os.environ['USERPROFILE']+"/.wslconfig", "w+") as f:
    f.writelines(
        ["wslVersion="+wslVersion+"\n",
        "kernel="+kernel+"\n",
        "memory="+memory+"\n",
        "processors="+processors+"\n",
        "localhostForwarding="+localhostForwarding+"\n",
        "kernelCommandLine="+kernelCommandLine+"\n",
        "swap="+swap+"\n",
        "swapFile="+swapFile+"\n",
        "pageReporting="+pageReporting+"\n",
        "guiApplications="+guiApplications+"\n",
        "debugConsole="+debugConsole+"\n",
        "nestedVirtualization="+nestedVirtualization+"\n",
        "vmldleTimeout="+vmldleTimeout+"\n"]
    )

print("WSL configuration file saved")