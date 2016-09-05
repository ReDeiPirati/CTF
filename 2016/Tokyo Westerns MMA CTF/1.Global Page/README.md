# Global Page WriteUp

The "quest" begin with a link wihtout any hint or sentence: [link to Global Page.](http://globalpage.chal.ctf.westerns.tokyo/)

![Landing page](images/Globalpageindex.png)
The Landing Page show one deleted and two followable links.

Trying to follow ctf or tokyo, the browser makes a GET request to a php as parameter(page) the followed link(ctf or tokyo) -> `http://globalpage.chal.ctf.westerns.tokyo/?page=ctf` or `http://globalpage.chal.ctf.westerns.tokyo/?page=tokyo`.


![Page](images/page.png)

Mh! Warning: include() => suggest with high probability a **LFI** attack.



