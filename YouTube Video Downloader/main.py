from tkinter import *
from YouTube import *

root = Tk()
root.geometry('790x550')
root.resizable(0,0)
photo = PhotoImage(file = "./logoo.png")
root.iconphoto(True,photo)
root.title("YouTube Video Downloader")

image1= PhotoImage(file="./we.png")
label_for_image= Label(root, image=image1)
label_for_image.place(x=240,y=0)

Link = StringVar()
Path = StringVar()

def Clear():
    e1.insert(0,"Paste YouTube Video Link")
    e1.bind("<FocusIn>", lambda args: e1.delete('0', 'end'))
    
    e2.insert(0,"Paste The Destination Path To Download Video")
    e2.bind("<FocusIn>", lambda args: e2.delete('0', 'end'))
    
def search():
    link = Link.get()
    YouTubeLink(link,l1,l2,l3,l4)
    
def VideoLow():
    path = Path.get()
    Low(path)

def VideoHigh():
    path = Path.get()
    High(path)

e1 = Entry(root,font=("ArialBlack",25),width=40,bd=5,textvariable=Link)
e1.place(x=30,y=100)

Button(root,font=("Calibri",20),text="Search",command=search).place(x=350,y=160)

l1 = Label(root,text="Title:",font=("ArialBlack",20))
l1.place(x=50,y=220)

l2 = Label(root,text="Author:",font=("ArialBlack",20))
l2.place(x=50,y=260)

l3 = Label(root,text="Duration:",font=("ArialBlack",20))
l3.place(x=50,y=300)

l4 = Label(root,text="Views:",font=("ArialBlack",20))
l4.place(x=50,y=340)

e2 = Entry(root,font=("ArialBlack",25),width=40,bd=5,textvariable=Path)
e2.place(x=30,y=400)

Button(root,text="Download Video In Low Quality",font=("ArialBlack",15,),command=VideoLow,bd=5).place(x=50,y=470)
Button(root,text="Download Video In High Quality",font=("ArialBlack",15),command=VideoHigh,bd=5).place(x=440,y=470)

Clear()

root.mainloop()

# https://www.youtube.com/watch?v=4ccg1tEcVkw