from Tkinter import *
import tkFileDialog as filedialog
import sys
import subprocess
window = Tk()
window.title("zyCrypt")
window.geometry('350x200')
def OpenFile(self):
    self.name = filedialog.askopenfilename(initialdir="I:/zyber/Steganography/steghide",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    self.name
Label(window, text="Cover File:").grid(row=0)

v = StringVar()
e1 = Entry(window, textvariable=v)
e1.grid(row=0, column=1)

e1.pack()

#OpenFile()    
#print(name)
window.mainloop()