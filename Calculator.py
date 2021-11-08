# Import packages
from tkinter import *
import math

# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Function to calculate trigonometric numbers of an angle
def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

# Function to find the square root of a number
def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

# Function to change the sign of number
def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    

# Function to calculate the percentage of a number
def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

# Funtion to find the result of an operation
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op

'''
Variables
'''
sin, cos, tan = math.sin, math.cos, math.tan

tk_calc = Tk()
tk_calc.configure(bg="#001a4d", bd=10)
tk_calc.title("Calculator")

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, bg='#BBB', justify='right').grid(columnspan=4, padx=10, pady=20) 

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#1f1f2e', 'font':('sans-serif', 20, 'bold')}
button_params_op={'bd':5, 'fg':'#0052cc', 'bg':'#1f1f2e', 'font':('sans-serif', 20, 'bold')}

'''
Buttons
'''
#--1st row--
delete_one = Button(tk_calc, bd=5, fg='#0052cc', font=('sans-serif',20,'bold'),
              text='DEL', command=button_delete, bg='#1f1f2e').grid(row=1, column=0, sticky="nsew")
delete_all = Button(tk_calc, bd=5, fg='#0052cc', font=('sans-serif', 20, 'bold'),
              text='C', command=button_clear_all, bg='#1f1f2e').grid(row=1, column=1, sticky="nsew")
# Change the sign of a number
signs = Button(tk_calc, button_params_op, text='±',
               command=sign_change).grid(row=1, column=2, sticky="nsew")
# nth root of a number
nth_root = Button(tk_calc, button_params_op, text='√',
                  command=square_root).grid(row=1, column=3, sticky="nsew")

#--2rd row--
# Sine of an angle in degrees
sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin).grid(row=2, column=0, sticky="nsew")
# Cosine of an angle in degrees
cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos).grid(row=2, column=1, sticky="nsew")
# Tangent of an angle in degrees
tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan).grid(row=2, column=2, sticky="nsew")
#--3th row--
add = Button(tk_calc, button_params_op, text='+',
             command=lambda:button_click('+')).grid(row=2, column=3, sticky="nsew")

#--4th row--
mul = Button(tk_calc, button_params_op, text='*',
             command=lambda:button_click('*')).grid(row=3, column=3, sticky="nsew")
button_7 = Button(tk_calc, button_params, text='7',
                  command=lambda:button_click('7')).grid(row=3, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params, text='8',
                  command=lambda:button_click('8')).grid(row=3, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params, text='9',
                  command=lambda:button_click('9')).grid(row=3, column=2, sticky="nsew")


#--5th row--
button_4 = Button(tk_calc, button_params, text='4',
                  command=lambda:button_click('4')).grid(row=4, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params, text='5',
                  command=lambda:button_click('5')).grid(row=4, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params, text='6',
                  command=lambda:button_click('6')).grid(row=4, column=2, sticky="nsew")
div = Button(tk_calc, button_params_op, text='/',
             command=lambda:button_click('/')).grid(row=4, column=3, sticky="nsew")

#--6th row--
button_1 = Button(tk_calc, button_params, text='1',
                  command=lambda:button_click('1')).grid(row=5, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params, text='2',
                  command=lambda:button_click('2')).grid(row=5, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params, text='3',
                  command=lambda:button_click('3')).grid(row=5, column=2, sticky="nsew")
sub = Button(tk_calc, button_params_op, text='-',
             command=lambda:button_click('-')).grid(row=5, column=3, sticky="nsew")

#--7th row--
# Transform number to percentage
percentage = Button(tk_calc, button_params, text='%',
               command=percent).grid(row=6, column=0, sticky="nsew")
button_0 = Button(tk_calc, button_params, text='0',
                  command=lambda:button_click('0')).grid(row=6, column=1, sticky="nsew")
point = Button(tk_calc, button_params, text='.',
               command=lambda:button_click('.')).grid(row=6, column=2, sticky="nsew")
equal = Button(tk_calc, button_params_op, text='=',
               command=button_equal).grid(row=6, column=3, sticky="nsew")

tk_calc.mainloop()
