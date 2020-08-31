from tkinter import *
from tkinter import filedialog
import os
import HenonDecryption as hD
import ArnoldDecryption as aD
from PIL import ImageTk, Image

def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))

def decryptArnoldShuffle():
    filePath = entry1.get()

    im = Image.open(filePath)
    image_size = im.size

    width = image_size[0]
    height = image_size[1]

    numberOfIterations = int(entry5.get())
    modN = int(entry6.get())

    resImage = aD.decryptArnoldImage(width,height,numberOfIterations,modN,filePath)
    entry2.insert(0,resImage)


def decryptHenonManipulation():
    filename = entry1.get()
    resImage = hD.decryptHenonImage(filename)
    entry3.insert(0,resImage)
    #print(filename)

def performEntireDecryption():
    hD.decryptHenonImage()
    filename = entry3.get()
    resImage = aD.decryptArnoldImage(filename)
    entry2.insert(0, resImage)
    entry4.insert(0, resImage)


def openFileForArnold():
    window = Toplevel(root)
    window.title("Arnold Map")
    window.geometry("600x600")
    path = entry2.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForHenon():
    window = Toplevel(root)
    window.title("Henon Map")
    window.geometry("600x600")
    path = entry3.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

#from tkFileDialog import askopenfilename

root =Tk()
Frame1 = Frame(root)
Frame1.pack()

Frame2 = Frame(root)
Frame2.pack(side=TOP)

Frame3 = Frame(root)
Frame3.pack(side=TOP)

Frame4= Frame(root)
Frame4.pack(side=TOP)

Frame5 = Frame(root)
Frame5.pack(side = TOP)

label_1 = Label(Frame1, text ="Image to be Decrypted : ",width = 125)
entry1 = Entry(Frame1,width =100)
button1 = Button(Frame1, text = "Select Image",command = choose_File)

label_2 = Label(Frame2,text = "No. Of Iterations:")
entry5 = Entry(Frame2,width = 80)

label_3 = Label(Frame2,text = "Value of mod N:")
entry6 = Entry(Frame2,width = 80)

button2 = Button(Frame3, text = "Decrypt Arnold Cat Map",command = decryptArnoldShuffle,width=20)
entry2 = Entry(Frame3,width =80)
button3 = Button(Frame3, text="Open Image",command = openFileForArnold)

button4 = Button(Frame4, text="Decrypt Henon Map",command = decryptHenonManipulation,width=20)
entry3 = Entry(Frame4,width =80)
button5 = Button(Frame4, text="Open Image",command = openFileForHenon)

button6 = Button(Frame5, text="Perform Decryption",command = performEntireDecryption,width=20)
entry4 = Entry(Frame5,width=80)
button7 = Button(Frame5, text="Open Image",command = openFileForArnold)

label_1.pack(side = TOP)
entry1.pack(side = TOP)
button1.pack(side = TOP)

label_2.pack(side = TOP)
entry5.pack(side = TOP)

label_3.pack(side = TOP)
entry6.pack(side =TOP)

button2.pack(side = LEFT)
entry2.pack(side=LEFT)
button3.pack(side=LEFT)

button4.pack(side = LEFT)
entry3.pack(side = LEFT)
button5.pack(side = LEFT)

button6.pack(side = LEFT)
entry4.pack(side =LEFT)
button7.pack(side=LEFT)

root.mainloop()