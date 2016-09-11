# CTF 101

Watch your heads!

Fire up the terminal: 
`pirate$ curl -X HEAD -v https://asis-ctf.ir/challenges/`

```
*   Trying 64.34.218.26...
* Connected to asis-ctf.ir (64.34.218.26) port 443 (#0)
* TLS 1.2 connection using TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
* Server certificate: asis-ctf.ir
* Server certificate: NetLock OnlineSSL (Class Online) Tanúsítványkiadó
* Server certificate: NetLock Arany (Class Gold) Főtanúsítvány
> HEAD /challenges/ HTTP/1.1
> Host: asis-ctf.ir
> User-Agent: curl/7.43.0
> Accept: */*
> 
< HTTP/1.1 302 Found
< Server: nginx
< Date: Sun, 11 Sep 2016 19:01:51 GMT
< Content-Type: text/html; charset=utf-8
< Connection: keep-alive
< Vary: Accept-Language, Cookie
< X-Frame-Options: SAMEORIGIN
< Content-Language: fa
< Location: /accounts/login/?next=/challenges/
< Strict-Transport-Security: max-age=15768000; includeSubDomains; preload;
< CTF-Level: Final 2016
< X-Content-Type-Options: nosniff
< X-XSS-Protection: 1; mode=block
< Flag: QVNJU3szMWE0ODM5MDBiODU3NjQyNmNjY2RmNTU0MDJiOWRkNn0K; base64 <-- FLAG:)
* no chunk, no close, no size. Assume close to signal end
```
Decode base64:
`echo "QVNJU3szMWE0ODM5MDBiODU3NjQyNmNjY2RmNTU0MDJiOWRkNn0K" | base64 -D`

The flag is: ASIS{31a483900b8576426cccdf55402b9dd6}

