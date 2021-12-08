import tkinter as tk
import sys
import os
from themes import Themes, Theme

THEME: Theme = Themes.LIGHT

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        Main.configure(self, bg=THEME.background)

        center_window(self)


class Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        Frame.configure(self, bg=THEME.background)


class Toplevel(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.configure(bg=THEME.background)


class Button(tk.Button):
    def __init__(self, master, **kwargs):
        tk.Button.__init__(self, master=master, **kwargs)
        self.defaultBackground = THEME.button_background
        # This is the hover effect. Binds mouse entry to a function that swaps bg.
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.configure(bg=THEME.button_background, fg=THEME.button_font_color, activebackground=THEME.button_background,
                       activeforeground=THEME.button_font_color, bd=2, relief='groove')

    def on_enter(self, e):
        """Sets the background to the hover color when mouse is over btn. Doesn't work for disabled buttons."""
        if self['state'] == 'normal':
            self['background'] = THEME.button_hover_background

    def on_leave(self, e):
        """Sets the background back to default background when mouse leaves."""
        self['background'] = THEME.button_background


class Text(tk.Text):
    def __init__(self, master, **kwargs):
        tk.Text.__init__(self, master=master, **kwargs)
        self.config(bg=THEME.entry_background, fg=THEME.entry_font_color, insertbackground=THEME.entry_font_color,
                    bd=2, wrap='word')


class Entry(tk.Entry):
    def __init__(self, master, **kwargs):
        tk.Entry.__init__(self, master=master, **kwargs)
        self.config(bg=THEME.entry_background, disabledbackground=THEME.disabled_entry_background, fg=THEME.entry_font_color,
                    insertbackground=THEME.entry_font_color)


class Label(tk.Label):
    def __init__(self, master, **kwargs):
        tk.Label.__init__(self, master=master, **kwargs)
        self.configure(bg=THEME.background, fg=THEME.font_color)


class Radio(tk.Radiobutton):
    def __init__(self, master, **kwargs):
        tk.Radiobutton.__init__(self, master=master, **kwargs)
        self.configure(bg=THEME.background, fg=THEME.font_color, anchor='w',
                       selectcolor=THEME.radio_checkbox_background)


class Checkbutton(tk.Checkbutton):
    def __init__(self, master, **kwargs):
        tk.Checkbutton.__init__(self, master=master, **kwargs)
        self.configure(bg=THEME.background, fg=THEME.font_color, anchor='w',
                       selectcolor=THEME.radio_checkbox_background)


class Scrollbar(tk.Scrollbar):
    def __init__(self, master, **kwargs):
        tk.Scrollbar.__init__(self, master=master, **kwargs)
        self.configure(bg=THEME.entry_background, troughcolor=THEME.background)


class Menu(tk.Menu):
    def __init__(self, master, **kwargs):
        tk.Menu.__init__(self, master=master, **kwargs)
        self.configure(bg=THEME.entry_background, fg=THEME.entry_font_color, activebackground=THEME.button_hover_background,
                       activeforeground=THEME.button_font_color)


class OptionMenu(tk.OptionMenu):
    def __init__(self, variable, *args, **kwargs):
        tk.OptionMenu.__init__(self, variable, *args, **kwargs)
        self.configure(background=THEME.button_background, fg=THEME.button_font_color, activebackground=THEME.button_hover_background,
                       activeforeground=THEME.button_font_color)
        self['menu'].configure(background=THEME.button_background, fg=THEME.button_font_color, activebackground=THEME.button_hover_background,
                               activeforeground=THEME.button_font_color)


class Popup(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.config(bg=THEME.background, padx=10, pady=10)


def file_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# 
def center_window(win):
    """Take the dimensions of the screen and adjust the app window to center within those dimensions."""
    windowwidth = win.winfo_reqwidth()
    windowheight = win.winfo_reqheight()
    positionright = int(win.winfo_screenwidth() / 3 - windowwidth)
    positiondown = int(win.winfo_screenheight() / 2 - windowheight)
    win.geometry("+{}+{}".format(positionright, positiondown))


def center_popup(pop, parent):
    """Takes the measurements of the parent Frame and adjusts the popup's geometry to center within it."""
    positionright = int(parent.winfo_rootx()) + int(parent.winfo_width() / 3)
    positiondown = int(parent.winfo_rooty())
    pop.geometry("+{}+{}".format(positionright, positiondown))


def update(widget, value):
    """Takes updates the widget's text to equal whatever Value is specified."""
    if isinstance(widget, Entry):
        if widget.cget("state") == "disabled":
            widget.config(state="normal")
            widget.delete(0, tk.END)
            widget.insert(0, value)
            widget.config(state="disabled")
        else:
            widget.delete(0, tk.END)
            widget.insert(0, value)
    elif isinstance(widget, Text):
        if widget.cget("state") == "disabled":
            widget.config(state="normal")
            widget.delete("1.0", tk.END)
            widget.insert("1.0", value)
            widget.config(state="disabled")
        else:
            widget.delete("1.0", tk.END)
            widget.insert("1.0", value)
    elif isinstance(widget, Label) or isinstance(widget, Button):
        widget.config(text=value)


def increment(widget, amount: int):
    """Increments an Entry or Label widget by a designated amount. The value MUST be an integer."""
    if isinstance(widget, Entry):
        new_entry = int(widget.get()) + amount
        update(widget, str(new_entry))
    elif isinstance(widget, Label):
        new_label = int(widget.cget("text") + amount)
        widget.configure(text=new_label)


def clear(*widgets):
    """Clears out the text from any Entry, Text, or Label widget."""
    for widget in widgets:
        if isinstance(widget, Entry):
            widget.delete(0, tk.END)
        elif isinstance(widget, Text):
            widget.delete("1.0", tk.END)
        elif isinstance(widget, Label):
            widget.config(text='')


def clip(main: tk.Tk, cliptext: str):
    """Append text to the clipboard"""
    tk.Tk.clipboard_clear(main)
    tk.Tk.clipboard_append(main, cliptext)


def set_theme(theme: Theme):
    global THEME
    THEME = theme


'''
# Display of all modules for theme building
def popuptest():
    pop = Popup()
    center_popup(pop, app)
    

app = Main()
set_theme(Themes.LIGHT)
frame = Frame(app)
menubar = Menu(app)
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="The Menu", menu=menu)
menu.add_command(label="Command")
menu.add_separator()
menu.add_command(label="Exit", command=sys.exit)
app.config(menu=menubar)
label = Label(frame, text="Labels look like this")
button1 = Button(frame, text="Test Button 1", command=popuptest)
button2 = Button(frame, text="clipboard copy")
text = Text(frame, width=20, height=2)
text.insert("1.0", "This is a text widget")
entry = Entry(frame, width=15)
entry.insert(0, "Entry")
variable = tk.StringVar(app)
variable.set("one")
optionmenu = OptionMenu(frame, variable, "one", "two", "three")
radiovar = tk.IntVar(value=1)
radio1 = Radio(frame, text="Radio 1", value=1, variable=radiovar)
radio2 = Radio(frame, text="Radio 2", value=2, variable=radiovar)
checkvar1 = tk.IntVar()
checkvar2 = tk.IntVar()
check1 = Checkbutton(frame, text="Check 1", variable=checkvar1)
check2 = Checkbutton(frame, text="Check 2", variable=checkvar2)

frame.pack()
label.pack()
button1.pack()
button2.pack()
text.pack()
entry.pack()
optionmenu.pack()
radio1.pack()
radio2.pack()
check1.pack()
check2.pack()

app.mainloop()
'''
