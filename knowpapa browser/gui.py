#!usr/bin/python
from Tkinter import *
from ScrolledText import *
import urlhandler
def go():
	text.delete(1.0, END)
	conn = urlhandler.urlhandler(entry.get())
	conn.openURL()
	text.insert(INSERT, conn.getURLdata())
	conn.closeURL()
browserwindow = Tk()
browserwindow.title('knowpapa browser')
label = Label(browserwindow, text= 'url:')
entry = Entry(browserwindow)
button = Button(browserwindow, text='Go', command = go)
text = ScrolledText(browserwindow)
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
text.pack(side= TOP)
browserwindow.mainloop() 
