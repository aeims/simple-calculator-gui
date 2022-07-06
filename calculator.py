from tkinter import *
root = Tk()
root.title('simple calc')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.insert(0, 'enter number')

def calc_click(number):
    cur_val = e.get()
    e.delete(0, END)
    e.insert(0, str(cur_val) + str(number))

def calc_clear():
    e.delete(0, END)

def calc_add():
    first_number = e.get()
    global f_num
    global math 
    math = 'add'
    f_num = int(first_number)
    e.delete(0, END)

def calc_subtract():
    first_number = e.get()
    global f_num
    global math 
    math = 'sub'
    f_num = int(first_number)
    e.delete(0, END)

def calc_multiply():
    first_number = e.get()
    global f_num
    global math 
    math = 'multiply'
    f_num = int(first_number)
    e.delete(0, END)

def calc_devide():
    first_number = e.get()
    global f_num
    global math 
    math = 'devide'
    f_num = int(first_number)
    e.delete(0, END)

def calc_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'add':
        e.insert(0, f_num + int(second_number))
    elif math == 'sub':
        e.insert(0, f_num - int(second_number))
    elif math == 'devide':
        e.insert(0, f_num / int(second_number))
    else:
        e.insert(0, f_num * int(second_number))





btn_1 = Button(root, text='1', padx=40, pady=20, command=lambda: calc_click(1))
btn_2 = Button(root, text='2', padx=40, pady=20, command=lambda: calc_click(2))
btn_3 = Button(root, text='3', padx=40, pady=20, command=lambda: calc_click(3))
btn_4 = Button(root, text='4', padx=40, pady=20, command=lambda: calc_click(4))
btn_5 = Button(root, text='5', padx=40, pady=20, command=lambda: calc_click(5))
btn_6 = Button(root, text='6', padx=40, pady=20, command=lambda: calc_click(6))
btn_7 = Button(root, text='7', padx=40, pady=20, command=lambda: calc_click(7))
btn_8 = Button(root, text='8', padx=40, pady=20, command=lambda: calc_click(8))
btn_9 = Button(root, text='9', padx=40, pady=20, command=lambda: calc_click(9))
btn_0 = Button(root, text='0', padx=40, pady=20, command=lambda: calc_click(0))
btn_add_sign = Button(root, text='+', padx=39, pady=20, command=calc_add)
btn_subtract_sign = Button(root, text='─', padx=37, pady=10, command=calc_subtract)
btn_multiply_sign = Button(root, text='*', padx=41, pady=10, command=calc_multiply)
btn_devide_sign = Button(root, text='/', padx=41, pady=10, command=calc_devide)
btn_equal_sign = Button(root, text='=', padx=91, pady=20, command=calc_equal)
btn_clear = Button(root, text='Clear', padx=79, pady=20, command=calc_clear)

btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)

btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)

btn_0.grid(row=4,column=0)
btn_clear.grid(row=4, column=1, columnspan=2)
btn_add_sign.grid(row=5, column=0)
btn_equal_sign.grid(row=5, column=1, columnspan=2)

btn_subtract_sign.grid(row=6, column=0)
btn_multiply_sign.grid(row=6, column=1)
btn_devide_sign.grid(row=6, column=2)

root.mainloop()