from tkinter import *
from tkinter import ttk
from tkinter import font
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
        entry = Entry(root, borderwidth=1, width = int((screen_width*1.04)/100), bg = entry_bg, relief = SOLID)
        entry.config(font=("Arial", int((screen_width*1.14)/100)))
        entry.pack()
        entry.place(x = (screen_width*25)/100, y = j)
        data.append(entry)
        input_fields_list.append(entry)
        j+=int((screen_height*4.63)/100)
    global submit_button
    submit_button = Button(root, padx = int((screen_width*0.83)/100), pady = int((screen_height*0.46)/100), text = "Confirm", fg = text_light, bg = button_bg,relief = SOLID, command = lambda: [Confirm(remaining_cash), var.set(1)], borderwidth = 0)
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
    print(result)


    
def display_result(result):
    global my_tree
    my_tree = ttk.Treeview(root)
    # global mylabel
    # mylabel = Label(root, text = "STATUS",bg = bg, fg = text_dark, relief="solid", width = int((screen_width*0.521)/100), height = 2)
    # mylabel.configure(font=("Arial", 18, 'bold'))
    # mylabel.pack()
    # mylabel.place(x = (screen_width*59.9)/100, y = (screen_height*5)/100)

    # global status
    # status = Label(root, pady = 2, text = result["status"],bg = bg, fg = text_dark, relief="solid", width = int((screen_width*1.04)/100), height = 2)
    # status.configure(font=("Arial", 18))
    # status.pack()
    # status.place(x = (screen_width*68.75)/100, y = (screen_height*5)/100)
    
    # global mylabe3
    # mylabe3 = Label(root,padx = int((screen_width*0.989)/100), text = "CHANGE",bg = bg, fg = text_dark, relief="solid", width = int((screen_width*1.6)/100), height = 2)
    # mylabe3.configure(font=("Arial", 18, 'bold'))
    # mylabe3.pack()
    # mylabe3.place(x = (screen_width*59.9)/100, y = (screen_height*11.5)/100)
    
    list = result["change"]
    my_tree = ttk.Treeview(root, height=12, columns = ("STATUS", "CHANGE", "Change"), show = 'headings') 
    my_tree.heading("STATUS", text = "STATUS")
    my_tree.heading("CHANGE", text = "CHANGE")
    my_tree.column("CHANGE", width = 270)
    my_tree.column("STATUS",width = 300, anchor=CENTER)
    style = ttk.Style()
    style.configure("Treeview", rowheight = 40, background = "Silver", fieldbackground = "Silver")
    style.configure("Treeview.Heading", font=('Arial', 22))
    
    count = 0
    string = result["status"]

    # if(count==0):
    #     my_tree.insert( parent = '', index = 'end', text = "", values = (""), tags = "status")
    #     my_tree.tag_configure('status', font = ("Arial", 18))
    if(string == "INSUFFICIENT_FUNDS"):
        i = 0

        while(i<2):
            if(i==1):
                my_tree.insert( parent = '', index = 'end', iid = i, text = "", values = (string), tags = "status")
                my_tree.tag_configure('status', font = ("Arial", 18))
            else:
               my_tree.insert( parent = '', index = 'end', iid = i, text = "", values = (" ", " ", " "), tags = "status") 
            i+=1


    for record in list:
        if(count==0):
            my_tree.insert( parent = '', index = 'end', text = "", values = (" ", " ", " "), tags = "status")
            my_tree.insert( parent = '', index = 'end', iid = count, text = "", values = (string, record[0], record[1]), tags = "row")
            my_tree.tag_configure('row', font = ("Arial", 18))
        # elif(count==1):
        #     my_tree.insert( parent = '', index = 'end', iid = count, text = "", values = (string, record[0], record[1]), tags = "row")
        #     my_tree.tag_configure('row', font = ("Arial", 18))
        else:
            my_tree.insert( parent = '', index = 'end', iid = count, text = "", values = (" ", record[0], record[1]), tags = "row")
            my_tree.tag_configure('row', font = ("Arial", 18))
        count +=1
    my_tree.place(x = (screen_width*44.9)/100, y = (screen_height*9)/100)
    
    # global array
    # array = []
    # n = int((screen_height*17.7)/100)
    # for i in range(len(list)):
    #     mylabe4 = Label(root, text = list[i][0],bg = bg, fg = text_dark, relief="solid", padx = int((screen_width*1.042)/100), width = 15, height = 2)
    #     mylabe4.configure(font=("Arial", 18))
    #     mylabe4.pack()
    #     mylabe4.place(x = int((screen_width*59.9)/100), y = n)
    #     array.append(mylabe4)

    #     mylabe5 = Label(root, text = list[i][1],bg = bg, fg = text_dark, relief="solid", padx = int((screen_width*0.6)/100), width = 15, height = 2)
    #     mylabe5.configure(font=("Arial", 18))
    #     mylabe5.pack()
    #     mylabe5.place(x = (screen_width*73)/100, y = n)
    #     array.append(mylabe5)
    #     n+=(screen_height*6.4)/100
    
yes_button = Button(root, padx = int((screen_width*0.885)/100), text="Yes", pady = int((screen_height*0.46)/100),borderwidth=0, bg=button_bg, fg=text_light, command=Yes)
yes_button.configure(font=("Arial", int((screen_width*0.729)/100)))
yes_button.pack()
yes_button.place(x = (screen_width*16.4)/100, y = (screen_height*27.3)/100)

no_button = Button(root,padx = int((screen_width*0.88)/100), text="No", pady = int((screen_height*0.46)/100), borderwidth=0, bg=button_bg, fg=text_light, command=No)
no_button.configure(font=("Arial", int((screen_width*0.73)/100)))
no_button.pack()
no_button.place(x = (screen_width*24)/100, y = (screen_height*27.3)/100)

def reset():
    global data
    data = []
    # mylabel.destroy()
    # status.destroy() 
    # mylabe3.destroy()
    Amount_due_entry.delete(0, END)
    Cash_given_entry.delete(0, END)
    if(submit_button != ''):
        submit_button.destroy()

    for items in input_fields_list:
        items.destroy()   
    # for item in array:
    #     item.destroy()
    my_tree.destroy()

reset_button = Button(root, text = "Reset",padx = int((screen_width*1.04)/100), pady = int((screen_height*0.55)/100), borderwidth=0, bg = button_bg, fg = text_light, command = reset)
reset_button.configure(font=("Arial", int((screen_width*0.833)/100)))
reset_button.pack()
reset_button.place(x = (screen_width*79.9)/100, y = (screen_height*69.5)/100)

root.mainloop()
