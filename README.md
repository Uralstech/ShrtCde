# ShrtCde (ShortCode)
A small python library for lazy devs. This shortens the amount of code you have to write for your program with the help of functions.

## LICENSE
This project uses the Apache-2.0 license. For more info, check LICENSE.

## INSTALLATION
```
pip install ShrtCde
```
or
```
pip3 install ShrtCde
```

## EXAMPLE (IO MODULE)
An example for the IO module.

```
from ShrtCde.IO import *

# Feel free to mess around with the function values!

path = input("Enter file path (write): ")
data = input("Enter data to write: ")
encoding = input("Enter encoding of data: (default: utf-8)")
encoding = encoding if encoding != "" else "utf8"

split = " "
data = list(data.split(sep=split))

append = input("Append data? y/n: ")
if append == 'y': writef(path, data, 'a', encoding)
else: writef(path, data, 'w', encoding)

print('\n\n')

path = input("Enter file path (read): ")
encoding = input("Enter encoding of data: (default: utf-8)")
encoding = encoding if encoding != "" else "utf8"

if not findf(path):
    print("File was not found.")
    input()
    quit()

mode = input("Enter read mode:\n-r to read whole file as string\n-rl to read first line as string\n-rls ro read whole file as list\n: ")
data = readf(path, mode, encoding)
print(data, f"\n\n TYPE: {str(type(data))}")
input()
```

## EXAMPLE (UI MODULE)
An example for the UI module.

```
from tkinter import filedialog
from ShrtCde.UI import *

# Feel free to mess around with the function values!

img_path = filedialog.askopenfilename(title="OPEN PNG")

___example___ = lambda:showinfo("EXAMPLE", "EXAMPLE")

root = mkRoot("EXAMPLE", "900x900", img_path, minsize="200x200", maxsize="1200x1200", color="Yellow")
toplevel1 = mkRoot("EXAMPLE", "300x300", mktoplevel=root, resize='x')
toplevel2 = mkRoot("EXAMPLE", "300x300", mktoplevel=root, resize='y')
toplevel3 = mkRoot("EXAMPLE", "300x550", mktoplevel=root, resize='xy')
mkMenu(root, {"func" : ___example___, "cascade" : {"func" : ___example___, 0:0, ("QUIT", "ctrl+q") : lambda:root.quit()}})

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

root.bind("<Control-q>", lambda x: root.quit())
root.mainloop()
```

All examples will also be available in the GitHub repo.

### GITHUB
https://github.com/Uralstech/ShrtCde