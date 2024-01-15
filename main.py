from pytube import YouTube
from tkinter import *
import win32clipboard
from plyer import notification
from win10toast import ToastNotifier

toast = ToastNotifier()

#Get Clipboard 
#win32clipboard.OpenClipboard()
#link = win32clipboard.GetClipboardData()
#win32clipboard.CloseClipboard()

try:
    win32clipboard.OpenClipboard()

    link = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    video = YouTube(link)

    name = video.title
    toast.show_toast("ClipboardDL", f"Downloading: {name}", duration=3,icon_path = "41+gelS+89L._AC_UF894,1000_QL80_.ico")

    ys = video.streams.get_highest_resolution()


    ys.download()


    toast.show_toast(f"ClipboardDL", "Finished!", duration=3,icon_path = "41+gelS+89L._AC_UF894,1000_QL80_.ico")
        
except:
    toast.show_toast("ClipboardDL", "Not a supported link", duration=3,icon_path = "41+gelS+89L._AC_UF894,1000_QL80_.ico")


