# tkstyles


tkstyles is a small library designed to work with the native tkinter gui development library. The classes are all tkinter widgets with the ability to declare a theme.

  - import tkstyles (no need to import tkinter as well)
  - set_theme("hufflepuff")
  - Declare, grid, and pack your widgets.
  - Magic.



### Installation
tkstyles can be installed using regular pip. There are no dependencies as the module only relies on what comes native to Python.

pip install tkstyles


### Todos

 - Add more themes.
 - Add possible support for certain ttk widgets.
 - Figure out a function to swap the theme within apps.

### Sample App:
from tkstyles import *

app = Main()
frame = Frame(app)

menubar = Menu(app)
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="The Menu", menu=menu)
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



License
----

MIT


**Free Stuff, Hell Yeah!**

