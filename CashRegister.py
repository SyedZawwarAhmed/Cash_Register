from tkinter import *
from tkinter.font import BOLD
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
root.geometry("1920x1080")
root.title("Cash Register")


# Due Amount: 

Amount_due_entry = Entry(root, width = 25)
Amount_due_entry.config(font =("Arial", 22))
Amount_due_entry.pack()
Amount_due_entry.place(x = 25, y = 80)
Amount_due_entry.insert(0, "")

def Amount_due():
    global price
    price = Amount_due_entry.get()

Amount_due_Button = Button(root, text="Enter Amount Due", bg="purple", fg="white", command=Amount_due)
Amount_due_Button.configure(font=("Arial", 18))
Amount_due_Button.pack()
Amount_due_Button.place(x = 340, y = 76)

# Given Cash:

Cash_given_entry = Entry(root, width= 25)
Cash_given_entry.config(font =("Arial", 22))
Cash_given_entry.pack()
Cash_given_entry.place(x = 25, y = 150)
Cash_given_entry.insert(0,"")

def Cash_given():
    global cash1
    cash1 = Cash_given_entry.get()

Cash_given_button = Button(root, text="Enter Cash Given", bg="purple", fg="white", command = Cash_given)
Cash_given_button.configure(font=("Arial", 18))
Cash_given_button.pack()
Cash_given_button.place(x = 350, y = 146)

# Confirming to Update the drawer:

confirmation_Label = Label(root, text = "Do you want to update Cash in Drawer?\n If Yes, press (Y/y) else press any key", padx = 50, bg = "white")
confirmation_Label.config(font=("Arial", 22))
confirmation_Label.pack()
confirmation_Label.place(x = 0, y = 220)

confirmation_Entry = Entry(root, width = 15)
confirmation_Entry.config(font=('Arial', 18))
confirmation_Entry.pack()
confirmation_Entry.place(x = 100, y = 330)
confirmation_Entry.insert(0,"")

labels = [
"Cash in Five Thousand Rupees:- ",
"Cash in One Thousand Rupees:- ",
"Cash in Five Hundred Rupees:- ",
"Cash in One Hundred Rupees:- ",
"Cash in Fifty Rupees:- ",
"Cash in Twenty Rupees:- ",
"Cash in Ten Rupees:- ",
"Cash in Five Rupees:- ",
"Cash in Two Rupees:- ",
"Cash in One Rupees:- "
]
data = []

var = IntVar()
def Submit(data, cid):
    i = 0
    for items in cid:
        j = data[i]
        if(j.get()==0):
            items.append(0)
        else:
            items.append(int(j.get()))
        i+=1

def Confirm():
    if confirmation_Entry.get() == 'Y' or confirmation_Entry.get() == 'y':
        n = 400
        for i in range(10):
            a = Label(root, padx = 30, pady = 10, text=labels[i])
            a.config(font=("Arial", 22))
            a.pack()
            a.place(x = 0, y = n)
            n+=50
            
        j = 415
        for entries in range(len(cid)):
            entry = Entry(root)
            entry.config(font=("Arial", 22))
            entry.pack()
            entry.place(x = 480, y = j)
            data.append(entry)
            j+=50

        submit_button = Button(root, padx = 20, pady = 5, text = "Submit", fg = "White", bg = "Purple", command = lambda: [Submit(data, cid), var.set(1)])
        submit_button.config(font=("Arial", 18))
        submit_button.pack()
        submit_button.place(x = 40, y = 925)

        submit_button.wait_variable(var)

        result = checkCashRegister(price, cash1, cid)
  
    else:
        result = checkCashRegister(price, cash1)
    
    mylabel = Label(root, padx = 10, pady = 10, text = "STATUS", borderwidth=2, relief="solid")
    mylabel.configure(font=("Arial", 22))
    mylabel.pack()
    mylabel.place(x = 1150, y = 80)
       
    mylabel = Label(root, pady = 10, text = result["status"], borderwidth=2, relief="solid",width=20)
    mylabel.configure(font=("Arial", 22))
    mylabel.pack()
    mylabel.place(x = 1287, y = 80)

    mylabel = Label(root, pady = 10, text = "CHANGE", borderwidth=2, relief="solid", width = 28)
    mylabel.configure(font=("Arial", 22))
    mylabel.pack()
    mylabel.place(x = 1150, y = 135)
    
    list = result["change"]
    n = 189
    for i in range(len(list)):
        mylabe1 = Label(root, pady = 10, text = list[i][0], borderwidth=2, relief="solid", width = 18)
        mylabe1.configure(font=("Arial", 22))
        mylabe1.pack()
        mylabe1.place(x = 1150, y = n)

        mylabe1 = Label(root, pady = 10, text = list[i][1], borderwidth=2, relief="solid", width = 10)
        mylabe1.configure(font=("Arial", 22))
        mylabe1.pack()
        mylabe1.place(x = 1457, y = n)

        n+=55 

confirmation_button = Button(root, text="Confirm", bg="purple", fg="white", command=Confirm)
confirmation_button.configure(font=("Arial", 16))
confirmation_button.pack()
confirmation_button.place(x = 325, y = 325)

root.mainloop()
