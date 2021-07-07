from tkinter import *

def checkCashRegister(price, cash, cid=[["ONE", 1000], ["TWO", 2000], ["FIVE", 5000], ["TEN", 10000], ["TWENTY", 20000], ["FIFTY", 500000], ["ONE HUNDRED", 1000000], ["FIVE HUNDRED", 500000], ["ONE THOUSAND", 1000000], ["FIVE THOUSAND", 5000000]]):
    status = getStatus(price, cash, cid)
    change = getChange(price, cash, cid, status)
    return {
        "status": status,
        "change": change
    }


def getStatus(price, cash, cid):
    cashInDrawerArray = cid
    cinda = []
    cashInDrawer = 0
    for item in cashInDrawerArray:
        cinda.append(item[1])
        cashInDrawer += item[1]
    ac = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
    status = ""
    totalChange = float(cash) - float(price)
    if totalChange > cashInDrawer:
        status = "INSUFFICIENT_FUNDS"
    elif totalChange == cashInDrawer:
        status = "CLOSED"
    else:
        status = "OPEN"
        i = 0
        while i < len(cinda):
            if totalChange >= ac[i] and cinda[i] >= ac[i]:
                totalChange -= ac[i]
                cinda[i] -= ac[i]
                totalChange = float(format(totalChange, ".2f"))
                cinda[i] = float(format(cinda[i], ".2f"))
            else: 
                i += 1
      
        if totalChange != 0:
            status = "INSUFFICIENT_FUNDS"

    return status


def getChange(price, cash, cid, status):
    totalChange = float(cash) - float(price)
    changeArray = []
    currentCurrencyName = ""
    currentCurrency = 0
    change = []
    ac = [
    ["FIVE THOUSAND", 5000],
    ["ONE THOUSAND", 1000],
    ["FIVE HUNDRED", 500],
    ["ONE HUNDRED", 100],
    ["FIFTY", 50],
    ["TWENTY", 20],
    ["TEN", 10],
    ["FIVE", 5],
    ["TWO", 2],
    ["ONE", 1]
    ]
    cashInDrawerArray = cid
    i = 0
    j = 0
    while i < len(ac):
        if totalChange >= ac[i][1] and cashInDrawerArray[i][1] >= ac[i][1]:
            totalChange -= ac[i][1]
            cashInDrawerArray[i][1] -= ac[i][1]
            totalChange = float(format(totalChange, ".2f"))
            cashInDrawerArray[i][1] = float(format(cashInDrawerArray[i][1], ".2f"))
            j += 1
        else:
            if j != 0:
                currentCurrencyName = ac[i][0]
                currentCurrency = ac[i][1] * j
                if status != "INSUFFICIENT_FUNDS":
                    change = [currentCurrencyName, currentCurrency]
                    changeArray.append(change)
            j = 0
            i += 1
    return changeArray

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
img = PhotoImage(file="D:\Annas Docs\Coding\Python\Template.png")      


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

root.mainloop()
