import tkinter.ttk
from tkinter import *
import Conversiones as cV


def slide(value):
    r = r_scale.get()
    g = g_scale.get()
    b = b_scale.get()
    hexcode = cV.rgb_to_hex(r, g, b)
    colorLabel.config(bg=f'{hexcode}')
    labHex.config(text=f'hex: {hexcode}')

    labCMYK.config(text=f'{cV.rgb_to_cmyk(r, g, b)}')
    labHSV.config(text=f'{cV.rgb_to_hsv(r, g, b)}')
    labHLS.config(text=f'{cV.rgb_to_hls(r, g, b)}')


# Configuration de la ventana principal
root = Tk()
root.title("PyPicker")
root.geometry("280x250")
iconPict = PhotoImage(file="icon.png")
root.iconphoto(False, iconPict)
root.resizable(0, 0)

# Configuracion de encabezado
colorLabel = Label(root, bg="Black", width=280, height=2, bd=0, relief=FLAT)
colorLabel.grid(row=0, column=0, sticky=NS)

# Frame secundario para slidebars de RGB
secondaryFrame = Frame(root, bd=2, relief=FLAT)
secondaryFrame.grid(row=1, column=0, pady=0, padx=5, sticky=W + E)

# SlideBar Red
r_label = Label(secondaryFrame, text="R", fg="red", font=('arial', 10, 'bold'), relief=FLAT)
r_label.grid(row=0, column=0)
r_scale = Scale(secondaryFrame, from_=0, to=255, length=240, fg='red', orient=HORIZONTAL, command=slide)
r_scale.grid(row=0, column=1)

# SlideBar Green
g_label = Label(secondaryFrame, text="G", fg="Green", font=('arial', 10, 'bold'), relief=FLAT)
g_label.grid(row=1, column=0)
g_scale = Scale(secondaryFrame, from_=0, to=255, length=210, fg='Green', orient=HORIZONTAL, command=slide)
g_scale.grid(row=1, column=1, sticky=W + E)

# SlideBer Blue
b_label = Label(secondaryFrame, text="B", fg="Blue", font=('arial', 10, 'bold'), relief=FLAT)
b_label.grid(row=2, column=0)
b_scale = Scale(secondaryFrame, from_=0, to=255, length=210, fg='Blue', orient=HORIZONTAL, command=slide)
b_scale.grid(row=2, column=1, sticky=W + E)

# Frame para TabControl
tabFrame = Frame(root)
tabFrame.grid(row=2, column=0, sticky=W + E, padx=5)
tabControl = tkinter.ttk.Notebook(tabFrame)

# Tabs
tab1 = tkinter.ttk.Frame(tabControl)
tab2 = tkinter.ttk.Frame(tabControl)
tab3 = tkinter.ttk.Frame(tabControl)
tab4 = tkinter.ttk.Frame(tabControl)

# Adding tabs to tabFrame
tabControl.add(tab1, text='HEX')
tabControl.add(tab2, text='CMYK')
tabControl.add(tab3, text='HSV')
tabControl.add(tab4, text='HSL')
tabControl.pack(expand=4, fill="both")

# Adding controls to each tab
labHex = Label(tab1, text="")
labHex.grid(column=0, row=0)
labCMYK = Label(tab2, text="")
labCMYK.grid(column=0, row=0)
labHSV = Label(tab3, text="")
labHSV.grid(column=0, row=0)
labHLS = Label(tab4, text="")
labHLS.grid(column=0, row=0)

root.mainloop()
