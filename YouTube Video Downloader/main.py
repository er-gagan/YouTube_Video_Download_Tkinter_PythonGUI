from tkinter import *
from YouTube import *
import urllib
from urllib.request import urlopen
from tkinter.messagebox import *

root = Tk()
root.geometry('790x540')
root.resizable(0,0)
photo = PhotoImage(file = "./logo.png")
root.iconphoto(True,photo)
root.title("YouTube Video Downloader")

image1= PhotoImage(file="./banner.png")
label_for_image= Label(root, image=image1)
label_for_image.place(x=240,y=0)

Link = StringVar()
Path = StringVar()

def CheckInternet():
    try:
        urlopen("https://www.google.com/")
        return True
    except urllib.error.URLError as Error:
        return False
    
def search():
    if CheckInternet():
        link = Link.get()
        if link[0:30:] == "https://www.youtube.com/watch?":
            YouTubeLink(link,l1,l2,l3,l4)
        else:
            showerror("Error","Please Paste YouTube Video Link Only")
    else:
        showerror("Error","Your system is not connected to the internet")
    
def VideoLow():
    path = Path.get()
    if path == "" or path == None or path[0::] in "                                               ":
        showerror("Error","Please Enter Destination Path")
    else:
        Low(path)

def VideoHigh():
    path = Path.get()
    if path == "" or path == None or path[0::] in "                                               ":
        showerror("Error","Please Enter Destination Path")
    else:
        High(path)

Label(root,text="Paste YouTube Video Link Here:",font=("Arial",13)).place(x=20,y=75)

e1 = Entry(root,font=("ArialBlack",25),width=40,bd=5,textvariable=Link)
e1.focus()
e1.place(x=30,y=100)

Button(root,font=("Calibri",20),text="Search",command=search,bd=4).place(x=350,y=160)

l1 = Label(root,text="Title:",font=("ArialBlack",20))
l1.place(x=50,y=220)

l2 = Label(root,text="Author:",font=("ArialBlack",20))
l2.place(x=50,y=260)

l3 = Label(root,text="Duration:",font=("ArialBlack",20))
l3.place(x=50,y=300)

l4 = Label(root,text="Views:",font=("ArialBlack",20))
l4.place(x=50,y=340)

Label(root,text="Paste Destination Path to be Download YouTube Video:",font=("Arial",13)).place(x=20,y=377)

e2 = Entry(root,font=("ArialBlack",25),width=40,bd=5,textvariable=Path)
e2.place(x=30,y=400)

Button(root,text="Download Video In Low Quality",font=("ArialBlack",15,),command=VideoLow,bd=5).place(x=50,y=470)
Button(root,text="Download Video In High Quality",font=("ArialBlack",15),command=VideoHigh,bd=5).place(x=440,y=470)


root.mainloop()

# https://www.youtube.com/watch?v=4ccg1tEcVkw