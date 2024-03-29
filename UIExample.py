from tkinter import filedialog
from ShrtCde.UI import *

# Feel free to mess around with the function values!

img_path = filedialog.askopenfilename(title="OPEN PNG")

___example___ = lambda:showinfo("EXAMPLE", "EXAMPLE")

root = mkRoot("EXAMPLE", "900x900", img_path, minsize="200x200", maxsize="1200x1200", color="Yellow")
toplevel1 = mkRoot("EXAMPLE", "300x300", mktoplevel=root, resize='x')
toplevel2 = mkRoot("EXAMPLE", "300x670", mktoplevel=root, resize='y')
toplevel3 = mkRoot("EXAMPLE", "300x550", mktoplevel=root, resize='xy')
mkMenu(root, {"func" : ___example___, "cascade" : {"func" : ___example___, 0:0, "func2" : ___example___, 1:0, ("QUIT", "ctrl+q") : lambda:root.quit()}})

mkLabel(root, text="label", width=20, height=2, font=mkFont("Terminal", 30, "bold", underline=1), border=5, relief="groove", fg="green", bg="red", hlcolor="blue", hlsize=5).pack()

mkLabel(toplevel1, text="example label", width=40).pack()
a,b=mkLabel(toplevel1, image=img_path, imagewidth=200, imageheight=200, width=300, height=200)
print("line20: ", b.name, type(b))
a.pack()

a,b=mkLabel(root, image=img_path, width=300, height=200)
print("line24: ", b.name, type(b))
a.pack()
mkButton(root, function=___example___, text="button", width=20, height=2, font=mkFont("SimSun", 30, "bold", overstrike=1), border=5, relief="groove", fg="green", bg="red", activefg="brown", activebg="pink").pack()

mkLabel(toplevel2, text="example button", width=40).pack()
a,b=mkButton(toplevel2, function=___example___, imagewidth=200, imageheight=200, image=img_path, width=300, height=200, activefg="green", activebg="yellow")
print("line30: ", b.name, type(b))
a.pack()

a,b=mkButton(root, function=___example___, image=img_path, width=300, height=200, activefg="blue", activebg="red")
print("line34: ", b.name, type(b))
a.pack()
text=mkText(root, default="EXAMPLE", width=50, height=20, font=mkFont("Consolas", 30, "bold", "italic"), border=5, relief="raised", cursorwidth=10, cursorfg="red", fg="blue", bg="green", activehlcolor="white", hlcolor="black", hlsize=5)
text.bind("<KeyRelease>", lambda x: print("line37: ", text.get('0.0', 'end')))
text.pack()

entry,entryvar=mkEntry(toplevel3, default="EXAMPLE", width=15, font=mkFont("Times New Roman"), border=10, relief="sunken", cursorwidth=20, cursorfg="blue", fg="green", bg="red", hlcolor="yellow", activehlcolor="pink", hlsize=20)
entry.bind("<KeyRelease>", lambda x: print("line41: ", entryvar.get()))
entry.pack()

entry2,entryvar2=mkEntry(toplevel3, default="EXAMPLE", show='*', width=15, font=mkFont("Times New Roman"), border=10, relief="sunken", cursorwidth=20, cursorfg="blue", fg="green", bg="red", hlcolor="yellow", activehlcolor="pink", hlsize=20)
entry2.bind("<KeyRelease>", lambda x: print("line45: ", entryvar2.get()))
entry2.pack()

def show():
    showinfo("EXAMPLE", "line49:  " + str(dropvar.get()) + "\t" + str(type(dropvar)))

# Try changing "vartype" below.
#If it's an int, GetDropdown will return an IntVar,
#if it's a float GetDropdown will return a DoubleVar,
#if it is the str "BOOL" GetDropdown will return a BooleanVar,
#if it's None, or any other str, GetDropdown will return a StringVar.
drop,dropvar=mkDropdown(toplevel3, [1, 2, 3, 4, 5, 6], vartype=None, function=show, width=20, height=2, font=mkFont("OCR-A BT", 40), border=5, relief='groove', fg="red", bg="black", activefg="blue", activebg="yellow", hlcolor="blue", hlsize=10)
drop.pack()

slider=mkScale(toplevel3, 0, 1, HORIZONTAL, default=0.5, text="EXAMPLE", mindist=0.01, width=40, length=200, font=mkFont(size=30), border=5, relief="groove", troughcolor="blue", activefg="green", fg="red", bg="yellow", hlcolor="purple", hlsize=5)
slider.pack()

mkLabel(toplevel2, "RADIOBUTTON EXAMPLE").pack()
v = StringVar(toplevel2)
mkRadiobutton(toplevel2, v, "EXAMPLE 1", image="C:/users/asus/downloads/lambda.png", imgwidth=80, imgheight=80, indicator=1, function=lambda:print(v.get()), width=100, height=100, border=10, relief='flat', fg="red", bg="green", activefg="grey", activebg="red")[0].pack()
mkRadiobutton(toplevel2, v, "EXAMPLE 2", text="EXAMPLE 2", indicator=1, function=lambda:print(v.get()), font=mkFont("Arial Black"), width=20, height=2, border=10, relief='flat', fg="red", bg="green", activefg="grey", activebg="red", selectbg="green").pack()
mkRadiobutton(toplevel2, v, "EXAMPLE 3", image="C:/users/asus/downloads/lambda.png", imgwidth=80, imgheight=80, indicator=0, function=lambda:print(v.get()), width=100, height=100, border=10, relief='flat', fg="red", bg="green", activefg="grey", activebg="red", selectbg="green")[0].pack()
mkRadiobutton(toplevel2, v, "EXAMPLE 4", text="EXAMPLE 4", default="EXAMPLE 3", indicator=0, function=lambda:print(v.get()), font=mkFont("Arial Black"), width=20, height=2, border=10, relief='flat', fg="red", bg="green", activefg="grey", activebg="red").pack()

root.bind("<Control-q>", lambda x: root.quit())
root.mainloop()