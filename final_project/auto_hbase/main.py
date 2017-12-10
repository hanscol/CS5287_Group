import sys
import hbase_config
from tkinter import *

class Application(Frame):

    def config_callback(self):
        test = self.entry_rootdir.get()
        hbase_config.site_config(test, test, test, test, test, test, test, test, test)


    def create_widgets(self):
        self.master.title("Configure")

        self.label_rootdir = Label(self, text="hbase.rootdir")
        self.label_rootdir.pack()
        self.entry_rootdir = Entry(self)
        self.entry_rootdir.pack()

        self.exit = Button(self)
        self.exit["text"] = "Cancel"
        self.exit["fg"] = "red"
        self.exit["command"] = self.quit
        self.exit.pack({"side": "left"})

        self.start = Button(self)
        self.start["text"] = "Configure",
        self.start["command"] = self.config_callback
        self.start.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

def main(argv):
    test = 'help'
    hbase_config.site_config(test, test, test, test, test, test, test, test, test)
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()

if __name__ == "__main__":
    main(sys.argv)