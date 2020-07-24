import pafy
def YouTubeLink(link,l1,l2,l3,l4):
    myvid = pafy.new(link)
    l1.config(text="Title: "+myvid.title[:40]+"...")
    l2.config(text="Author: "+myvid.author)
    l3.config(text="Duration: "+myvid.duration)
    l4.config(text="Views: "+str(myvid.viewcount))
    # path = "C:/Users/gagan/OneDrive/Desktop"
    # print(myvid.title)
    # print(myvid.author)
    # print(myvid.duration)
    # print(myvid.viewcount)

#===============360px Video Quality=====================
# Video_Low_Quality=myvid.streams[0]
# print((int(Video_Low_Quality.get_filesize())//1024)//1024,"MB")
# print(Video_Low_Quality.resolution)
# print(Video_Low_Quality.extension)
# Video_Low_Quality.download(filepath=path)  # downloading start at resuming
# print("Download Complete...")

#===============720px Video Quality=====================
# Video_High_Quality=myvid.streams[1]
# print((int(Video_High_Quality.get_filesize())//1024)//1024,"MB")
# print(Video_High_Quality.resolution)
# print(Video_High_Quality.extension)
# Video_High_Quality.download(filepath=path)  # downloading start at resuming
# print("Download Complete...")