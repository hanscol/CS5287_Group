import sys
from tkinter import *

CONFIG_FILE_PATH = 'config.txt'

class Application(Frame):

    def config_callback(self):
        options = parse_config(CONFIG_FILE_PATH)
        for option in self.wrap:
            if option[:5] == 'entry' and self.wrap[option].get():
                options[option[6:]] = self.wrap[option].get()
        #options = self.wrap[].get()
        write_config(CONFIG_FILE_PATH, options)
        self.quit()

    def create_widgets(self):
        self.master.title("Configure")
        wrap = {}
        user_param_file = open(CONFIG_FILE_PATH, 'r')
        user_param_file = user_param_file.readlines()
        col_count = 0
        row_count = 0
        max_row_count = 0
        for line in user_param_file:
            if (len(line) > 1) & (line[0] != '*'):
                line = line.split(": ")
                wrap['label_' + line[0]] = Label(self, text=line[0])
                wrap['label_' + line[0]].grid(row=row_count, column=col_count)
                row_count += 1
                wrap['entry_' + line[0]] = Entry(self)
                wrap['entry_' + line[0]].grid(row=row_count, column=col_count)
                row_count += 1
            else:
                if line[0] == '*':
                    col_count+=1
                    if max_row_count < row_count:
                        max_row_count = row_count
                    row_count = 0
                    wrap['label_' + line] = Label(self, text=line.strip('\n. '))
                    wrap['label_' + line].grid(row=row_count, column=col_count)
                    row_count += 1
        if max_row_count < row_count:
            max_row_count = row_count
        self.wrap = wrap

        self.exit = Button(self, text='Cancel', command=self.quit).grid(row=max_row_count+1, column=0)
        #self.exit["text"] = "Cancel"
        #self.exit["fg"] = "red"
        #self.exit["command"] = self.quit
        #self.exit.pack({"side": "left"})

        self.start = Button(self, text='Configure', command=self.config_callback).grid(row=max_row_count+1, column=1, sticky=W)
        #self.start["text"] = "Configure",
        #self.start["command"] = self.config_callback
        #self.start.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

def parse_config(user_param_file_path):
    user_param_file = open(user_param_file_path, 'r')
    user_param_file = user_param_file.readlines()
    options = {}
    for line in user_param_file:
        if (len(line) > 1) & (line[0] != '*'):
            line = line.split(": ")
            options[line[0]] = line[1].strip('\n')
    return options

def write_config(user_param_file_path, options):
    user_param_file_read = open(user_param_file_path, 'r')
    user_param_file_lines = user_param_file_read.readlines()
    user_param_file_write = open(user_param_file_path, 'w+')
    for line in user_param_file_lines:
        if (len(line) > 1) & (line[0] != '*'):
            line = line.split(": ")
            user_param_file_write.write(line[0]+': '+options[line[0]])
            user_param_file_write.write('\n')
        else:
            user_param_file_write.write(line)
    user_param_file_write.close()

def main(argv):
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()

if __name__ == "__main__":
    main(sys.argv)