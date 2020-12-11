import os
from PIL import Image , ImageEnhance
import tkinter as tk
from tkinter import ttk
import random

N = random.randint(1,100)
n = str(N)




win = tk.Tk()
win.title('Photo Editor')

path_lable = ttk.Label(win , text = "Enter image path : ")
path_lable.grid(row = 0 , column = 0 , sticky = tk.W)

path_var = tk.StringVar()
path_entry = ttk.Entry(win , width = 18 , textvariable = path_var)
path_entry.grid(row = 0 , column = 1)
path_entry.focus()

file_type_lable = ttk.Label(win , text = "Convert image to : ")
file_type_lable.grid(row = 4 , column = 0 )

file_type_var = tk.StringVar()
file_type_combobox = ttk.Combobox(win , width = 15 , textvariable = file_type_var , state = 'readonly' )
file_type_combobox['values'] = ('PDF', 'PNG', 'JPG')
file_type_combobox.grid(row = 4 , column = 1)

colour_type_var = tk.StringVar()
colour_type_lable = ttk.Label(win , text = 'Set colour : ')
colour_type_lable.grid(row = 6 , column = 0 , sticky = tk.W )

colour_type_var = tk.StringVar()
colour_combobox = ttk.Combobox(win , width = 15 , textvariable = colour_type_var , state = "readonly")
colour_combobox['values'] = ('Black & White' , 'Orginal Colour' , 'Extra colour')
colour_combobox.grid(row = 6 , column = 1)

brightness_label = ttk.Label(win , text = "Set Brightness : ")
brightness_label.grid(row = 7 , column = 0 , sticky = tk.W)

brightness_var = tk.IntVar()
brightness_combobox = ttk.Combobox(win , width = 15 , textvariable = brightness_var , state = 'readonly')
brightness_combobox['values'] = (0,1,2,3)
brightness_combobox.current(1)
brightness_combobox.grid(row = 7, column = 1 )

sharp_image_lable = ttk.Label(win , text = "Set Sharpness : ")
sharp_image_lable.grid(row = 8 , column = 0 , sticky = tk.W)

sharp_var = tk.IntVar()
sharp_combobox = ttk.Combobox(win , width = 15 , textvariable = sharp_var , state = 'readonly')
sharp_combobox['values'] = (1,2,3,4,5,6,7,8,9,10)
sharp_combobox.current(0)
sharp_combobox.grid(row = 8 , column = 1)


contrast_lable = ttk.Label(win , text = "Set Contrast : ")
contrast_lable.grid(row = 9 , column = 0 , sticky = tk.W)

contrast_vaar = tk.IntVar()
contrast_combobox = ttk.Combobox(win , width = 15 , textvariable = contrast_vaar , state = 'readonly')
contrast_combobox['values'] = (0,1,2,3)
contrast_combobox.current(1)
contrast_combobox.grid(row = 9 , column = 1)

size_lable = ttk.Label(win , text = 'Reduce  size : ')
size_lable.grid(row = 10 , column = 0 , sticky = tk.W)

size_type = tk.StringVar()
size_radiobutton = ttk.Radiobutton(win , text = 'Low' , value = 'Low' , variable = size_type)
size_radiobutton.grid(row = 11 , column = 0)

size_radiobutton1 = ttk.Radiobutton(win , text = 'Medium' , value = 'Medium' , variable = size_type)
size_radiobutton1.grid(row = 11 , columnspan = 7)

size_radiobutton2 = ttk.Radiobutton(win , text = 'High' , value = 'High' , variable = size_type)
size_radiobutton2.grid(row = 11 , column = 2)


def action():
    path = path_var.get()
    img = Image.open(path)

    if file_type_var.get() == 'PDF':
        print(img.save('newfile'+n+'.pdf'))
    elif file_type_var.get() == "PNG":
        print(img.save('newimage'+n+'.png'))
    else:
        print()
        # print(img.save('newimage'+n+'.jpg'))

    if colour_type_var.get() == "Black & White":
        colour_change = ImageEnhance.Color(img)
        colour_change.enhance(0).save('newimage'+n+'.jpg')
    elif colour_type_var.get() == "Orginal Colour":
        colour_change = ImageEnhance.Color(img)
        # colour_change.enhance(1).save('newimage'+n+'.jpg')
    elif colour_type_var.get() == "Extra colour":
        colour_change = ImageEnhance.Color(img)
        colour_change.enhance(2).save('newimage'+n+'.jpg')

    
    

def brightness():
    path = path_var.get()
    img = Image.open(path)
    if brightness_var.get() == 1:
        print()
    else:
        brightness_change = ImageEnhance.Brightness(img)
        brightness_change.enhance(brightness_var.get()).save('newimage2'+n+'.jpg')

    

def sharpness():
    path = path_var.get()
    img = Image.open(path)
    if sharp_var.get() == 1:
        print()
    else:
        sharp_change = ImageEnhance.Sharpness(img)
        sharp_change.enhance(sharp_var.get()).save('newimage3'+n+'.jpg')

    

def contrast():
    path = path_var.get()
    img = Image.open(path)
    if contrast_vaar.get() == 1:
        print()
    else:
        contrast_change = ImageEnhance.Contrast(img)
        contrast_change.enhance(contrast_vaar.get()).save('newimage4'+n+'.jpg')

    

all_function = lambda : [action(),brightness(),sharpness(),contrast()]

submit_button = ttk.Button(win , text = 'Edit' ,command = all_function)
submit_button.grid(row = 12 , columnsp = 5)












win.mainloop()
