
import tkinter as tk
import math
 
root = tk.Tk()
 
root.title('Simple Calculator')
root.geometry("295x310+150+150")
 
root.attributes("-alpha",0.9)
root["background"] = "#ffffff"
font = ('宋体', 20)
font_16 = ('宋体', 16)
result_num = tk.StringVar()
result_num.set('')
 
tk.Label(root,
          textvariable=result_num, font=font, height=2,
         width=20, justify=tk.LEFT, anchor=tk.SE
         ).grid(row=1, column=1, columnspan=4)
 
#buttons
button_clear = tk.Button(root, text='AC', width=5, font=font_16, relief=tk.FLAT, bg='#6495ed')
button_back = tk.Button(root, text='←', width=5, font=font_16, relief=tk.FLAT, bg='#6495ed')
button_division = tk.Button(root, text='÷', width=5, font=font_16, relief=tk.FLAT, bg='#c8c7c5')
button_multiplication = tk.Button(root, text='×', width=5, font=font_16, relief=tk.FLAT, bg='#c8c7c5')
button_clear.grid(row=2, column=1, padx=4, pady=2)
button_back.grid(row=2, column=2, padx=4, pady=2)
button_division.grid(row=2, column=3, padx=4, pady=2)
button_multiplication.grid(row=2, column=4, padx=4, pady=2)
 
button_seven = tk.Button(root, text='7', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_eight = tk.Button(root, text='8', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_nine = tk.Button(root, text='9', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_subtraction = tk.Button(root, text='-', width=5, font=font_16, relief=tk.FLAT, bg='#c8c7c5')
button_seven.grid(row=3, column=1, padx=4, pady=2)
button_eight.grid(row=3, column=2, padx=4, pady=2)
button_nine.grid(row=3, column=3, padx=4, pady=2)
button_subtraction.grid(row=3, column=4, padx=4, pady=2)
 
button_four = tk.Button(root, text='4', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_five = tk.Button(root, text='5', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_six = tk.Button(root, text='6', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_addition = tk.Button(root, text='+', width=5, font=font_16, relief=tk.FLAT, bg='#c8c7c5')
button_four.grid(row=4, column=1, padx=4, pady=2)
button_five.grid(row=4, column=2, padx=4, pady=2)
button_six.grid(row=4, column=3, padx=4, pady=2)
button_addition.grid(row=4, column=4, padx=4, pady=2)
 
button_one = tk.Button(root, text='1', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_two = tk.Button(root, text='2', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_three = tk.Button(root, text='3', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_equal = tk.Button(root, text='=', width=5, height = 5, font=font_16, relief=tk.FLAT, bg='#8fd1e1')
button_one.grid(row=5, column=1, padx=4, pady=2)
button_two.grid(row=5, column=2, padx=4, pady=2)
button_three.grid(row=5, column=3, padx=4, pady=2)
button_equal.grid(row=5, column=4, padx=4, pady=2, rowspan=3)
 
button_zero = tk.Button(root, text='0', width=12, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_point = tk.Button(root, text='.', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_zero.grid(row=6, column=1, padx=4, pady=2, columnspan=2)
button_point.grid(row=6, column=3, padx=4, pady=2)
 
button_sin = tk.Button(root, text='sin', width=5, font=font_16, relief=tk.FLAT, bg='#c8c7c5')
button_cos = tk.Button(root, text='cos', width=5, font=font_16, relief=tk.FLAT, bg='#c8c7c5')
button_tan = tk.Button(root, text='tan', width=5, font=font_16, relief=tk.FLAT, bg='#c8c7c5')
button_sin.grid(row=7, column=1, padx=4, pady=2)
button_cos.grid(row=7, column=2, padx=4, pady=2)
button_tan.grid(row=7, column=3, padx=4, pady=2)

def click_button(x):
    print('x:\t',x)
    result_num.set(result_num.get() + x)
 
def calculation():
    opt_str = result_num.get()
    result = eval(opt_str)
    result_num.set(str(result))
 
def back():
    opt_str=result_num.get()
    opt_str=opt_str[:-1]
    result_num.set(opt_str)
 
def clear():
    opt_str = ""
    result_num.set(opt_str)
 
def sin():
    opt_str = result_num.get()
    result = math.sin((float(opt_str)*math.pi)/180)
    result_num.set(str(result))
 
def cos():
    opt_str = result_num.get()
    result = math.cos((float(opt_str)*math.pi)/180)
    result_num.set(str(result))
 
def tan():
    opt_str = result_num.get()
    result = math.tan((float(opt_str)*math.pi)/180)
    result_num.set(str(result))
 
 
 
button_one.config(command=lambda: click_button('1'))
button_two.config(command=lambda: click_button('2'))
button_three.config(command=lambda: click_button('3'))
button_four.config(command=lambda: click_button('4'))
button_five.config(command=lambda: click_button('5'))
button_six.config(command=lambda: click_button('6'))
button_seven.config(command=lambda: click_button('7'))
button_eight.config(command=lambda: click_button('8'))
button_nine.config(command=lambda: click_button('9'))
button_zero.config(command=lambda: click_button('0'))
 
button_addition.config(command=lambda: click_button('+'))
button_subtraction.config(command=lambda: click_button('-'))
button_multiplication.config(command=lambda: click_button('*'))
button_division.config(command=lambda: click_button('/'))
button_point.config(command=lambda: click_button('.'))
button_back.config(command=lambda: click_button('←'))
button_clear.config(command=lambda: click_button(''))
button_equal.config(command=lambda: click_button('='))
 
button_sin.config(command=lambda: click_button('sin'))
button_cos.config(command=lambda: click_button('cos'))
button_tan.config(command=lambda: click_button('tan'))
 
button_back.config(command=back)
button_clear.config(command=clear)
button_sin.config(command=sin)
button_cos.config(command=cos)
button_tan.config(command=tan)
button_equal.config(command=calculation)
 
root.mainloop()