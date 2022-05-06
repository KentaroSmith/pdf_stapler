from PyPDF2 import PdfFileMerger
from tkinter import *
from tkinter import ttk
from shutil import move

import os
root = Tk()
#root.iconbitmap('pdf.ico')
root.geometry("500x300")
root.title("PDF Stapler")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
style = ttk.Style()
style.configure('tab.background', background = "white")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
tab_control = ttk.Notebook(mainframe)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Combine docs")

this_folder = StringVar("")
doc_title = StringVar("")

def make_document():
    merger = PdfFileMerger()
    #this_folder= input("Enter the file path for this month's folder: ")
    global this_folder
    global doc_title 
    this_folder = str(this_folder.get())
    doc_title = str(doc_title.get())
    pdfs = os.listdir(this_folder)
    for pdf in pdfs:
        location = this_folder + "\\" +pdf
        merger.append(location)
    #doc_title = input("Enter the new document title: ")
    doc_title = doc_title+".pdf"
    merger.write(doc_title)
    merger.close()
    move(doc_title, this_folder)

tab_one_data = [
    [this_folder, "Enter the file path to your folder: "],
    [doc_title, "Enter the title of the new document: "]
]

def LineItem(tab, tab_data, row_num, item_data, description):
    variables = []
    for item in tab_data:
        num = str(tab_data.index(item))
        data = "info"
        data_label = "display"
        variables = [data+num, data_label+num]
    if tab == tab1:    
        variables[0] = Entry(tab, text=item_data, width=200)
        variables[1] = Label(tab, text = description)
        variables[1].grid(column = 2, row = row_num)
        variables[0].grid(column = 3, row = row_num)

    

def tab_display(tab, tab_data):
    row_number = 2
    for data in tab_data:
        LineItem(tab, tab_data, row_number, data[0], data[1])
        row_number += 1

tab_display(tab1, tab_one_data)
ttk.Button(tab1, text="Combine files", command=make_document).grid(column = 2, row = 15, sticky = E)
ttk.Label(tab1, text="Place all of the PDF's you wish to combine into one folder").grid(column=2, row=1, sticky=N)
tab_control.pack(expand=1, fill = 'both')
root.mainloop()