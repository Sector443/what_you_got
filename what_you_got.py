from time import sleep
from selenium import webdriver
import httplib2
from os import system, environ
import os.path
import subprocess, shlex
from sys import platform

#Global variable configuration
ip_addr = list()
ouput_file = environ['PWD'] + '/srm_web_servers.txt'
subnet_mask = str('')


class wtyg:
	#Class variables config
	outfile_location = environ['PWD'] + '/srm_web_servers.txt'
	subnet_mask = str('')


	def __init__(self):
		if os.path.exists(self.outfile_location):
			self.banner()
			choice = input('Existing output file found, do you want to see its content? [Y/n]: ')
			if choice == 'Y' or choice == 'y':
				self.menu('3')
			elif choice == 'N' or choice == 'n':
				pass


	def banner(self):
		subprocess.call('clear', shell=True)
		print('\033[1;31;40m ##############################################################')
		print('\ \      / / |__   __ _| |\ \ / /__  _   _ / ___| ___ | ||__ \ ')
		print(" \ \ /\ / /| '_ \ / _` | __\ V / _ \| | | | |  _ / _ \| __|/ / ")
		print('  \ V  V / | | | | (_| | |_ | | (_) | |_| | |_| | (_) | |_|_|  ') 
		print('   \_/\_/  |_| |_|\__,_|\__||_|\___/ \__,_|\____|\___/ \__(_)  ')
		print('\033[1;31;40m ##############################################################')
		print('> Python script to scan entire private subnets on \nSRM University network for port 80 under 20min')
		print("by CJHackerz@$ecTor443Labs:~ \n")


	def menu(self, option):
		if option == '1':
			system('sudo apt install zmap -y')
		elif option == '2':
			self.scan()
			self.show()
		
		elif option == '3':
			self.show()
		
		else:
			print('Alert!, 1nValid option!\n')


	def set_subnet_mask(self):
		print('\n Please choose any one of the private subnet listed below, to perform scan on it... \n')
		print('1.) 10.0.0.0/8 \n')
		print('2.) 172.16.0.0/12 \n')
		print('3.) 192.168.0.0/16 \n')
		choice = input('>')
		
		if choice == '1':
			self.subnet_mask = '10.0.0.0/8'
		elif choice == '2':
			self.subnet_mask = '172.16.0.0/12'
		elif choice == '3':
			self.subnet_mask = '192.168.0.0/16'
		else:
			print('Alert!, 1nValid option!\n')


	def set_outfile_location(self):
		new_outfile_location = input('Where you want to save output file? [Default: Current working directory] >> ')
		
		if new_outfile_location != '':
			self.outfile_location = new_outfile_location
		else:
			pass


	def scan(self):
		self.set_subnet_mask()
		self.set_outfile_location()
		sys_command = 'sudo zmap -p 80' + ' ' + self.subnet_mask + ' ' + '-o' + ' ' + self.outfile_location
		#args = shlex.split(sys_command)
		#print(sys_command)
		system(sys_command)


	def show(self):
		out_file = open(self.outfile_location)
		driver = webdriver.Chrome() #Loads web browser object from selenium 
	
		#parsing data from output file
		for x in out_file:
			ip_addr.append(x.strip('\n'))

		#I will tell what I got
		for i in range(0,len(ip_addr)-1):
			print("Connecting " + ip_addr[i])
			print("Opening " + ip_addr[i])
			driver.get("http://" + ip_addr[i])
			sleep(3)


if __name__ == '__main__':
	if platform == 'linux':
		main = wtyg()
		main.banner()
		print('1.) Install prerequisites for this tool')
		print('2.) Run script')
		choice = input('> ')
		main.menu(choice)
	else:
		print('This script is not compatible yet with windows and macos...')