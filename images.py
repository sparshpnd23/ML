from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Image")
#root.resizable(False,False)
def back(number):

    global label
    global btn_back
    global btn_forword
    label.grid_forget()
    label =Label(image=images[number-1])
    btn_back =Button(root,text="<<",command=lambda: back(number-1))
    btn_forword=Button(root,text=">>",command=lambda : forword(number+1))
    status =Label(root,text="Image "+str(number)+ " of "+str(len(images)),bd=1,anchor=E,relief=SUNKEN)
    status.grid(row=2,columnspan=3,pady=10,sticky=W+E)

    if number == 1:
        btn_back=Button(root,text="<<",state=DISABLED)
    label.grid(row=0,column=0,columnspan=3)
    btn_back.grid(row=1,column=0)
    btn_forword.grid(row=1,column=2)


def quit():
    root.quit()
def forword(number):
    global label
    global btn_back
    global btn_forword
    label.grid_forget()
    label =Label(image=images[number-1])
    btn_back =Button(root,text="<<",command=lambda: back(number-1))
    btn_forword=Button(root,text=">>",command=lambda : forword(number+1))
    status =Label(root,text="Image "+str(number)+ " of "+str(len(images)),bd=1,anchor=E,relief=SUNKEN)
    status.grid(row=2,columnspan=3,pady=10,sticky=W+E)


    if number == len(images):
        btn_forword=Button(root,text=">>",state=DISABLED)
    label.grid(row=0,column=0,columnspan=3)
    btn_back.grid(row=1,column=0)
    btn_forword.grid(row=1,column=2)

    


  
img1 = ImageTk.PhotoImage(Image.open('image1.jpeg'))
img2 = ImageTk.PhotoImage(Image.open('image2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('image3.jpeg'))
img4 = ImageTk.PhotoImage(Image.open('image4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('image5.jpeg'))
img6 = ImageTk.PhotoImage(Image.open('image6.jpeg'))
images=[img1,img2,img3,img4,img5,img6]
label =Label(image=img1)
status =Label(root,text="Image 1 of "+str(len(images)),bd=1,anchor=E,relief=SUNKEN)

label.grid(row=0,column=0,columnspan=3)
btn_back = Button(root,text="<<",command=back, state=DISABLED)
btn_exit = Button(root,text="Exit",command=quit)
btn_forword = Button(root,text=">>",command=lambda :forword(2))
btn_back.grid(row=1,column=0)
btn_exit.grid(row=1,column=1)
btn_forword.grid(row=1,column=2)
status.grid(row=2,columnspan=3,pady=10,sticky=W+E)



root.mainloop()