from time import sleep
from selenium import webdriver
import httplib2

#Tagged objects
http = httplib2.Http()

#Configuration
ip_addr = list()
out_file = open('srm_web_servers.txt')

#parsing data from output file
for x in out_file:
	ip_addr.append(x.strip('\n'))

driver = webdriver.Chrome()

for i in range(0,len(ip_addr)-1):
	print("Connecting " + ip_addr[i])
	print("Opening " + ip_addr[i])
	driver.get("http://" + ip_addr[i])
	sleep(3)

