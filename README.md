# Steghide-gui
i'm just tryna build a gui for this 
(read README.docx..... screeenshots inside..)


Readme:

Step 1:

First, install steghide from http://steghide.sourceforge.net/

Step 2:

Copy the desired document and a cover image for encryption to the steghide folder 
In my case its I:\zyber\Steganography\steghide

 

The cover image is c.jpg and the file we want to encrypt and hide is a.docx.

Step 3:
There are various methods of encryption. 

#steghide
Gives you a help menu.

#steghide encinfo
Gives all available encryptions and options.


This is where i’m hanging in desigining a gui... more info about the gui part is some_code.py
Dropdown boxes with each algorithm has their own modes (like an address... 2d array?)

This is just without any parameters.
	Open command window the above said directory, and paste the following commands to encrypt.

#steghide embed -cf c.jpg -ef a.docx
 
	Itll ask for passphrase. Enter twice to confirm it.
It will be encrypted. 
 



Since a.docx is encrypted inside c.jpg, we deleted it to check it will comeback after extracting.

  
Step 4: 
	For Extracting of the document,
#steghide extract -sf c.jpg

Given passphrase, 
 


And, Voil! A.docx is extracted.



So on to the next part,
	Check the read only checkbox on the jpeg’s properties.

 

  Editing the metadata for the document file and the jpeg by Right clicking>Properties>Details.

 


The final jpeg, once written on cd, is write protected,and the document will be carried on by the cd, unless copied.

The password is: qwerty

And, I had an idea about geo locking the file to a specific place(s). How cool wouldthat be?! Anybody could help on that, or the gui part, Thanks  For the Contribution!
