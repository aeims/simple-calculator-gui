from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Simple Calculator')

entry = Entry(root, width=45, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


signs = ('+', '*', '/')


def btn_click(char):
    cur_val = entry.get()
    entry_clear()
    if cur_val == '0' and char not in signs:
        entry.insert(0, char)
    elif cur_val == '0' and char in signs:
        entry.insert(0, '0')
    elif char in signs and cur_val == '':
        pass
    else:
        entry.insert(0, cur_val + str(char))


def entry_clear():
    entry.delete(0, END)


def entry_del():
    val = entry.get()
    entry_clear()
    entry.insert(0, val[0:-1])


def calc():
    if entry.get() != '':
        try:
            ans = eval(entry.get())
            entry_clear()
            entry.insert(0, ans)
        except ZeroDivisionError:
            entry_clear()
            messagebox.showerror('Error', 'Can not devide by zero!')
            if not messagebox.askretrycancel('Simple Calculator', 'Try again?'):
                root.destroy()
        except SyntaxError:
            entry_clear()
            messagebox.showerror('Error', 'Something is wrong!')
            if not messagebox.askretrycancel('Simple Calculator', 'Try again?'):
                root.destroy()


btn_1 = Button(root, text='1', padx=40, pady=20, fg='black', bg='#E8E8E8', command=lambda: btn_click(1))
btn_2 = Button(root, text='2', padx=40, pady=20, fg='black', bg='#E8E8E8', command=lambda: btn_click(2))
btn_3 = Button(root, text='3', padx=40, pady=20, fg='black', bg='#E8E8E8', command=lambda: btn_click(3))
btn_4 = Button(root, text='4', padx=40, pady=20, fg='black', bg='#E8E8E8',  command=lambda: btn_click(4))
btn_5 = Button(root, text='5', padx=40, pady=20, fg='black', bg='#E8E8E8',  command=lambda: btn_click(5))
btn_6 = Button(root, text='6', padx=40, pady=20, fg='black', bg='#E8E8E8',  command=lambda: btn_click(6))
btn_7 = Button(root, text='7', padx=40, pady=20, fg='black', bg='#E8E8E8',  command=lambda: btn_click(7))
btn_8 = Button(root, text='8', padx=40, pady=20, fg='black', bg='#E8E8E8',  command=lambda: btn_click(8))
btn_9 = Button(root, text='9', padx=40, pady=20, fg='black', bg='#E8E8E8',  command=lambda: btn_click(9))
btn_0 = Button(root, text='0', padx=40, pady=20, fg='black', bg='#E8E8E8',  command=lambda: btn_click(0))
btn_dot = Button(root, text='.', padx=42, pady=20, fg='black', bg='#E8E8E8',  command=lambda: btn_click('.'))
btn_clear = Button(root, text='C', padx=39, pady=20, fg='black', bg='#E8E8E8', command=entry_clear)

btn_subtract_sign = Button(root, text='─', padx=42, pady=10, fg='black', bg='#949493', command=lambda: btn_click('-'))
btn_add_sign = Button(root, text='+', padx=40, pady=10, fg='black', bg='#949493', command=lambda: btn_click('+'))
btn_multiply_sign = Button(root, text='x', padx=40, pady=10, fg='black', bg='#949493', command=lambda: btn_click('*'))
btn_devide_sign = Button(root, text='÷', padx=40, pady=10, fg='black', bg='#949493', command=lambda: btn_click('/'))

btn_equal_sign = Button(root, text='=', padx=44, pady=85, bg='#43ABFF', command=calc)

btn_del = Button(root, text='⌫', padx=40, pady=20, fg='black', bg='#949493', command=entry_del)


btn_1.grid(row=4,column=0)
btn_2.grid(row=4,column=1)
btn_3.grid(row=4,column=2)

btn_4.grid(row=3,column=0)
btn_5.grid(row=3,column=1)
btn_6.grid(row=3,column=2)

btn_7.grid(row=2,column=0)
btn_8.grid(row=2,column=1)
btn_9.grid(row=2,column=2)

btn_0.grid(row=5,column=0)
btn_dot.grid(row=5, column=1)
btn_clear.grid(row=5, column=2)

btn_equal_sign.grid(row=3, column=3, rowspan=3)



btn_multiply_sign.grid(row=1, column=0)
btn_devide_sign.grid(row=1, column=1)
btn_add_sign.grid(row=1, column=2)
btn_subtract_sign.grid(row=1, column=3)

btn_del.grid(row=2, column=3)

root.mainloop()