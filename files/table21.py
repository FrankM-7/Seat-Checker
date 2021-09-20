import tkinter as tk
from prettytable import PrettyTable
from datetime import datetime
from sys import exit

# start root
root = tk.Tk()
# start my label for my root window
label_1 = tk.Label(root, width=24)
# add the label to my window
label_1.pack()

# my table
dataTable = PrettyTable()
# headers
dataTable.field_names = ["CRN", "Available", "Max", "Time"]


# function for adding a new line every 30 secs
def addnew():
    global process
    # time
    now = datetime.now()
    # second right now
    currentSecond = now.strftime("%S")
    # ever 30 seconds run this
    if (int(currentSecond) % 30) == 0:
        label_1.after(2000)
        data = open('data1.csv', 'r').readlines()
        try:
            for i in range(len(lists)-1):
                if int(data[process].split(',')[1]) > 0:
                    dataTable.add_row(data[process].rstrip().split(','))
                    label_1.config(text=dataTable)
                    label_1.after(1000, addnew)
                process += 1
        except:
            exit()
    label_1.after(1000, addnew)


process = 0
classLinks = open('classLinks.csv', 'r')
lists = classLinks.readlines()[0].split(',')
addnew()
root.mainloop()

