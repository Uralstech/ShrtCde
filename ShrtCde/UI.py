"""
    Author: Uralstech (Udayshankar Ravikumar)
    
    GitHub: https://github.com/Uralstech/ShrtCde

    A UI module for Tkinter GUI.
"""

from tkinter import *
from tkinter import font as f
from tkinter.messagebox import *
from typing import Literal, TypeAlias, Union
from types import FunctionType

_TKObject: TypeAlias = Union[Tk, Toplevel]
_Rootvar: TypeAlias = Union[Tk, None]
_Booleanvar: TypeAlias = Literal[0, 1]
_Intvar: TypeAlias = Union[int, float]
_Listvar: TypeAlias = Union[list, tuple]
_Textvar: TypeAlias = Union[str, None]
_Weightvar: TypeAlias = Literal['normal', 'bold']
_Slantvar: TypeAlias = Literal['roman', 'italic']
_Orientvar: TypeAlias = Literal["horizontal", "vertical"]


def mkRoot(title='ShrtCde window', size='500x500', image: _Textvar=None, mktoplevel: _Rootvar=None, **kwargs) -> _TKObject:
    """
        Creates a Tkinter window and returns the Tk / Toplevel object.

        Parameters
        ----------

        - ``title``: (string) Title for the window.
        - ``size``: (string) Size of the window (widthxheight).
        - ``image``: (string) Path to image icon for the window (PNG).
        - ``mktoplevel``: (Tk window) If not None, function will return a Toplevel window; Otherwise a Tk window.

        KWARGS:
        -------

        - ``minsize``: (string) Minimum size for the window (widthxheight)
        - ``maxsize``: (string) Maximum size for the window (widthxheight)
        - ``resizable``: (string) Resize settings for the window.
                - ``'x'``: (string) Makes X axis of the window non-resizable.
                - ``'y'``: (string) Makes Y axis of the window non-resizable.
                - ``'xy'``: (string) Makes both X and Y axis of the window non-resizable.
        - ``bg``: (string) Background color of the window.
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
     
def mkFont(family="Calibri", size=15, weight: _Weightvar="normal", slant: _Slantvar="roman", underline: _Booleanvar=0, overstrike: _Booleanvar=0) -> f.Font:
    """
        Creates and returns a Tkinter font object.
        
        Parameters
        ----------

        - ``family``: (string) Font family for the font object.
        - ``size``: (integer) Size for the font object.
        - ``weight``: (string) Weight setting for the font object.
                - ``'normal'``: (string) Normal weight setting for the font object.
                - ``'bold'``: (string) Bold weight setting for the font object.
        - ``slant``: (string) Slant setting for the font object.
                - ``'roman'``: (string) Normal slant setting for the font object.
                - ``'italic'``: (string) Italic slant setting for the font object.
        - ``underline``: (integer) Underline setting for the font object.
                - ``0``: (integer) Removes underline setting for the font object.
                - ``1``: (integer) Adds underline setting for the font object.
        - ``overstrike``: (integer) Overstrike setting for the font object.
                - ``0``: (integer) Removes overstrike setting for the font object.
                - ``1``: (integer) Adds overstrike setting for the font object.
    """

    font = f.Font(family=family, size=size, weight=weight, underline=underline, overstrike=overstrike, slant=slant)

    return font

def mkMenu(root: _TKObject, commands: dict) -> tuple[Menu, list[Union[Menu, None]]]:
    """
        Creates a menu for the tkinter window. Returns the menu and a list of sub-menus, if any.

        Parameters
        ----------

        - ``root``: (Tk, Toplevel) Window object to which the menu will be attached.
        - ``command``: (dictionary) Dictionary with Name-Command pairs for the menu.
            - Example:
                - ``{"foo" : bar}``
                    - Creates item 'foo' which calls 'bar', a predefined function.
                - ``{"cascade" : {"foo" : bar}}``
                    - Creates a cacade menu called 'cascade' with item 'foo' which calls 'bar'.
                - ``{"cascade" : {"foo" : bar, 0:0, "quit" : bar}}``
                    - Creates seperator at '0:0' item in 'cascade'.
                - ``{"cascade" : {("foo", "faa") : bar}}``
                    - Creates item 'foo' with accelerator 'faa' which calls 'bar'.
        
        Confused? Try this snippet::

            from ShrtCde.UI import *
            func = lambda: print("foo")

            root = mkRoot()
            mkMenu(root, {"foo" : func, "cascade" : {"foo" : func, 0:0, ("foo", "faa") : func}})
            root.mainloop()
                        
    """
    
    menu = Menu(root)

    submenus = []
    if commands != {} and commands != None:
        for i in commands.keys():
            if isinstance(commands[i], FunctionType): menu.add_command(label=str(i), command=commands[i])
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

def mkLabel(root: _TKObject, text: _Textvar=None, image: _Textvar=None, **kwargs) -> Union[Label, tuple[Label, PhotoImage]]:
    """
        Creates and returns a Tkinter label. If image path is included, also returns image object.

        Parameters
        ----------

        - ``root``: (Tk, Toplevel) Window object to display the label on.
        - ``text``: (string) Text to display on the label.
        - ``image``: (string) Path to an image to display on the label.
        - NOTE: Only use text OR image. Both cannot be used.

        KWARGS:
        -------

        - ``width``: (float) Width of the label.
        - ``height``: (float) Height of the label.
        - ``imgwidth``: (float) Width of the label's image.
        - ``imgheight``: (float) Height of the label's image.
        - ``font``: (tkinter font) Font for the label's text.
        - ``border``: (float) Size of the label's border.
        - ``relief``: (string) Relief setting of the label. See tkinter manual.
                - ``'raised'``
                - ``'sunken'``
                - ``'flat'`` 
                - ``'ridge'``
                - ``'solid'``
                - ``'groove'``
        - ``fg``: (string) Color of the label's foreground.
        - ``bg``: (string) Color of the label's background.
        - ``hlcolor``: (string) Color of the label's highlight.
        - ``hlsize``: (float) Size of the label's highlight.
    """
    
    label = Label(root)

    border = kwargs['border'] if 'border' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else mkFont()

    fg = kwargs['fg'] if 'fg' in kwargs else "Black"

    width = kwargs['width'] if 'width' in kwargs else None
    height = kwargs['height'] if 'height' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    imgwidth = kwargs['imgwidth'] if 'imgwidth' in kwargs else None
    imgheight = kwargs['imgheight'] if 'imgheight' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None
    hlcolor = kwargs['hlcolor'] if 'hlcolor' in kwargs else None
    hlsize = kwargs['hlsize'] if 'hlsize' in kwargs else None

    img = None
    if text != None:
        label = Label(root, text=text, font=font, fg=fg)
    elif image != None:
        img = PhotoImage(file=image)

        if imgwidth != None: img.config(width=imgwidth)
        if imgheight != None: img.config(height=imgheight)
        
        label = Label(root)
        label.config(image=img)
        label.image = img
    
    label.config(border=border)
    if width != None: label['width'] = width
    if height != None: label['height'] = height
    if relief != None: label['relief'] = relief
    if bg != None: label['bg'] = bg
    if hlcolor != None: label['highlightbackground'] = hlcolor
    if hlsize != None: label['highlightthickness'] = hlsize

    if img == None: return label
    else: return label, img

def mkText(root: _TKObject, **kwargs) -> Text:
    """
        Creates and returns a Tkinter text widget.

        Parameters
        ----------

        - ``root``: (Tk, Toplevel) Window object to display the Text object on.

        KWARGS:
        -------

        - ``default``: (string) Default text for the Text object.
        - ``width``: (float) Width of the Text object.
        - ``height``: (float) Height of the Text object.
        - ``font``: (tkinter font) Font for the Text object's text.
        - ``border``: (float) Size of the Text object's border.
        - ``relief``: (string) Relief setting of the Text object. See tkinter manual.
                - ``'raised'``
                - ``'sunken'``
                - ``'flat'`` 
                - ``'ridge'``
                - ``'solid'``
                - ``'groove'``
        - ``cursorwidth``: (float) Width of the Text object's cursor.
        - ``cursorfg``: (string) Color of the Text object's cursor.
        - ``fg``: (string) Color of the Text object's foreground.
        - ``bg``: (string) Color of the Text object's background.
        - ``hlcolor``: (string) Color of the Text object's highlight.
        - ``activehlcolor``: (string) Color of the Text object's highlight when active.
        - ``hlsize``: (float) Size of the Text object's highlight.
    """
    
    text = Text(root)

    border = kwargs['border'] if 'border' in kwargs else 1
    cursorwidth = kwargs['cursorwidth'] if 'cursorwidth' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else mkFont()

    cursorfg = kwargs['cursorfg'] if 'cursorfg' in kwargs else "Black"
    fg = kwargs['fg'] if 'fg' in kwargs else "Black"
    bg = kwargs['bg'] if 'bg' in kwargs else "White"
    default = kwargs['default'] if 'default' in kwargs else ""

    width = kwargs['width'] if 'width' in kwargs else None
    height = kwargs['height'] if 'height' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    hlcolor = kwargs['hlcolor'] if 'hlcolor' in kwargs else None
    activehlcolor = kwargs['activehlcolor'] if 'activehlcolor' in kwargs else None
    hlsize = kwargs['hlsize'] if 'hlsize' in kwargs else None

    text.config(font=font, border=border, insertwidth=cursorwidth, insertbackground=cursorfg, fg=fg, bg=bg)
    
    if width != None: text.config(width=width)
    if height != None: text.config(height=height)
    if relief != None: text.config(relief=relief)
    if hlcolor != None: text.config(highlightbackground=hlcolor)
    if activehlcolor != None: text.config(highlightcolor=activehlcolor)
    if hlsize != None: text.config(highlightthickness=hlsize)

    text.insert('0.0', default)

    return text

def mkButton(root: _TKObject, text: _Textvar=None, image: _Textvar=None, **kwargs) -> Union[Button, tuple[Button, PhotoImage]]:
    """
        Creates and returns a tkinter button. If image path is included, also returns image object.

        Parameters
        ----------

        - ``root``: (Tk, Toplevel) Window object to display the button on.
        - ``text``: (string) Text to display on the button.
        - ``image``: (string) Path to an image to display on the button.
        - NOTE: Only use text OR image. Both cannot be used.

        KWARGS:
        -------

        - ``function``: (function) Function to assign to the button.
        - ``width``: (float) Width of the button.
        - ``height``: (float) Height of the button.
        - ``imgwidth``: (float) Width of the button's image.
        - ``imgheight``: (float) Height of the button's image.
        - ``font``: (tkinter font) Font for the button's text.
        - ``border``: (float) Size of the button's border.
        - ``relief``: (string) Relief setting of the button. See tkinter manual.
                - ``'raised'``
                - ``'sunken'``
                - ``'flat'`` 
                - ``'ridge'``
                - ``'solid'``
                - ``'groove'``
        - ``fg``: (string) Color of the button's foreground.
        - ``bg``: (string) Color of the button's background.
        - ``activefg``: (string) Color of the button's foreground when active.
        - ``activebg``: (string) Color of the button's background when active.
    """

    button = Button(root)

    border = kwargs['border'] if 'border' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else mkFont()

    fg = kwargs['fg'] if 'fg' in kwargs else "Black"
    activefg = kwargs['activefg'] if 'activefg' in kwargs else "Black"

    function = kwargs['function'] if 'function' in kwargs else None
    width = kwargs['width'] if 'width' in kwargs else None
    height = kwargs['height'] if 'height' in kwargs else None
    imgwidth = kwargs['imgwidth'] if 'imgwidth' in kwargs else None
    imgheight = kwargs['imgheight'] if 'imgheight' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None
    activebg = kwargs['activebg'] if 'activebg' in kwargs else None

    img = None
    if text != None:
        button = Button(root, text=text, font=font)
    elif image != None:
        img = PhotoImage(file=image)

        if imgwidth != None: img.config(width=imgwidth)
        if imgheight != None: img.config(height=imgheight)
        
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

def mkRadiobutton(root: _TKObject, variable: Union[StringVar, IntVar, DoubleVar, BooleanVar]=None, value=None, text: _Textvar=None, image: _Textvar=None, **kwargs) -> Union[Radiobutton, tuple[Radiobutton, PhotoImage]]:
    """
        Creates and returns a tkinter radio button. If image path is included, also returns image object.

        Parameters
        ----------

        - ``root``: (Tk, Toplevel) Window object to display the radio button on.
        - ``variable``: (StringVar, IntVar, DoubleVar, BooleanVar) The var which will be manipulated by the radio button.
        - ``value``: (Any) The value assigned to the radio button.
        - ``text``: (string) Text to display on the radio button.
        - ``image``: (string) Path to an image to display on the radio button.
        - NOTE: Only use text OR image. Both cannot be used.

        KWARGS:
        -------

        - ``indicator``: (integer) Indicator value of the radio button.
            - ``0``
            - ``1``
        - ``default``: (string) Default selected option of the radio button.
        - ``function``: (function) Function to assign to the radio button.
        - ``width``: (float) Width of the radio button.
        - ``height``: (float) Height of the radio button.
        - ``imgwidth``: (float) Width of the radio button's image.
        - ``imgheight``: (float) Height of the radio button's image.
        - ``font``: (tkinter font) Font for the radio button's text.
        - ``border``: (float) Size of the radio button's border.
        - ``relief``: (string) Relief setting of the radio button. See tkinter manual.
                - ``'raised'``
                - ``'sunken'``
                - ``'flat'`` 
                - ``'ridge'``
                - ``'solid'``
                - ``'groove'``
        - ``fg``: (string) Color of the radio button's foreground.
        - ``bg``: (string) Color of the radio button's background.
        - ``activefg``: (string) Color of the radio button's foreground when active.
        - ``activebg``: (string) Color of the radio button's background when active.
        - ``selectbg``: (string) Color of the radio button's background when selected.
    """

    border = kwargs['border'] if 'border' in kwargs else 1
    indicator = kwargs['indicator'] if 'indicator' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else mkFont()

    fg = kwargs['fg'] if 'fg' in kwargs else "Black"
    activefg = kwargs['activefg'] if 'activefg' in kwargs else "Black"
    activebg = kwargs['activebg'] if 'activebg' in kwargs else "White"
    selectbg = kwargs['selectbg'] if 'selectbg' in kwargs else "White"

    default = kwargs['default'] if 'default' in kwargs else None
    function = kwargs['function'] if 'function' in kwargs else None
    width = kwargs['width'] if 'width' in kwargs else None
    height = kwargs['height'] if 'height' in kwargs else None
    imgwidth = kwargs['imgwidth'] if 'imgwidth' in kwargs else None
    imgheight = kwargs['imgheight'] if 'imgheight' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None

    img = None
    if text != None:
        button = Radiobutton(root, text=text, font=font)
    elif image != None:
        img = PhotoImage(file=image)

        if imgwidth != None: img.config(width=imgwidth)
        if imgheight != None: img.config(height=imgheight)
        
        button = Radiobutton(root)
        button.config(image=img)
        button.image = img

    button.config(variable=variable, value=value, indicator=indicator, border=border, fg=fg, activeforeground=activefg, activebackground=activebg, selectcolor=selectbg)
    if default != None: variable.set(default)
    if function != None: button.config(command=function)
    if width != None: button['width'] = width
    if height != None: button['height'] = height
    if relief != None: button['relief'] = relief
    if bg != None: button['bg'] = bg
    
    if img == None: return button
    else: return button, img

def mkDropdown(root: _TKObject, options: _Listvar, **kwargs) -> tuple[OptionMenu, Union[IntVar, DoubleVar, BooleanVar, StringVar]]:
    """
        Creates and returns a tkinter dropdown with StringVar / IntVar / DoubleVar / BooleanVar.

        
        Parameters
        ----------

        - ``root``: (Tk, Toplevel) Window object to display the dropdown on.
        - ``options``: (list, tuple) Options for the dropdown.

        KWARGS:
        -------

        - ``vartype``: (string, integer, float) Object to tell the function what type of var to return.
            - ``None``, string: Tells function to return StringVar.
            - integer: Tells function to return IntVar.
            - float: Tells function to return FloatVar.
            - ``'BOOL'``: (string) Tells function to return BooleanVar.
        - ``function``: (function) Function to assign to the dropdown.
        - ``width``: (float) Width of the dropdown.
        - ``height``: (float) Height of the dropdown.
        - ``font``: (tkinter font) Font for the dropdown's text.
        - ``border``: (float) Size of the dropdown's border.
        - ``relief``: (string) Relief setting of the dropdown. See tkinter manual.
                - ``'raised'``
                - ``'sunken'``
                - ``'flat'`` 
                - ``'ridge'``
                - ``'solid'``
                - ``'groove'``
        - ``fg``: (string) Color of the dropdown's foreground.
        - ``bg``: (string) Color of the dropdown's background.
        - ``activefg``: (string) Color of the dropdown's foreground when active.
        - ``activebg``: (string) Color of the dropdown's background when active.
        - ``hlcolor``: (string) Color of the dropdown's highlight.
        - ``hlsize``: (float) Size of the dropdown's highlight.
    """

    border = kwargs['border'] if 'border' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else mkFont()

    fg = kwargs['fg'] if 'fg' in kwargs else "Black"
    activefg = kwargs['activefg'] if 'activefg' in kwargs else "Black"

    vartype = kwargs['vartype'] if 'vartype' in kwargs else None
    function = kwargs['function'] if 'function' in kwargs else None
    width = kwargs['width'] if 'width' in kwargs else None
    height = kwargs['height'] if 'height' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None
    activebg = kwargs['activebg'] if 'activebg' in kwargs else None
    hlcolor = kwargs['hlcolor'] if 'hlcolor' in kwargs else None
    hlsize = kwargs['hlsize'] if 'hlsize' in kwargs else None

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
    if hlcolor != None: dropdown['highlightbackground'] = hlcolor
    if hlsize != None: dropdown['highlightthickness'] = hlsize

    return dropdown, clicked

def mkEntry(root: _TKObject, **kwargs) -> tuple[Entry, StringVar]:
    """
        Creates and returns a tkinter entry with StringVar.
        
        Parameters
        ----------

        - ``root``: (Tk, Toplevel) Window object to display the Text object on.

        KWARGS:
        -------

        - ``default``: (string) Default text for the entry.
        - ``show``: (string) Character to show in place of actual entered characters in the entry.
            - Example:
                - ``show='*'``: Every character entered in the entry will be replaced with the *.
        - ``width``: (float) Width of the entry.
        - ``font``: (tkinter font) Font for the entry's text.
        - ``border``: (float) Size of the entry's border.
        - ``relief``: (string) Relief setting of the entry. See tkinter manual.
                - ``'raised'``
                - ``'sunken'``
                - ``'flat'`` 
                - ``'ridge'``
                - ``'solid'``
                - ``'groove'``
        - ``cursorwidth``: (float) Width of the entry's cursor.
        - ``cursorfg``: (string) Color of the entry's cursor.
        - ``fg``: (string) Color of the entry's foreground.
        - ``bg``: (string) Color of the entry's background.
        - ``hlcolor``: (string) Color of the entry's highlight.
        - ``activehlcolor``: (string) Color of the entry's highlight when active.
        - ``hlsize``: (float) Size of the entry's highlight.
    """
    
    intext = StringVar(root)
    entry = Entry(root, textvariable=intext)

    border = kwargs['border'] if 'border' in kwargs else 1
    cursorwidth = kwargs['cursorwidth'] if 'cursorwidth' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else mkFont()

    default = kwargs['default'] if 'default' in kwargs else ""
    cursorfg = kwargs['cursorfg'] if 'cursorfg' in kwargs else "Black"
    fg = kwargs['fg'] if 'fg' in kwargs else "Black"

    show = kwargs['show'] if 'show' in kwargs else None
    width = kwargs['width'] if 'width' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None
    hlcolor = kwargs['hlcolor'] if 'hlcolor' in kwargs else None
    activehlcolor = kwargs['activehlcolor'] if 'activehlcolor' in kwargs else None
    hlsize = kwargs['hlsize'] if 'hlsize' in kwargs else None

    entry.config(font=font, border=border, insertbackground=cursorfg, insertwidth=cursorwidth, fg=fg)

    if show != None: entry['show'] = show
    if width != None: entry['width'] = width
    if relief != None: entry['relief'] = relief
    if bg != None: entry['bg'] = bg
    if hlcolor != None: entry['highlightbackground'] = hlcolor
    if activehlcolor != None: entry['highlightcolor'] = activehlcolor
    if hlsize != None: entry['highlightthickness'] = hlsize

    intext.set(default)

    return entry, intext

def mkScale(root: _TKObject, start: _Intvar=0, end: _Intvar=1, orient: _Orientvar="horizontal", **kwargs) -> Scale:
    """
        Creates and returns a scale widget.

        Parameters
        ----------

        - ``root``: (Tk, Toplevel) Window object to display the scale on.
        - ``start``: (integer, float) Start position of the scale.
        - ``end``: (integer, float) End position of the scale.
        - ``orient``: (string) Orientation of the scale.
            - ``'horizontal'`` or tkinter constant ``HORIZONTAL``: (string) Sets scale to horizontal orientation.
            - ``'vertical'`` or tkinter constant ``VERTICAL``: (string) Sets scale to vertical orientation.

        KWARGS:
        -------

        - ``default``: (integer, float) Default position of the scale.
        - ``text``: (string) Text to show near the scale, depending on orientation.
        - ``mindist``: (integer, float) Minimum distance the scale can travel.
        - ``width``: (float) Width of the scale.
        - ``length``: (float) Length of the scale.
        - ``font``: (tkinter font) Font for the scale's text.
        - ``border``: (float) Size of the scale's border.
        - ``relief``: (string) Relief setting of the scale. See tkinter manual.
                - ``'raised'``
                - ``'sunken'``
                - ``'flat'`` 
                - ``'ridge'``
                - ``'solid'``
                - ``'groove'``
        - ``troughcolor``: (string) Color of the scale's trough.
        - ``fg``: (string) Color of the scale's foreground.
        - ``bg``: (string) Color of the scale's background.
        - ``activefg``: (string) Color of the scale's foreground when active.
        - ``hlcolor``: (string) Color of the scale's highlight.
        - ``hlsize``: (float) Size of the scale's highlight.
    """

    scale = Scale(root, from_=start, to=end, orient=orient)
    
    default = kwargs['default'] if 'default' in kwargs else 0
    mindist = kwargs['mindist'] if 'mindist' in kwargs else 1
    border = kwargs['border'] if 'border' in kwargs else 1

    font = kwargs['font'] if 'font' in kwargs else mkFont()

    text = kwargs['text'] if 'text' in kwargs else None
    width = kwargs['width'] if 'width' in kwargs else None
    length = kwargs['length'] if 'length' in kwargs else None
    relief = kwargs['relief'] if 'relief' in kwargs else None
    troughcolor = kwargs['troughcolor'] if 'troughcolor' in kwargs else None
    activefg = kwargs['activefg'] if 'activefg' in kwargs else None
    fg = kwargs['fg'] if 'fg' in kwargs else None
    bg = kwargs['bg'] if 'bg' in kwargs else None
    hlcolor = kwargs['hlcolor'] if 'hlcolor' in kwargs else None
    hlsize = kwargs['hlsize'] if 'hlsize' in kwargs else None

    scale.config(resolution=mindist, border=border, font=font)

    if text != None: scale['label'] = text
    if width != None: scale['width'] = width
    if length != None: scale['length'] = length
    if relief != None: scale['relief'] = relief
    if troughcolor != None: scale['troughcolor'] = troughcolor
    if activefg != None: scale['activebackground'] = activefg
    if fg != None: scale['fg'] = fg
    if bg != None: scale['bg'] = bg
    if hlcolor != None: scale['highlightbackground'] = hlcolor
    if hlsize != None: scale['highlightthickness'] = hlsize

    scale.set(default)

    return scale
