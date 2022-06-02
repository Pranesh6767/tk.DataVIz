from tkinter import *
from tkinter import ttk

root_window = Tk()

estyle = ttk.Style()
estyle.element_create("plain.field", "from", "clam")

estyle.layout("EntryStyle.TEntry",
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])
estyle.configure("EntryStyle.TEntry",
                 background="green",
                 foreground="grey",
                 fieldbackground="black")
entry_v = StringVar()
entry = ttk.Entry(root_window, style="EntryStyle.TEntry", textvariable=entry_v)
entry.pack(padx=10, pady=10)
root_window.mainloop()