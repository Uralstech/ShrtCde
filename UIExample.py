from tkinter import filedialog
from ShrtCde.UI import *

# Feel free to mess around with the function values!

img_path = filedialog.askopenfilename(title="OPEN PNG")

___example___ = lambda:showinfo("EXAMPLE", "EXAMPLE")

root = GetRoot(title="EXAMPLE", size="900x900", minsize="200x200", maxsize="1200x1200", color="Yellow", image=img_path)
toplevel1 = GetRoot(title="EXAMPLE", size="300x300", resize='x', mktoplevel=root)
toplevel2 = GetRoot(title="EXAMPLE", size="300x300", resize='y', mktoplevel=root)
toplevel3 = GetRoot(title="EXAMPLE", size="300x300", resize='xy', mktoplevel=root)
GetMenu(root, {"func" : ___example___, "cascade" : {"func" : ___example___, 0:0, ("QUIT", "ctrl+q") : lambda:root.quit()}})

GetLabel(root, text="label", width=20, height=2, font=GetFont(family="Terminal", size=30, weight="bold"), border=5, relief="groove", fg="green", bg="red", highlight="blue", highlightsize=5).pack()

GetLabel(toplevel1, text="example label", width=40).pack()
a,b=GetLabel(toplevel1, image=img_path, imagewidth=200, imageheight=200, width=300, height=200)
print("line20: ", b.name, type(b))
a.pack()

a,b=GetLabel(root, image=img_path, width=300, height=200)
print("line24: ", b.name, type(b))
a.pack()
GetButton(root, function=___example___, text="button", width=20, height=2, font=GetFont(family="SimSun", size=30, weight="bold"), border=5, relief="groove", fg="green", bg="red", activefg="brown", activebg="pink").pack()

GetLabel(toplevel2, text="example button", width=40).pack()
a,b=GetButton(toplevel2, function=___example___, imagewidth=200, imageheight=200, image=img_path, width=300, height=200, activefg="green", activebg="yellow")
print("line30: ", b.name, type(b))
a.pack()

a,b=GetButton(root, function=___example___, image=img_path, width=300, height=200, activefg="blue", activebg="red")
print("line34: ", b.name, type(b))
a.pack()
text=GetText(root, text="EXAMPLE", width=50, height=20, font=GetFont(family="Consolas", size=20, weight="bold"), border=5, relief="raised", insertwidth=10, insertfg="red", fg="blue", bg="green", activehighlight="white", highlight="black", highlightsize=5)
text.bind("<KeyRelease>", lambda x: print("line37: ", text.get('0.0', 'end')))
text.pack()

entry,entryvar=GetEntry(toplevel3, default="EXAMPLE", width=15, font=GetFont(family="Times New Roman"), border=10, relief="sunken", insertwidth=20, insertfg="blue", fg="green", bg="red", highlight="yellow", activehighlight="pink", highlightsize=20)
entry.bind("<KeyRelease>", lambda x: print("line41: ", entryvar.get()))
entry.pack()

def show():
    showinfo("EXAMPLE", "line45:  " + str(dropvar.get()) + "\t" + str(type(dropvar)))

# Try changing "vartype" below.
#If it's an int, GetDropdown will return an IntVar,
#if it's a float GetDropdown will return a DoubleVar,
#if it is the str "BOOL" GetDropdown will return a BooleanVar,
#if it's None, or any other str, GetDropdown will return a StringVar.
drop,dropvar=GetDropdown(toplevel3, [1, 2, 3, 4, 5, 6], vartype=None, function=show, width=20, height=2, font=GetFont(family="OCR-A-BT", size=40), border=5, relief='groove', fg="red", bg="black", activefg="blue", activebg="yellow", highlight="blue", highlightsize=10)
drop.pack()

root.bind("<Control-q>", lambda x: root.quit())
root.mainloop()