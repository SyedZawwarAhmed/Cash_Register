from tkinter import *
from tkinter.font import BOLD
from functions import checkCashRegister
from functions import remaining_cash
from functions import cid
from functions import labels

button_bg = "#023e8a"
text_light = "#caf0f8"
text_dark = "#03045e"
bg = "#CAF0F8"

root = Tk()
root.geometry("1280x720")
root.title("Cash Register")
root.configure(background=bg)

# Due Amount: 

Amount_due_entry = Entry(root, width = 20, borderwidth=0)
Amount_due_entry.config(font =("Arial", 22))
Amount_due_entry.pack()
Amount_due_entry.place(x = 150, y = 80)
Amount_due_entry.insert(0, "")

def Amount_due():
    global price
    price = Amount_due_entry.get()

Amount_due_Button = Button(root, text="Enter Amount Due",padx = 36, pady = 8, borderwidth=0, bg=button_bg, fg=text_light, command=Amount_due)
Amount_due_Button.configure(font=("Arial", 14))
Amount_due_Button.pack()
Amount_due_Button.place(x = 490, y = 76)

# Given Cash:

Cash_given_entry = Entry(root, width= 20, borderwidth=0)
Cash_given_entry.config(font =("Arial", 22))
Cash_given_entry.pack()
Cash_given_entry.place(x = 150, y = 150)
Cash_given_entry.insert(0,"")

def Cash_given():
    global cash1
    cash1 = Cash_given_entry.get()

Cash_given_button = Button(root, text="Enter Cash Given",padx = 40, pady = 8, borderwidth=0 , bg=button_bg, fg=text_light, command = Cash_given)
Cash_given_button.configure(font=("Arial", 14))
Cash_given_button.pack()
Cash_given_button.place(x = 490, y = 146)

# Confirming to Update the drawer:

confirmation_Label = Label(root, text = "Do you want to update Cash in Drawer?", bg = bg, fg = text_dark, padx = 50)
confirmation_Label.config(font=("Arial", 22))
confirmation_Label.pack()
confirmation_Label.place(x = 120, y = 220)
# 
input_fields_list = []
var = IntVar()
data = []        
def Confirm(cash_entered):
    i = 0
    for item in cash_entered:
        j = data[i]
        if(j.get()==""):
            item[1] = 0
        else:
            item[1] = int(j.get())
        i += 1
def Yes():
    n = 400
    for i in range(10):
        a = Label(root, padx = 30, pady = 10, text=labels[i],bg = bg, fg = text_dark)
        a.config(font=("Arial", 22))
        a.pack()
        a.place(x = 40, y = n)
        input_fields_list.append(a)
        n+=50
            
    j = 415
    for entries in range(len(remaining_cash)):
        entry = Entry(root, borderwidth=0)
        entry.config(font=("Arial", 22))
        entry.pack()
        entry.place(x = 520, y = j)
        data.append(entry)
        input_fields_list.append(entry)
        j+=50
    global submit_button
    submit_button = Button(root, padx = 16, pady = 5, text = "Confirm", fg = text_light, bg = button_bg,relief = SOLID, command = lambda: [Confirm(remaining_cash), var.set(1)], borderwidth = 5)
    submit_button.config(font=("Arial", 16))
    submit_button.pack()
    submit_button.place(x = 360, y = 925)
    
    submit_button.wait_variable(var)

    result = checkCashRegister(price, cash1, remaining_cash)
    display_result(result)
    
def No():
    result = checkCashRegister(price, cash1)
    display_result(result)
    
def display_result(result):
    global mylabel
    mylabel = Label(root, pady = 10, text = "STATUS",bg = bg, fg = text_dark, relief="solid", width = 10)
    mylabel.configure(font=("Arial", 22, 'bold'))
    mylabel.pack()
    mylabel.place(x = 1150, y = 80)

    global status
    status = Label(root, pady = 10, text = result["status"],bg = bg, fg = text_dark, relief="solid", width = 20)
    status.configure(font=("Arial", 22))
    status.pack()
    status.place(x = 1320, y = 80)
    
    global mylabe3
    mylabe3 = Label(root, pady = 10, text = "CHANGE",bg = bg, fg = text_dark, relief="solid", width = 30)
    mylabe3.configure(font=("Arial", 20, 'bold'))
    mylabe3.pack()
    mylabe3.place(x = 1150, y = 135)
    
    list = result["change"]
    global array
    array = []
    n = 189
    for i in range(len(list)):
        mylabe4 = Label(root, pady = 10, text = list[i][0],bg = bg, fg = text_dark, relief="solid", width = 20)
        mylabe4.configure(font=("Arial", 22))
        mylabe4.pack()
        mylabe4.place(x = 1150, y = n)
        array.append(mylabe4)

        mylabe5 = Label(root, pady = 10, text = list[i][1],bg = bg, fg = text_dark, relief="solid", width = 12)
        mylabe5.configure(font=("Arial", 22))
        mylabe5.pack()
        mylabe5.place(x = 1456, y = n)
        array.append(mylabe5)
        n+=55
    
yes_button = Button(root, padx = 17,  text="Yes", pady = 6,borderwidth=0, bg=button_bg, fg=text_light, command=Yes)
yes_button.configure(font=("Arial", 14))
yes_button.pack()
yes_button.place(x = 315, y = 295)

no_button = Button(root,padx = 17, text="No", pady = 7, borderwidth=0, bg=button_bg, fg=text_light, command=No)
no_button.configure(font=("Arial", 14))
no_button.pack()
no_button.place(x = 460, y = 295)

def reset():
    global data
    data = []
    mylabel.destroy()
    status.destroy() 
    mylabe3.destroy()
    Amount_due_entry.delete(0, END)
    Cash_given_entry.delete(0, END)
    submit_button.destroy()

    for items in input_fields_list:
        items.destroy()   
    for item in array:
        item.destroy()

reset_button = Button(root, text = "Reset",padx = 20, pady = 6, borderwidth=0, bg = button_bg, fg = text_light, command = reset)
reset_button.configure(font=("Arial", 16))
reset_button.pack()
reset_button.place(x = 1154, y = 600)

root.mainloop()
