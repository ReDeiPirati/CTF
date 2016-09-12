
from pwn import *
from hashlib import *
import string
import itertools
from Crypto.Util.number import *
from sympy import perfect_power
import time

# Cout primes and perfect powers in a range
def countNumbers(lower,upper):
	countp= 0
	countpp=0
	num=lower
	# Range(lower,upper+1) is not possible to use cause overflow
	while num <= upper:
		if isPrime(num):
			countp+=1
		if perfect_power(num):
			countpp+=1
		num+=1
	return countpp+countp

# Connect to the server using pwntools
conn = remote('secuprim.asis-ctf.ir',42738)
print conn.recvline(timeout=2)
print conn.recvline(timeout=2)
res = conn.recvline(timeout=2)
print res
print conn.recvline(timeout=2)

# Extract postfix and Sha256's first 8 char 
postfix = res.split('"')[1]
sha = res.split('"')[3][:8]

alphanumeric = string.uppercase+string.lowercase+string.digits
ans =""

# Find X
for s in itertools.product(alphanumeric,repeat=4):
	if sha256("%s%s"%(''.join(s),postfix)).hexdigest().startswith(sha):
		print ''.join(s)
		ans=s
		break;

ans= ''.join(ans)
conn.send(ans)

count=0
print conn.recvline()
print conn.recvline()

# Solve the tests
while True:
	time.sleep(1)
	print conn.recvline()
	count+=1
	print "Question number: %d"%count
	numbers = conn.recvline()
	print numbers
	num1=long(numbers.split()[12])
	num2=long(numbers.split()[16])
	answer=str(countNumbers(num1,num2))
	conn.send(answer)