# tkstyles


tkstyles is a small library designed to work with the native tkinter gui development library. The classes are all tkinter widgets with the ability to declare a theme. Each theme will adjust the color scheme of widgets at the same time. I purposefully did not let themes change any text style aside from color.

  - import tkstyles
  - set_theme(THEMES.Hufflepuff)
  - Declare, grid, and pack widgets.
  - Magic.


### Installation
tkstyles can be installed using regular pip. There are no dependencies as the module only relies on what comes native to Python.

```python
pip install tkstyles
```

### Sample App:
```python
import tkstyles as ui
import sys 

app = ui.Main()
frame = ui.Frame(app)
ui.set_theme(ui.Theme.BLUE)

menubar = ui.Menu(app)
menu = ui.Menu(menubar, tearoff=0)
menubar.add_cascade(label="The Menu", menu=menu)
menu.add_command(label="Exit", command=sys.exit)
app.config(menu=menubar)

label = ui.Label(frame, text="Labels look like this")

button = ui.Button(frame, text="This is a button")

text = ui.Text(frame, width=20, height=2)
text.insert("1.0", "This is a text widget")

entry = ui.Entry(frame, width=15)
entry.insert(0, "Entry")

variable = ui.tk.StringVar(app)
variable.set("one")
optionmenu = ui.OptionMenu(frame, variable, "one", "two", "three")

frame.pack()
label.pack()
button.pack()
text.pack()
entry.pack()
optionmenu.pack()

app.mainloop()
```


License
----

MIT


**Free Stuff, Hell Yeah!**

