from tkinter import *
from functions import checkCashRegister

cid = [
["FIVE THOUSAND"],
["ONE THOUSAND"],
["FIVE HUNDRED"],
["ONE HUNDRED"],
["FIFTY"],
["TWENTY"],
["TEN"],
["FIVE"],
["TWO"],
["ONE"]
]

root = Tk()
root.geometry("800x600")
img = PhotoImage(file="Template.png")      

# Adding Image in BackGround

my_label1 = Label(root, image = img)
my_label1.place(x = 0, y = 0)

# Adding on Heading

my_text = Label(root, text = "Cash Register", fg = "red", font = ("Helvetica", 30))
my_text.pack()

e = Entry(root, width = 50)
e.pack()
e.place(x = 250, y = 70)
e.insert(0,"")

def Clickme():
    global price
    price = e.get()

mybutton = Button(root, text="Enter Amount Due", bg="purple", fg="white", command=Clickme)
mybutton.pack()
mybutton.place(x = 500, y = 70)

e1 = Entry(root, width = 50)
e1.pack()
e1.place(x = 250, y = 100)
e1.insert(0,"")

def Clickme1():
    global cash1
    cash1 = e1.get()

mybutton1 = Button(root, text="Enter Cash Given", bg="purple", fg="white", command = Clickme1)
mybutton1.pack()
mybutton1.place(x = 500, y = 100)

confirmation_Label = Label(root, text = "Do you want to update Cash in Drawer?\n If Yes, press (Y/y) else press any key", padx = 50, bg = "white")
confirmation_Label.pack()
confirmation_Label.place(x = 250, y = 450)


e2 = Entry(root, width = 50)
e2.pack()
e2.place(x = 250, y = 500)
e2.insert(0,"")

labels = [
"Cash in Five Thousand Rupees:- ",
"Cash in One Thousand Rupees:-",
"Cash in Five Hundred Rupees:-",
"Cash in One Hundred Rupees:- ",
"Cash in Fifty Rupees:- ",
"Cash in Twenty Rupees:- ",
"Cash in Ten Rupees:- ",
"Cash in Five Rupees:- ",
"Cash in Two Rupees:- ",
"Cash in One Rupees:- "
]
def Clickme2():
    if e2.get() == 'Y' or e2.get() == 'y':
        for item in cid:    
            x = int(input("Cash in " + item[0] + " Rupee/s:- "))
            item.append(x)    
        result = checkCashRegister(price, cash1, cid)
        mylabel = Label(root, text = result)
        mylabel.pack()
        mylabel.place(x = 260, y = 550)
    else:
        result = checkCashRegister(price, cash1)
        mylabel1 = Label(root, text = result)
        mylabel1.pack()
        mylabel1.place(x = 260, y = 550)


mybutton2 = Button(root, text="Confirm", bg="purple", fg="white", command=Clickme2)
mybutton2.pack()
mybutton2.place(x = 500, y = 500)

def Clickme3():
    return root.quit()

# Quit Button

mybutton3 = Button(root, text="Quit", bg="purple", fg="white", command=Clickme3)
mybutton3.pack()
mybutton3.place(x = 600, y = 500)

root.mainloop()

