from Tkinter import *
import tkFileDialog as filedialog
import sys
import subprocess
import ntpath
window = Tk()	#mainwindow
window.title("zyCrypt") #title				
window.geometry('700x700') #dimensions
photo = PhotoImage(file="a.gif") #heading
w = Label(window,image=photo)
w.pack()
class Encrypt(object):				#all these parsed names will be used to label in a txt box and to be attributes of the steghide commands
	def OpenFile1(self,importnitialdir):    #parsing cover file name
    		cover=ntpath.basename(filedialog.askopenfilename(initialdir="I:/zyber/Steganography/steghide",
        	                   filetypes =(("Text File", "*.txt"),("All Files","*.*")),
            	               title = "Choose a file."
                	           )
    			   )
    		return cover
   		
	b = Button(window, text="Selet Cover File",  width=70, command=OpenFile1) #a button for that... but it doesnt wait for button click
	b.pack()

	def OpenFile2(self,initialdir):		#parsing embed file name
    		cover=ntpath.basename(filedialog.askopenfilename
    		original=ntpath.basename(filedialog.askopenfilename(initialdir="I:/zyber/Steganography/steghide",
        	                   filetypes =(("Text File", "*.txt"),("All Files","*.*")),
            	               title = "Choose a file."
                	           )
    			   )
    		return original
   		
	b = Button(window, text="Selet Cover File",  width=70, command=OpenFile2)
	b.pack()
	#print cover

object=Encrypt()
cover = object.OpenFile1(".")    
original = object.OpenFile2(".")  
tkvar = StringVar(window)[][]    #trying to build two tiptool dropwon box where boxx one is encryption and sec0nd one are the modes for each encryption
#meaning, each selection of box1 should make box2 dynamic.. s
choices = { 'cast-128','gost','rijndael-128','twofish','arcfour','cast-256','loki97','rijndael-192','saferplus','wake:','des:','des:','rijndael-256:','serpent:','xtea','blowfish:','enigma::','rc2::','tripledes::'},
{
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'stream'}
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'stream'}
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'stream'}
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'},
{'cbc','cfb','ctr','ecb','ncfb','nofb','ofb'}
}
print(cover)
print(original)
docrypt="steghide "+"-cf "+cover+"-ef "+"original"
#well then call the subprocess with <docrypt> as the command 
#will change for decrypt
window.mainloop()