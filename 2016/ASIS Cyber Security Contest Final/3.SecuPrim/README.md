# SecuPrim(PWN) writeup

Description:
```
Test your might.
nc secuprim.asis-ctf.ir 42738
```
Let's connect:
```
Bot detection: Are you ready?

ASIS needs proof of work to start the Math challenge.

SHA256(X + "C2KqwGZaVs3IL7exIxPmMf").hexdigest() = "ddc91896f78e85b15597da41793b143e...",

X is a string of alphanumeric and |X| = 4
```

X looks like: ([A-Z]|[a-z]|[0-9]){4} so the possible combination are 52**4(D(52,4)): the dispositions(?) of 52 char on 4.

In the next 30 challenges was asked to guess:
```
In each stage tell us the number of primes or perfect power integers in given range

-----------------------------------------------------------------------------------

Question number: 1
What's the number of primes or perfect powers like n such that: 227036832795065889903254126908022045187773043077006026091797424774580454170936485242624129444594570235744796783430950725784783948112544611185467891099856852874974031873062295722416896951878648085488714636560750594359088767211547683445370482650338448686974136961040 <= n <= 227036832795065889903254126908022045187773043077006026091797424774580454170936485242624129444594570235744796783430950725784783948112544611185467891099856852874974031873062295722416896951878648085488714636560750594359088767211547683445370482650338448686974136961144
```

A simple calculus: iterate from the lower to the upper and foreach number ask if was Prime or a Perfect Power; the sum take us to: 
`Congratz: the flag is: ASIS{Security_with0ut_Prime_Numbers_iS_Nothing_AT_ALL_}`   