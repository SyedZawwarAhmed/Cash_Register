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
root.geometry("1920x1080")
root.title("Cash Register")

# Due Amount: 

Amount_due_entry = Entry(root, width = 50)
Amount_due_entry.pack()
Amount_due_entry.place(x = 25, y = 70)
Amount_due_entry.insert(0, "")

def Amount_due():
    global price
    price = Amount_due_entry.get()

Amount_due_Button = Button(root, text="Enter Amount Due", bg="purple", fg="white", command=Amount_due)
Amount_due_Button.pack()
Amount_due_Button.place(x = 225, y = 70)

# Given Cash:

Cash_given_entry = Entry(root, width = 50)
Cash_given_entry.pack()
Cash_given_entry.place(x = 25, y = 100)
Cash_given_entry.insert(0,"")

def Cash_given():
    global cash1
    cash1 = Cash_given_entry.get()

Cash_given_button = Button(root, text="Enter Cash Given", bg="purple", fg="white", command = Cash_given)
Cash_given_button.pack()
Cash_given_button.place(x = 225, y = 100)

# Confirming to Update the drawer:

confirmation_Label = Label(root, text = "Do you want to update Cash in Drawer?\n If Yes, press (Y/y) else press any key", padx = 50, bg = "white")
confirmation_Label.pack()
confirmation_Label.place(x = 25, y = 125)

confirmation_Entry = Entry(root, width = 10)
confirmation_Entry.pack()
confirmation_Entry.place(x = 45, y = 165)
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
        n = 200
        for i in range(10):
            a = Label(root, padx = 20, pady = 5, text=labels[i])
            a.pack()
            a.place(x = 0, y = n)
            n+=25
            
        j = 200
        for entries in range(len(cid)):
            entry = Entry(root)
            entry.pack()
            entry.place(x = 190, y = j)
            data.append(entry)
            j+=25

        submit_button = Button(root, padx = 30, text = "Submit", fg = "White", bg = "Purple", command = lambda: [Submit(data, cid), var.set(1)])
        submit_button.pack()
        submit_button.place(x = 75, y = 600)

        submit_button.wait_variable(var)

        result = checkCashRegister(price, cash1, cid)
  
    else:
        result = checkCashRegister(price, cash1)
       
    mylabel = Label(root, text = result["status"])
    mylabel.pack()
    mylabel.place(x = 260, y = 550)

    mylabel = Label(root, text = result["change"])
    mylabel.pack()
    mylabel.place(x = 260, y = 570)

confirmation_button = Button(root, text="Confirm", bg="purple", fg="white", command=Confirm)
confirmation_button.pack()
confirmation_button.place(x = 126, y = 165)

root.mainloop()
