import pafy
from tkinter.messagebox import *
myvid = None

def YouTubeLink(link,l1,l2,l3,l4):
    global myvid
    myvid = pafy.new(link)
    l1.config(text="Title: "+myvid.title[:40]+"...")
    l2.config(text="Author: "+myvid.author)
    l3.config(text="Duration: "+myvid.duration)
    l4.config(text="Views: "+str(myvid.viewcount))
    
#===============360px Video Quality=====================
def Low(path):
    global myvid
    try:
        Video_Low_Quality=myvid.streams[0]
        print("\nTitle:",Video_Low_Quality.title)
        print("Video Size:",(int(Video_Low_Quality.get_filesize())//1024)//1024,"MB")
        print("Video Resolution:",Video_Low_Quality.resolution)
        print("Video Extension:",Video_Low_Quality.extension)
        print("\nDownloading Progress...\n")
        Video_Low_Quality.download(filepath=path)  # downloading start at resuming
        print("\nDownload Complete...\n")
    except IndexError:
        showerror("Error","This YouTube Video Not Support Low Quality")

#===============720px Video Quality=====================
def High(path):
    global myvid
    try:
        Video_High_Quality=myvid.streams[1]
        print("\nTitle:",Video_High_Quality.title)
        print("Video Size:",(int(Video_High_Quality.get_filesize())//1024)//1024,"MB")
        print("Video Resolution:",Video_High_Quality.resolution)
        print("Video Extension:",Video_High_Quality.extension)
        print("\nDownloading Progress...\n")
        Video_High_Quality.download(filepath=path)  # downloading start at resuming
        print("\nDownload Complete...\n")
    except IndexError:
        showerror("Error","This YouTube Video Not Support High Quality")