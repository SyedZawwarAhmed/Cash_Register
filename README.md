# Cash Register

A Cash Register that accepts purchased price payment and cash in drawer, and displays the change based on the amount due and amount given entered by the user.

## Table of contents

- [Overview](#overview)
  - [Objective](#objective)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Overview

### Objective

- Users can enter the **amount due**, **amount given** and **cash in drawer** using input fields
- Users can see the **status key** and **change**
- If cash in drawer is less than the change due or the exact change can not be given then the status key will be **INSUFFICIENT FUNDS** and change key will be empty
- If cash in drawer is equal to the change then the change will be displayed and the status key will be **CLOSED**
- If cash in drawer is greater than change then the change will be displayed and the status key will be **OPEN** 
- Users can reset the inputs and results by clicking on the **reset button** but the cash in drawer will not be changed
- Users have the option to change the cash in drawer or go with the previous one everytime they calculate a new change


### Usage Demo

![](step1.png)
![](step2.png)
![](step3.png)
![](step4.png)
![](step5.png)
![](step6.png)
![](step7.png)

### Links

- Solution URL: [https://github.com/SyedZawwarAhmed/Cash_Register](https://github.com/SyedZawwarAhmed/Cash_Register)

## Our process

### Built with

- Python 
- Python(Tkinter)

### What We learned

While making this project, the most important thing which We learned is Tkinter library. We also learned how to display data in tables using tkinter treeview.

Here is the snippet of the treeview we used in this project
```py
my_tree = ttk.Treeview(root)   
list = result["change"]
my_tree = ttk.Treeview(root, height=12, columns = ("STATUS", "CHANGE", "Change"), show = 'headings') 
my_tree.heading("STATUS", text = "STATUS")
my_tree.heading("CHANGE", text = "CHANGE")
my_tree.column("CHANGE", width = 270)
my_tree.column("STATUS",width = 300, anchor=CENTER)
style = ttk.Style()
style.configure("Treeview", rowheight = 40, background = "Silver", fieldbackground = "Silver")
style.configure("Treeview.Heading", font=('Arial', 22))	
```

### Useful resources

- [Stack Overflow](https://www.stackoverflow.com) - As always, when we got stuck, stackoverflow helped me get through.
- [w3Schools](https://www.w3schools.com) - This is the best website for documentation with easily understandable code examples.

## Authors

- **Syed Zawwar Ahmed**
- **Muhammad Annas Baig**