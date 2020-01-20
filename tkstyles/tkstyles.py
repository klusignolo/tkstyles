import tkinter as tk
import sys
import os

theme = 14

# ********************** Theme Names *********************
# 0: "Green"
# 1: "Dark"
# 2: "Blue"
# 3: "Love" or "Pink"
# 4: "Yellow"
# 5: "Hufflepuff"
# 6: "Gryffindor"
# 7: "Slytherin"
# 8: "Ravenclaw"
# 9: "Red"
# 10: "Purple"
# 11: "Gold"
# 12: "HCSS"
# 13: "Black and White"
# 14: "Light"
# ********************************************************

# The Main and Frame background.
background = ["#f2fff9", "#191919", "#5895fc", "#ff3f79", "#fffef2", '#dcab20', '#5c0000', '#2a623d', '#222f5b',
              "#cf0202", "#b48efa", "#ffaf2d", "#117011", "#000000", "#ffffff"]
# The Button background.
bbackground = ["#dcede0", "#232323", "#2e62f2", "#e81253", "#efe2d0", '#181818', '#fb8800', '#474747', '#946b2d',
               "#b30000", "#e7d3ff", "#ffb005", "#2f912f", "#ffffff", "#b3f2ff"]
# The Button's Hover background
hbackground = ['#23e046', '#0c0c0c', '#023bd9', "#ce002c", "#ffd52d", '#535353', '#fbb100', '#1a472a', '#9a610a',
               '#ed1818', '#9c38ff', "#ff9800", "#117011", "#ededed", "#d1f7ff"]
# The Entry and Text background
ebackground = ['#d9ffd8', '#474747', '#5e89ff', "#fca9c2", "#fff7d8", "#feeb9f", '#ab4e4e', '#8ddaa7', '#a98957',
               '#eb4444', '#d8a1ff', "#f7be4a", "#ffffff", "#ffffff", "#e0faff"]
# The Disabled Entry background.
dbackground = ['#d2efe4', '#0c0c0c', '#b8c8f5', "#e5d0d7", "#f2eede", "#fceaaa", '#936a6a', '#add0b9', '#ad9673',
               '#de9999', '#eed9f9', "#edc572", "#ededed", "#ededed", "#ffffff"]
# The Radiobutton/Checkbox background
rbackground = ['#d9ffd8', '#474747', '#5e89ff', "#fca9c2", "#fff7d8", "#feeb9f", '#ab4e4e', '#8ddaa7', '#ad9673',
               '#eb4444', '#d8a1ff', "#f7be4a", "#474747", "#474747", "#e0faff"]
# The default Font color
fontcolor = ["#242624", "#efefef", "#000000", "#440014", "#262524", "#1c1c1c", '#d08400', '#000000', '#b8740e',
             "#000000", "#000000", "#4d2e00", "#ffffff", "#ffffff", "#000000"]
# The default Button font color
bfontcolor = ["#242624", "#efefef", "#ffffff", "#440014", "#262524", "#f0e095", '#3c0101', '#d3e4d3', '#08143a',
              "#000000", "#000000", "#4d2e00", "#ffffff", "#000000", "#000000"]
# The default Entry font color
efontcolor = ["#242624", "#efefef", "#000000", "#440014", "#262524", "#1c1c1c", '#3c0101', '#000000', '#060c1f',
              "#000000", "#000000", "#4d2e00", "#000000", "#000000", "#000000"]


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        Main.configure(self, bg=background[theme])

        # This chunk is for centering the app within the window when it's launched.
        center_window(self)


class Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        Frame.configure(self, bg=background[theme])


class Toplevel(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.configure(bg=background[theme])


class Button(tk.Button):
    def __init__(self, master, **kwargs):
        tk.Button.__init__(self, master=master, **kwargs)
        self.defaultBackground = bbackground
        # This is the hover effect. Binds mouse entry to a function that swaps bg.
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.configure(bg=bbackground[theme], fg=bfontcolor[theme], activebackground=bbackground[theme],
                       activeforeground=bfontcolor[theme], bd=2, relief='groove')

    # Sets the background to the hover color when mouse is over btn. Doesn't work for disabled buttons.
    def on_enter(self, e):
        if self['state'] == 'normal':
            self['background'] = hbackground[theme]

    # Sets the background back to default background when mouse leaves.
    def on_leave(self, e):
        self['background'] = bbackground[theme]


class Text(tk.Text):
    def __init__(self, master, **kwargs):
        tk.Text.__init__(self, master=master, **kwargs)
        self.config(bg=ebackground[theme], fg=efontcolor[theme], insertbackground=efontcolor[theme],
                    bd=2, wrap='word')


class Entry(tk.Entry):
    def __init__(self, master, **kwargs):
        tk.Entry.__init__(self, master=master, **kwargs)
        self.config(bg=ebackground[theme], disabledbackground=dbackground[theme], fg=efontcolor[theme],
                    insertbackground=efontcolor[theme])


class Label(tk.Label):
    def __init__(self, master, **kwargs):
        tk.Label.__init__(self, master=master, **kwargs)
        self.configure(bg=background[theme], fg=fontcolor[theme])


class Radio(tk.Radiobutton):
    def __init__(self, master, **kwargs):
        tk.Radiobutton.__init__(self, master=master, **kwargs)
        self.configure(bg=background[theme], fg=fontcolor[theme], anchor='w',
                       selectcolor=rbackground[theme])


class Checkbutton(tk.Checkbutton):
    def __init__(self, master, **kwargs):
        tk.Checkbutton.__init__(self, master=master, **kwargs)
        self.configure(bg=background[theme], fg=fontcolor[theme], anchor='w',
                       selectcolor=rbackground[theme])


class Scrollbar(tk.Scrollbar):
    def __init__(self, master, **kwargs):
        tk.Scrollbar.__init__(self, master=master, **kwargs)
        self.configure(bg=ebackground[theme], troughcolor=background[theme])


class Menu(tk.Menu):
    def __init__(self, master, **kwargs):
        tk.Menu.__init__(self, master=master, **kwargs)
        self.configure(bg=ebackground[theme], fg=efontcolor[theme], activebackground=hbackground[theme],
                       activeforeground=bfontcolor[theme])


class OptionMenu(tk.OptionMenu):
    def __init__(self, variable, *args, **kwargs):
        tk.OptionMenu.__init__(self, variable, *args, **kwargs)
        self.configure(background=bbackground[theme], fg=bfontcolor[theme], activebackground=hbackground[theme],
                       activeforeground=bfontcolor[theme])
        self['menu'].configure(background=bbackground[theme], fg=bfontcolor[theme], activebackground=hbackground[theme],
                               activeforeground=bfontcolor[theme])


class Popup(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.config(bg=background[theme], padx=10, pady=10)


def file_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# This method takes the dimensions of the user's screen and adjusts the app to center within those dimensions.
def center_window(win):
    windowwidth = win.winfo_reqwidth()
    windowheight = win.winfo_reqheight()
    positionright = int(win.winfo_screenwidth() / 3 - windowwidth)
    positiondown = int(win.winfo_screenheight() / 2 - windowheight)
    win.geometry("+{}+{}".format(positionright, positiondown))


# This method takes the measurements of the parent Frame and adjusts the popup's geometry to center it.
def center_popup(pop, parent):
    positionright = int(parent.winfo_rootx()) + int(parent.winfo_width() / 3)
    positiondown = int(parent.winfo_rooty())
    pop.geometry("+{}+{}".format(positionright, positiondown))


# Takes updates the widget's text to equal whatever Value is specified.
def update(widget, value):
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


# Increments an Entry or Label widget by a designated amount. The value MUST be an integer.
def increment(widget, amount):
    if isinstance(widget, Entry):
        new_entry = int(widget.get()) + amount
        update(widget, str(new_entry))
    elif isinstance(widget, Label):
        new_label = int(widget.cget("text") + amount)
        widget.configure(text=new_label)


# This Function clears out a Tkinter Entry, but does not insert a new value.
def clear(*widgets):
    for widget in widgets:
        if isinstance(widget, Entry):
            widget.delete(0, tk.END)
        elif isinstance(widget, Text):
            widget.delete("1.0", tk.END)
        elif isinstance(widget, Label):
            widget.config(text='')


def clip(main, cliptext):
    tk.Tk.clipboard_clear(main)
    tk.Tk.clipboard_append(main, cliptext)


def set_theme(theme_name):
    global theme
    if theme_name.lower() == 'green':
        theme = 0
    if theme_name.lower() == 'dark':
        theme = 1
    if theme_name.lower() == 'blue':
        theme = 2
    if theme_name.lower() == 'love' or theme_name.lower() == 'pink':
        theme = 3
    if theme_name.lower() == 'yellow':
        theme = 4
    if theme_name.lower() == 'hufflepuff':
        theme = 5
    if theme_name.lower() == 'gryffindor':
        theme = 6
    if theme_name.lower() == 'slytherin':
        theme = 7
    if theme_name.lower() == 'ravenclaw':
        theme = 8
    if theme_name.lower() == 'red':
        theme = 9
    if theme_name.lower() == 'purple':
        theme = 10
    if theme_name.lower() == 'gold':
        theme = 11
    if theme_name.lower() == 'hcss':
        theme = 12
    if theme_name.lower() == 'black and white':
        theme = 13
    if theme_name.lower() == 'light':
        theme = 14


'''
# Display of all modules for theme building
def popuptest():
    pop = Popup()
    center_popup(pop, app)

app = Main()
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
button2 = Button(frame, text="clipboard copy", command=lambda: clip(app, entry.get()))
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
