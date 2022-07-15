from tkinter import *
from tkinter import font as f
from tkinter.messagebox import *
from types import FunctionType
import os

def GetRoot(title='ShrtCde window', size='500x500', image=None, mktoplevel=None, **kwargs):
    """
        Author: Udayshankar R

        Creates a Tkinter window and returns "root".

        KWARGS: minsize: str, maxsize: str, resizable: str, bg: str
    """

    minsize = list(kwargs['minsize'].split('x')) if 'minsize' in kwargs else ['0', '0']
    for i in range(len(minsize)): minsize[i] = int(minsize[i])
    maxsize = list(kwargs['maxsize'].split('x')) if 'maxsize' in kwargs else ['0', '0']
    for i in range(len(maxsize)): maxsize[i] = int(maxsize[i])

    resizeX = False if 'resizable' in kwargs and 'x' in kwargs['resizable'] else True
    resizeY = False if 'resizable' in kwargs and 'y' in kwargs['resizable'] else True
    
    bg = kwargs['bg'] if 'bg' in kwargs else None

    if mktoplevel == None: root = Tk()
    else: root = Toplevel(mktoplevel)

    root.title(title)
    root.geometry(size)
    root.resizable(resizeX, resizeY)

    if minsize != (0, 0): root.minsize(minsize[0], minsize[1])
    if maxsize != (0, 0): root.maxsize(maxsize[0], maxsize[1])

    if image != None:
        root.iconphoto(False, PhotoImage(file = image))

    if bg != None:
        root.config(bg=bg)
    
    return root

def GetMenu(root, commands):
    """
        Author: Udayshankar R

        Creates a menu for the tkinter window.
    """
    
    menu = Menu(root)

    # example
    # {"func" : lambda:print("lol"), "cascade" : {"func" : lambda:print("lol"), 0:0, ("func", "ctrl+lol") : lambda:print("lol")}}
    
    submenus = []
    if commands != {} and commands != None:
        for i in commands.keys():
            if isinstance(commands[i], FunctionType):
                menu.add_command(label=str(i), command=commands[i])
            elif isinstance(commands[i], dict):
                submenu = Menu(menu, tearoff=0)
                for j in commands[i].keys():
                    if j != 0: 
                        if isinstance(j, tuple): submenu.add_command(label=str(j[0]), accelerator=str(j[1]), command=commands[i][j])
                        else: submenu.add_command(label=str(j), command=commands[i][j])
                    else: submenu.add_separator()
                
                submenus.append(submenu)
                menu.add_cascade(label=i, menu=submenu)

    root.config(menu=menu)
    return menu, submenus
        
def GetFont(family="Calibri", size=15, weight="normal", underline=0, overstrike=0, slant="roman"):
    """
        Author: Udayshankar R

        Creates and returns a Tkinter.Font font. Default = Calibri.
    """

    font = f.Font(family=family, size=size, weight=weight, underline=underline, overstrike=overstrike, slant=slant)

    return font

def GetLabel(root, **kwargs):
    """
        Author: Udayshankar R

        Creates and returns a Tkinter label. If image path is included, also returns image object.

        KWARGS: text:str, image: str, imagewidth: int, imageheight:int, width: int, height: int, font: tkinter.font, border: int, relief: str, fg: str, bg: str, highlight: str, highlightsize: int
    """
    
    label = Label(root)

    border = kwargs['border'] if 'border' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else GetFont()

    fg = kwargs['fg'] if 'fg' in kwargs else "Black"

    width = kwargs['width'] if 'width' in kwargs else None
    height = kwargs['height'] if 'height' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    text = kwargs['text'] if 'text' in kwargs else None
    image = kwargs['image'] if 'image' in kwargs else None
    image_width = kwargs['imagewidth'] if 'imagewidth' in kwargs else None
    image_height = kwargs['imageheight'] if 'imageheight' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None
    highlight = kwargs['highlight'] if 'highlight' in kwargs else None
    highlightsize = kwargs['highlightsize'] if 'highlightsize' in kwargs else None

    img = None
    if text != None:
        label = Label(root, text=text, font=font, fg=fg)
    elif image != None:
        img = PhotoImage(file=image)

        if image_width != None: img.config(width=image_width)
        if image_height != None: img.config(height=image_height)
        
        label = Label(root)
        label.config(image=img)
        label.image = img
    
    label.config(border=border)
    if width != None: label['width'] = width
    if height != None: label['height'] = height
    if relief != None: label['relief'] = relief
    if bg != None: label['bg'] = bg
    if highlight != None: label['highlightbackground'] = highlight
    if highlightsize != None: label['highlightthickness'] = highlightsize

    if img == None: return label
    else: return label, img

def GetText(root, **kwargs):
    """
        Author: Udayshankar R

        Creates and returns a Tkinter text widget.

        KWARGS: default:str, width: int, height: int, font: tkinter.font, border: int, relief: str, insertwidth: int, insertfg: str, fg: str, bg: str, highlight: str, activehighlight: str, highlightsize: int
    """
    
    textobject = Text(root)

    border = kwargs['border'] if 'border' in kwargs else 1
    insertwidth = kwargs['insertwidth'] if 'insertwidth' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else GetFont()

    insertfg = kwargs['insertfg'] if 'insertfg' in kwargs else "Black"
    fg = kwargs['fg'] if 'fg' in kwargs else "Black"
    bg = kwargs['bg'] if 'bg' in kwargs else "White"
    default = kwargs['default'] if 'default' in kwargs else ""

    width = kwargs['width'] if 'width' in kwargs else None
    height = kwargs['height'] if 'height' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    highlight = kwargs['highlight'] if 'highlight' in kwargs else None
    activehighlight = kwargs['activehighlight'] if 'activehighlight' in kwargs else None
    highlightsize = kwargs['highlightsize'] if 'highlightsize' in kwargs else None

    textobject.config(font=font, border=border, insertwidth=insertwidth, insertbackground=insertfg, fg=fg, bg=bg)
    
    if width != None: textobject.config(width=width)
    if height != None: textobject.config(height=height)
    if relief != None: textobject.config(relief=relief)
    if highlight != None: textobject.config(highlightbackground=highlight)
    if activehighlight != None: textobject.config(highlightcolor=activehighlight)
    if highlightsize != None: textobject.config(highlightthickness=highlightsize)

    textobject.insert('0.0', default)

    return textobject

def GetButton(root, **kwargs):
    """
        Author: Udayshankar R

        Creates and returns a tkinter button which responds to function. If image path is included, also returns image object.

        KWARGS: function: function, text:str, image: str, imagewidth: int, imageheight:int, width: int, height: int, font: tkinter.font, border: int, relief: str, fg: str, bg: str, activefg: str, activebg: str
    """

    button = Button(root)

    border = kwargs['border'] if 'border' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else GetFont()

    fg = kwargs['fg'] if 'fg' in kwargs else "Black"
    activefg = kwargs['activefg'] if 'activefg' in kwargs else "Black"

    function = kwargs['function'] if 'function' in kwargs else None
    text = kwargs['text'] if 'text' in kwargs else None
    image = kwargs['image'] if 'image' in kwargs else None
    width = kwargs['width'] if 'width' in kwargs else None
    height = kwargs['height'] if 'height' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None
    activebg = kwargs['activebg'] if 'activebg' in kwargs else None
    image_width = kwargs['imagewidth'] if 'imagewidth' in kwargs else None
    image_height = kwargs['imageheight'] if 'imageheight' in kwargs else None

    img = None
    if text != None:
        button = Button(root, text=text, font=font)
    elif image != None:
        img = PhotoImage(file=image)

        if image_width != None: img.config(width=image_width)
        if image_height != None: img.config(height=image_height)
        
        button = Button(root)
        button.config(image=img)
        button.image = img

    button.config(border=border, fg=fg, activeforeground=activefg)
    if function != None: button.config(command=function)
    if width != None: button['width'] = width
    if height != None: button['height'] = height
    if relief != None: button['relief'] = relief
    if bg != None: button['bg'] = bg
    if activebg != None: button['activebackground'] = activebg
        
    if img == None: return button
    else: return button, img

def GetDropdown(root, options, **kwargs):
    """
        Author: Udayshankar R

        Creates and returns a tkinter dropdown with StringVar.

        KWARGS: vartype: str/int/float/bool, function: function, width: int, height: int, font: tkinter.font, border: int, relief: str, fg: str, bg: str, activefg: str, activebg: str, highlight: str, highlightsize: int
    """

    border = kwargs['border'] if 'border' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else GetFont()

    fg = kwargs['fg'] if 'fg' in kwargs else "Black"
    activefg = kwargs['activefg'] if 'activefg' in kwargs else "Black"

    vartype = kwargs['vartype'] if 'vartype' in kwargs else None
    function = kwargs['function'] if 'function' in kwargs else None
    width = kwargs['width'] if 'width' in kwargs else None
    height = kwargs['height'] if 'height' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None
    activebg = kwargs['activebg'] if 'activebg' in kwargs else None
    highlight = kwargs['highlight'] if 'highlight' in kwargs else None
    highlightsize = kwargs['highlightsize'] if 'highlightsize' in kwargs else None

    if isinstance(vartype, int): clicked = IntVar()
    elif isinstance(vartype, float): clicked = DoubleVar()
    elif vartype == 'BOOL': clicked = BooleanVar()
    elif vartype == None or isinstance(vartype, str): clicked = StringVar(root)

    def call_function(x):
        if function != None: function()
        pass

    clicked.set(options[0])
    dropdown = OptionMenu(root, clicked, *options, command=call_function)

    dropdown.config(font=font, fg=fg, activeforeground=activefg, border=border)

    if width != None: dropdown['width'] = width
    if height != None: dropdown['height'] = height
    if relief != None: dropdown['relief'] = relief
    if bg != None: dropdown['bg'] = bg
    if activebg != None: dropdown['activebackground'] = activebg
    if highlight != None: dropdown['highlightbackground'] = highlight
    if highlightsize != None: dropdown['highlightthickness'] = highlightsize

    dropdown.pack()

    return dropdown, clicked

def GetEntry(root, **kwargs):
    """
        Author: Udayshankar R

        Creates and returns a tkinter entry with StringVar.

        KWARGS: default:str, width: int, font: tkinter.font, border: int, relief: str, insertwidth: int, insertfg: str, fg: str, bg: str, highlight: str, activehighlight: str, highlightsize: int
    """
    
    intext = StringVar(root)
    entry = Entry(root, textvariable=intext)

    border = kwargs['border'] if 'border' in kwargs else 1
    insertwidth = kwargs['insertwidth'] if 'insertwidth' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else GetFont()

    default = kwargs['default'] if 'default' in kwargs else ""
    insertfg = kwargs['insertfg'] if 'insertfg' in kwargs else "Black"
    fg = kwargs['fg'] if 'fg' in kwargs else "Black"

    width = kwargs['width'] if 'width' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None
    highlight = kwargs['highlight'] if 'highlight' in kwargs else None
    activehighlight = kwargs['activehighlight'] if 'activehighlight' in kwargs else None
    highlightsize = kwargs['highlightsize'] if 'highlightsize' in kwargs else None

    entry.config(width=width, font=font, border=border, insertbackground=insertfg, insertwidth=insertwidth, fg=fg)

    if width != None: entry['width'] = width
    if relief != None: entry['relief'] = relief
    if bg != None: entry['bg'] = bg
    if highlight != None: entry['highlightbackground'] = highlight
    if activehighlight != None: entry['highlightcolor'] = activehighlight
    if highlightsize != None: entry['highlightthickness'] = highlightsize

    intext.set(default)

    return entry, intext
