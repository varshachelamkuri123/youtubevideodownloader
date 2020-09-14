
import tkinter as tk
from tkinter import *

import pytube
from pytube import YouTube
def downloadVid():
    global E1
   
    yt=YouTube(E1.get())
    videos=yt.streams.all()
    s=1
    for v in videos:
        print(str(s)+"."+str(v))
        s +=1
    n=int(input("enter your choice"))
    vid=videos[n-1]
    destination=str(input("enter your destinstion"))
    vid.download(destination)
    print(yt.filename+"\n has been downloaded")
root=tk.Tk()
 
w=tk.Label(root,text="YouTube Downloader")
w.pack()

E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)


button=tk.Button(root,text="Download",fg="red",command=downloadVid)
button.pack(side=tk.BOTTOM)
root.mainloop()
          
