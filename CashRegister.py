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
entry_bg = "#ffeeee"

root = Tk()
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
root.geometry(f"{screen_width}x{screen_height}")
root.title("Cash Register")
root.configure(background=bg)

# Due Amount: 

Amount_due_entry = Entry(root, width = int((screen_width*1.04)/100), borderwidth=1, bg = entry_bg, relief = SOLID)
Amount_due_entry.config(font =("Arial", int((screen_width*1.14)/100)))
Amount_due_entry.pack()
Amount_due_entry.place(x =(screen_width*20)/100, y = (screen_height*7.4)/100)
Amount_due_entry.insert(0, "")

Amount_due_Label = Label(root, text = "Enter Amount Due ", bg = bg, fg = text_dark)
Amount_due_Label.config(font=("Arial", int((screen_width*1.14)/100)))
Amount_due_Label.pack()
Amount_due_Label.place(x = (screen_width*6.2)/100, y = (screen_height*7)/100)
price = 0

def Amount_due():
    global price
    price = Amount_due_entry.get()

# Amount_due_Button = Button(root, text="Enter Amount Due",padx = 36, pady = 8, borderwidth=0, bg=button_bg, fg=text_light, command=Amount_due)
# Amount_due_Button.configure(font=("Arial", 14))
# Amount_due_Button.pack()
# Amount_due_Button.place(x = (screen_width*25.5)/100, y = (screen_height*7)/100)

# Given Cash:

Cash_given_entry = Entry(root, width = int((screen_width*1.04)/100), borderwidth=1, bg = entry_bg, relief = SOLID)
Cash_given_entry.config(font =("Arial", int((screen_width*1.14)/100)))
Cash_given_entry.pack()
Cash_given_entry.place(x = (screen_width*20)/100, y = (screen_height*13.9)/100)
Cash_given_entry.insert(0,"")

Cash_given_Label = Label(root, text = "Enter Cash Given ",bg = bg,  fg = text_dark)
Cash_given_Label.config(font=("Arial", int((screen_width*1.14)/100)))
Cash_given_Label.pack()
Cash_given_Label.place(x = (screen_width*6.2)/100, y = (screen_height*13.52)/100)

cash1 = 0

def Cash_given():
    global cash1
    cash1 = Cash_given_entry.get()

# Cash_given_button = Button(root, text="Enter Cash Given",padx = 40, pady = 8, borderwidth=0 , bg=button_bg, fg=text_light, command = Cash_given)
# Cash_given_button.configure(font=("Arial", 14))
# Cash_given_button.pack()
# Cash_given_button.place(x = (screen_width*25.5)/100, y = (screen_height*13.52)/100)

# Confirming to Update the drawer:

confirmation_Label = Label(root, text = "Do you want to update Cash in Drawer?", bg = bg, fg = text_dark, padx = int((screen_width*2.6)/100))
confirmation_Label.config(font=("Arial", int((screen_width*1.14)/100)))
confirmation_Label.pack()
confirmation_Label.place(x = (screen_width*6.25)/100, y = (screen_height*20.4)/100)
# 
input_fields_list = []
var = IntVar()
data = [] 

submit_button = ''

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
    n = (screen_height*37.1)/100

    global price
    price = Amount_due_entry.get()

    global cash1
    cash1 = Cash_given_entry.get()

    for i in range(10):
        a = Label(root, padx = int((screen_width*0.61)/100), pady = int((screen_height*0.926)/100), text=labels[i],bg = bg, fg = text_dark)
        a.config(font=("Arial", int((screen_width*1.14)/100)))
        a.pack()
        a.place(x = (screen_width*2.1)/100, y = n)
        input_fields_list.append(a)
        n+=int((screen_height*4.63)/100)
            
    j = int((screen_height*38.43)/100)
    for entries in range(len(remaining_cash)):
        entry = Entry(root, borderwidth=1, bg = entry_bg, relief = SOLID)
        entry.config(font=("Arial", int((screen_width*1.14)/100)))
        entry.pack()
        entry.place(x = (screen_width*27.1)/100, y = j)
        data.append(entry)
        input_fields_list.append(entry)
        j+=int((screen_height*4.63)/100)
    global submit_button
    submit_button = Button(root, padx = int((screen_width*0.83)/100), pady = int((screen_height*0.46)/100), text = "Confirm", fg = text_light, bg = button_bg,relief = SOLID, command = lambda: [Confirm(remaining_cash), var.set(1)], borderwidth = 5)
    submit_button.config(font=("Arial", int((screen_width*0.83)/100)))
    submit_button.pack()
    submit_button.place(x = int((screen_width*18.75)/100), y = int((screen_height*85.65)/100))
    
    submit_button.wait_variable(var)

    result = checkCashRegister(price, cash1, remaining_cash)
    display_result(result)
    
def No():

    global price
    price = Amount_due_entry.get()

    global cash1
    cash1 = Cash_given_entry.get()

    result = checkCashRegister(price, cash1)
    display_result(result)
    
def display_result(result):
    global mylabel
    mylabel = Label(root, pady = int((screen_height*0.926)/100), text = "STATUS",bg = bg, fg = text_dark, relief="solid", width = int((screen_width*0.521)/100))
    mylabel.configure(font=("Arial", int((screen_width*1.14)/100), 'bold'))
    mylabel.pack()
    mylabel.place(x = (screen_width*59.9)/100, y = (screen_height*7.41)/100)

    global status
    status = Label(root, pady = int((screen_height*0.926)/100), text = result["status"],bg = bg, fg = text_dark, relief="solid", width = int((screen_width*1.04)/100))
    status.configure(font=("Arial", int((screen_width*1.14)/100)))
    status.pack()
    status.place(x = (screen_width*68.75)/100, y = (screen_height*7.41)/100)
    
    global mylabe3
    mylabe3 = Label(root, pady = int((screen_height*0.926)/100), text = "CHANGE",bg = bg, fg = text_dark, relief="solid", width = int((screen_width*1.5625)/100))
    mylabe3.configure(font=("Arial", int((screen_width*1.146)/100), 'bold'))
    mylabe3.pack()
    mylabe3.place(x = (screen_width*59.9)/100, y = (screen_height*12.5)/100)
    
    list = result["change"]
    global array
    array = []
    n = int((screen_height*17.5)/100)
    for i in range(len(list)):
        mylabe4 = Label(root, pady = int((screen_height*0.926)/100), text = list[i][0],bg = bg, fg = text_dark, relief="solid", width = int((screen_width*1.042)/100))
        mylabe4.configure(font=("Arial", int((screen_width*1.146)/100), 'bold'))
        mylabe4.pack()
        mylabe4.place(x = int((screen_width*59.9)/100), y = n)
        array.append(mylabe4)

        mylabe5 = Label(root, pady = int((screen_height*0.521)/100), text = list[i][1],bg = bg, fg = text_dark, relief="solid", width = int((screen_width*0.625)/100))
        mylabe5.configure(font=("Arial", int((screen_width*1.146)/100)))
        mylabe5.pack()
        mylabe5.place(x = (screen_width*75.8)/100, y = n)
        array.append(mylabe5)
        n+=(screen_height*5.1)/100
    
yes_button = Button(root, padx = int((screen_width*0.885)/100), text="Yes", pady = int((screen_height*0.46)/100),borderwidth=0, bg=button_bg, fg=text_light, command=Yes)
yes_button.configure(font=("Arial", int((screen_width*0.729)/100)))
yes_button.pack()
yes_button.place(x = (screen_width*16.4)/100, y = (screen_height*27.3)/100)

no_button = Button(root,padx = int((screen_width*0.88)/100), text="No", pady = int((screen_height*0.64)/100), borderwidth=0, bg=button_bg, fg=text_light, command=No)
no_button.configure(font=("Arial", int((screen_width*0.73)/100)))
no_button.pack()
no_button.place(x = (screen_width*24)/100, y = (screen_height*27.3)/100)

def reset():
    global data
    data = []
    mylabel.destroy()
    status.destroy() 
    mylabe3.destroy()
    Amount_due_entry.delete(0, END)
    Cash_given_entry.delete(0, END)
    if(submit_button != ''):
        submit_button.destroy()

    for items in input_fields_list:
        items.destroy()   
    for item in array:
        item.destroy()

reset_button = Button(root, text = "Reset",padx = int((screen_width*1.04)/100), pady = int((screen_height*0.55)/100), borderwidth=0, bg = button_bg, fg = text_light, command = reset)
reset_button.configure(font=("Arial", int((screen_width*0.833)/100)))
reset_button.pack()
reset_button.place(x = (screen_width*60.1)/100, y = (screen_height*55.6)/100)

root.mainloop()
