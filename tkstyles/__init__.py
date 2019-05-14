import tkinter as tk
import sys
import os

theme = 2
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
# ********************************************************

# The Main and Frame background.
background = ["#f2fff9", "#191919", "#f2f7ff", "#ff3f79", "#fffef2", '#dcab20', '#5c0000', '#2a623d', '#222f5b']
# The Button background.
bbackground = ["#dcede0", "#232323", "#dce2ed", "#e81253", "#efe2d0", '#181818', '#fb8800', '#474747', '#946b2d']
# The Button's Hover background
hbackground = ['#23e046', '#0c0c0c', '#d8e8ff', "#ce002c", "#ffd52d", '#535353', '#fbb100', '#1a472a', '#9a610a']
# The Entry and Text background
ebackground = ['#d9ffd8', '#474747', '#d8e8ff', "#fca9c2", "#fff7d8", "#feeb9f", '#ab4e4e', '#8ddaa7', '#a98957']
# The Disabled Entry background.
dbackground = ['#d2efe4', '#0c0c0c', '#d9e9f9', "#e5d0d7", "#f2eede", "#fceaaa", '#936a6a', '#add0b9', '#ad9673']
# The default Font color
fontcolor = ["#242624", "#efefef", "#242526", "#440014", "#262524", "#1c1c1c", '#d08400', '#000000', '#b8740e']
# The default Button font color
bfontcolor = ["#242624", "#efefef", "#242526", "#440014", "#262524", "#f0e095", '#3c0101', '#d3e4d3', '#08143a']
# The default Entry font color
efontcolor = ["#242624", "#efefef", "#242526", "#440014", "#262524", "#1c1c1c", '#3c0101', '#000000', '#060c1f']


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        Main.configure(self, bg=background[theme])

        # This chunk is for centering the app within the window when it's launched.
        center_window(self)


class Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        Frame.configure(self, bg=background[theme], padx=5, pady=5)


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
                       selectcolor=ebackground[theme])


class Scrollbar(tk.Scrollbar):
    def __init__(self, master, **kwargs):
        tk.Scrollbar.__init__(self, master=master, **kwargs)
        self.configure(bg=ebackground[theme], troughcolor=background[theme])


class Menu(tk.Menu):
    def __init__(self, master, **kwargs):
        tk.Menu.__init__(self, master=master, **kwargs)
        self.configure(bg=ebackground[theme], fg=efontcolor[theme], activebackground=background[theme],
                       activeforeground=bfontcolor[theme])


class OptionMenu(tk.OptionMenu):
    def __init__(self, variable, *args, **kwargs):
        tk.OptionMenu.__init__(self, variable, *args, **kwargs)
        self.configure(background=bbackground[theme], fg=bfontcolor[theme], activebackground=hbackground[theme],
                       activeforeground=bfontcolor[theme])
        self['menu'].configure(background=bbackground[theme], fg=bfontcolor[theme], activebackground=hbackground[theme],
                               activeforeground=bfontcolor[theme])


class Popup(tk.Toplevel):
    self.config(bg=background[theme])


def popup(message):
    pop = tk.Toplevel()
    center_popup(pop, self)
    pop.wm_title("Message")
    pop.config(bg=background[theme], padx=25)

    def close(self):
        pop.destroy()

    text = Label(pop, text=message)
    okbtn = Button(pop, text="OK", width=20, command=lambda: close(pop))
    text.pack()
    okbtn.pack()
    pop.bind('<Return>', close)
    pop.focus()


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


def update(entry, value):
    entry.delete(0, tk.END)
    entry.insert(0, value)


# This Function Updates Entries that are disabled by activating them, running update, and disabling.
def update_disabled(entry, value):
    entry.config(state="normal")
    update(entry, value)
    entry.config(state="disabled")


# This Function clears out a Tkinter Entry, but does not insert a new value.
def clear(*args):
    for arg in args:
        arg.delete(0, tk.END)


def clip(entry_widget):
    self.clipboard_clear()
    self.clipboard_append(entry_widget)


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


"""
#Display of all modules for theme building 

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
button = Button(frame, text="This is a button")
text = Text(frame, width=20, height=2)
text.insert("1.0", "This is a text widget")
entry = Entry(frame, width=15)
entry.insert(0, "Entry")
variable = tk.StringVar(app)
variable.set("one")
optionmenu = OptionMenu(frame, variable, "one", "two", "three")

frame.pack()
label.pack()
button.pack()
text.pack()
entry.pack()
optionmenu.pack()

app.mainloop()
"""
