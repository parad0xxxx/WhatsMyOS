'''imports'''
import platform # this library is used to get computer stats
import os # this library is used to gather the computer username

program_name = "What's My OS" # project name
username = os.path.expanduser('~').split('\\')[2] # computer username
os = platform.system() # OS (windows, mac, linux)
node = platform.node() # gets name of computer connected to internet
creator = 'Parad0x' # the creator of this project
arch = platform.architecture()[0] # gets OS architecture (32-bit, 64-bit)
pro = platform.processor() # gets processors
release = platform.release() # gets OS update

print('---------------------------------------')
print('Welcome ' + username + ' to ' + program_name + '!') # welcomes computer username to program name
print('---------------------------------------')
print('Lets Start!\n')
print("• Your computer is running:\n " + os) # prints OS type
print("• Your architecture is:\n " + arch) # prints architecture type
print("• Your OS release is:\n " + os + ' ' + release) # prints OS release (update)
print("• Your network name is:\n " + node) # prints name of computer connected to internet
print("• Your processors are:\n " + pro) # prints computer processors
print("Thanks for using " + program_name + " this was made by " + creator) # finishes off with the name of the program, and the creator of it.
